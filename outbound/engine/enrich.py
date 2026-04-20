"""Batch-Enrichment: Websites lesen, Signale extrahieren, Scores aktualisieren."""

import re
import time
import httpx
from html.parser import HTMLParser

from .db import get_db, add_signal, upsert_score, update_kanzlei, get_signals
from .scraper import parse_homepage, parse_team_page, parse_career_page, analyze_text
from .scorer import suggest_scores


class _HTMLTextExtractor(HTMLParser):
    """Extrahiert sichtbaren Text aus HTML."""

    def __init__(self):
        super().__init__()
        self._text = []
        self._skip = False
        self._skip_tags = {"script", "style", "noscript", "svg", "path"}

    def handle_starttag(self, tag, attrs):
        if tag in self._skip_tags:
            self._skip = True

    def handle_endtag(self, tag):
        if tag in self._skip_tags:
            self._skip = False

    def handle_data(self, data):
        if not self._skip:
            text = data.strip()
            if text:
                self._text.append(text)

    def get_text(self) -> str:
        return " ".join(self._text)


def html_to_text(html: str) -> str:
    """Konvertiert HTML zu reinem Text."""
    extractor = _HTMLTextExtractor()
    try:
        extractor.feed(html)
    except Exception:
        pass
    return extractor.get_text()


def _find_subpage_urls(html: str, base_domain: str) -> dict:
    """Findet Team-, Karriere- und Über-uns-Seiten in HTML-Links."""
    urls = {}
    # Regex für href-Attribute
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', html, re.IGNORECASE)

    team_patterns = ["team", "ueber-uns", "über-uns", "about", "unser-team", "mitarbeiter", "kanzlei"]
    career_patterns = ["karriere", "career", "jobs", "stellenangebot", "stellenangebote", "arbeiten-bei"]

    for href in hrefs:
        href_lower = href.lower()
        # Nur interne Links
        if href.startswith("/") or base_domain in href:
            for pat in team_patterns:
                if pat in href_lower and "team" not in urls:
                    urls["team"] = href
                    break
            for pat in career_patterns:
                if pat in href_lower and "career" not in urls:
                    urls["career"] = href
                    break

    return urls


def _make_absolute(url: str, base_url: str) -> str:
    """Macht relative URL absolut."""
    if url.startswith("http"):
        return url
    if url.startswith("//"):
        return "https:" + url
    if url.startswith("/"):
        from urllib.parse import urlparse
        parsed = urlparse(base_url)
        return f"{parsed.scheme}://{parsed.netloc}{url}"
    return base_url.rstrip("/") + "/" + url


def fetch_page(url: str, timeout: float = 10.0) -> tuple[str, str]:
    """Holt eine Seite. Gibt (html, text) zurück."""
    if not url.startswith("http"):
        url = "https://" + url

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "de-DE,de;q=0.9",
    }

    try:
        resp = httpx.get(url, headers=headers, timeout=timeout, follow_redirects=True)
        resp.raise_for_status()
        html = resp.text
        text = html_to_text(html)
        return html, text
    except Exception as e:
        return "", ""


