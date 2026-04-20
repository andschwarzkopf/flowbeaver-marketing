"""BraveSearch API Wrapper und Query-Strategie für Lead Discovery."""

import time
import httpx

from .config import (
    BRAVE_API_KEY, BRAVE_API_URL, BRAVE_RATE_LIMIT_SEC,
    REGIONS, TIER1_QUERY_TEMPLATES, TIER2_QUERY_TEMPLATES,
)
from .db import add_kanzlei, log_search_run, get_kanzlei_by_domain
from .models import SearchResult

_last_request_time = 0.0


def _rate_limit():
    """Wartet wenn nötig, um Rate-Limit einzuhalten."""
    global _last_request_time
    elapsed = time.time() - _last_request_time
    if elapsed < BRAVE_RATE_LIMIT_SEC:
        time.sleep(BRAVE_RATE_LIMIT_SEC - elapsed)
    _last_request_time = time.time()


def brave_search(query: str, count: int = 20) -> list[dict]:
    """Führt eine Brave Web Search aus. Gibt Roh-Ergebnisse zurück."""
    if not BRAVE_API_KEY:
        raise ValueError("BRAVE_API_KEY nicht gesetzt. Bitte als Umgebungsvariable setzen.")

    _rate_limit()

    response = httpx.get(
        BRAVE_API_URL,
        params={
            "q": query,
            "count": count,
            "search_lang": "de",
            "country": "DE",
        },
        headers={
            "Accept": "application/json",
            "Accept-Encoding": "gzip",
            "X-Subscription-Token": BRAVE_API_KEY,
        },
        timeout=15.0,
    )
    response.raise_for_status()
    data = response.json()
    return data.get("web", {}).get("results", [])


def _normalize_domain(url: str) -> str:
    """Extrahiert Domain ohne www."""
    from urllib.parse import urlparse
    if not url:
        return ""
    parsed = urlparse(url)
    domain = parsed.netloc.lower()
    if domain.startswith("www."):
        domain = domain[4:]
    return domain


def _is_kanzlei_domain(domain: str) -> bool:
    """Filtert offensichtlich irrelevante Domains (Verzeichnisse, Portale, Social Media)."""
    skip_domains = {
        "linkedin.com", "xing.com", "facebook.com", "instagram.com", "youtube.com",
        "twitter.com", "kununu.com", "indeed.com", "stepstone.de", "monster.de",
        "glassdoor.de", "northdata.de", "bundesanzeiger.de",
        "google.com", "google.de", "bing.com",
        "steuerberater.de", "stbverband.de", "datev.de",
        "wikipedia.org", "wiktionary.org",
        "gelbeseiten.de", "11880.com", "dasoertliche.de", "meinestadt.de",
        "provenexpert.com", "trustpilot.com", "whofinance.de",
        "haufe.de", "lexware.de", "buhl.de", "sevdesk.de", "lexoffice.de",
    }
    return domain not in skip_domains and not domain.endswith(".gov.de")


def extract_results(raw_results: list[dict], query: str, city: str) -> list[SearchResult]:
    """Konvertiert Brave-Rohergebnisse in SearchResult-Objekte, filtert irrelevante."""
    results = []
    seen_domains = set()

    for item in raw_results:
        url = item.get("url", "")
        domain = _normalize_domain(url)

        if not domain or domain in seen_domains or not _is_kanzlei_domain(domain):
            continue

        seen_domains.add(domain)
        results.append(SearchResult(
            title=item.get("title", ""),
            url=url,
            domain=domain,
            description=item.get("description", ""),
            query=query,
            city=city,
        ))

    return results


def run_discovery(region_key: str, tier2: bool = True, count_per_query: int = 20) -> dict:
    """Führt Discovery für eine Region aus. Gibt Zusammenfassung zurück.

    Returns:
        dict mit keys: total_results, new_kanzleien, duplicates, queries_run, results (list)
    """
    if region_key not in REGIONS:
        raise ValueError(f"Unbekannte Region: {region_key}. Verfügbar: {list(REGIONS.keys())}")

    region = REGIONS[region_key]
    all_results = []
    seen_domains = set()
    new_count = 0
    dup_count = 0
    queries_run = 0

    templates = TIER1_QUERY_TEMPLATES + (TIER2_QUERY_TEMPLATES if tier2 else [])

    for city in region["cities"]:
        for template in templates:
            query = template.format(city=city)
            print(f"  Suche: {query}")

            try:
                raw = brave_search(query, count=count_per_query)
            except Exception as e:
                print(f"  FEHLER bei '{query}': {e}")
                continue

            queries_run += 1
            results = extract_results(raw, query, city)

            for r in results:
                if r.domain in seen_domains:
                    continue
                seen_domains.add(r.domain)

                # Prüfe ob schon in DB
                existing = get_kanzlei_by_domain(r.domain)
                if existing:
                    dup_count += 1
                    continue

                # In DB eintragen
                kanzlei_id = add_kanzlei(
                    name=r.title,
                    website=r.url,
                    city=city,
                    region=region_key,
                    source="brave_search",
                    notes=f"Query: {query}\nBeschreibung: {r.description}",
                )
                if kanzlei_id:
                    new_count += 1
                    all_results.append({
                        "id": kanzlei_id,
                        "name": r.title,
                        "domain": r.domain,
                        "city": city,
                        "url": r.url,
                        "description": r.description,
                    })
                else:
                    dup_count += 1

            log_search_run(
                query=query, city=city, region=region_key,
                results_count=len(results), new_count=sum(1 for r in results if r.domain not in seen_domains),
            )

    summary = {
        "region": region["label"],
        "total_results": len(seen_domains),
        "new_kanzleien": new_count,
        "duplicates": dup_count,
        "queries_run": queries_run,
        "results": all_results,
    }

    print(f"\n--- {region['label']} ---")
    print(f"  Queries: {queries_run}")
    print(f"  Gefunden: {len(seen_domains)} unique Domains")
    print(f"  Neu in DB: {new_count}")
    print(f"  Duplikate: {dup_count}")

    return summary