def enrich_kanzlei(kanzlei_id: int, verbose: bool = False) -> dict:
    """Reichert eine einzelne Kanzlei an: Website lesen, Signale extrahieren, scoren.

    Returns:
        Dict mit enrichment-Ergebnis.
    """
    with get_db() as conn:
        row = conn.execute("SELECT * FROM kanzleien WHERE id = ?", (kanzlei_id,)).fetchone()
        if not row:
            return {"error": f"Kanzlei {kanzlei_id} nicht gefunden"}
        k = dict(row)

    domain = k["domain"]
    website = k["website"] or f"https://{domain}"
    if verbose:
        print(f"  [{kanzlei_id}] {domain}...", end=" ", flush=True)

    # Homepage lesen
    html, text = fetch_page(website)
    if not text or len(text) < 50:
        if verbose:
            print("SKIP (kein Inhalt)")
        return {"id": kanzlei_id, "domain": domain, "status": "no_content"}

    # Homepage-Signale
    homepage_signals = parse_homepage(text)
    for dim, data in homepage_signals.items():
        add_signal(kanzlei_id, dim,
                   f"Homepage: {', '.join(data['matches'][:5])}",
                   website, "website")

    # Team-Seite suchen und lesen
    subpages = _find_subpage_urls(html, domain)
    team_data = {}
    if "team" in subpages:
        team_url = _make_absolute(subpages["team"], website)
        _, team_text = fetch_page(team_url)
        if team_text:
            team_data = parse_team_page(team_text)
            if team_data.get("estimated_size", 0) > 0:
                update_kanzlei(kanzlei_id, estimated_size=team_data["estimated_size"])
                add_signal(kanzlei_id, "size",
                           f"Team-Seite: ~{team_data['estimated_size']} Personen, Rollen: {', '.join(team_data.get('roles', [])[:5])}",
                           team_url, "website")
            if "team" in subpages:
                update_kanzlei(kanzlei_id, team_page_url=team_url)
            for dim, matches in team_data.get("signals", {}).items():
                add_signal(kanzlei_id, dim, f"Team-Seite: {', '.join(matches[:3])}", team_url, "website")

    # Karriere-Seite suchen und lesen
    career_data = {}
    if "career" in subpages:
        career_url = _make_absolute(subpages["career"], website)
        _, career_text = fetch_page(career_url)
        if career_text:
            career_data = parse_career_page(career_text)
            update_kanzlei(kanzlei_id, career_page_url=career_url)
            if career_data.get("job_count", 0) > 0:
                add_signal(kanzlei_id, "recruiting",
                           f"Karriere-Seite: {career_data['job_count']} Stellen ({', '.join(career_data.get('jobs_found', [])[:3])})",
                           career_url, "career")
            if career_data.get("datev_mentioned"):
                add_signal(kanzlei_id, "datev", "DATEV in Stellenanzeige erwähnt", career_url, "career")
            if career_data.get("fibu_mentioned"):
                add_signal(kanzlei_id, "fibu", "FiBu in Stellenanzeige erwähnt", career_url, "career")

    # Neu scoren mit allen Signalen
    all_signals = get_signals(kanzlei_id)
    score_result = suggest_scores(k, all_signals)
    upsert_score(
        kanzlei_id,
        score_result["scores"],
        score_result["ko_hit"],
        score_result["ko_reason"],
        score_result["summary"],
        scored_by="auto_enrich",
    )

    if verbose:
        print(f"{score_result['total']}/20 Tier {score_result['tier']}")

    return {
        "id": kanzlei_id,
        "domain": domain,
        "status": "enriched",
        "total": score_result["total"],
        "tier": score_result["tier"],
        "homepage_signals": len(homepage_signals),
        "team_size": team_data.get("estimated_size", 0),
        "career_jobs": career_data.get("job_count", 0),
    }


def batch_enrich(min_prescore: int = 5, limit: int = 200, verbose: bool = True) -> list[dict]:
    """Batch-Enrichment der Top-Kandidaten.

    Args:
        min_prescore: Minimaler Vorscore für Enrichment
        limit: Max. Anzahl zu verarbeiten
        verbose: Ausgabe pro Kanzlei

    Returns:
        Liste von Enrichment-Ergebnissen.
    """
    with get_db() as conn:
        rows = conn.execute("""
            SELECT k.id, k.domain, s.total
            FROM kanzleien k
            JOIN scores s ON k.id = s.kanzlei_id
            WHERE s.ko_hit = 0 AND s.total >= ? AND s.scored_by != 'auto_enrich'
            ORDER BY s.total DESC
            LIMIT ?
        """, (min_prescore, limit)).fetchall()

    candidates = [dict(r) for r in rows]
    if verbose:
        print(f"Enrichment: {len(candidates)} Kandidaten (Score >= {min_prescore})")

    results = []
    for i, c in enumerate(candidates):
        result = enrich_kanzlei(c["id"], verbose=verbose)
        results.append(result)
        # Rate limiting: nicht zu schnell fetchen
        time.sleep(0.3)

    # Zusammenfassung
    enriched = [r for r in results if r.get("status") == "enriched"]
    no_content = [r for r in results if r.get("status") == "no_content"]

    if verbose:
        print(f"\n=== Enrichment-Ergebnis ===")
        print(f"Verarbeitet: {len(results)}")
        print(f"Angereichert: {len(enriched)}")
        print(f"Kein Inhalt: {len(no_content)}")

        # Neue Tier-Verteilung
        tiers = {}
        for r in enriched:
            t = r.get("tier", "?")
            tiers[t] = tiers.get(t, 0) + 1
        print(f"Tier-Verteilung: {tiers}")

    return results
