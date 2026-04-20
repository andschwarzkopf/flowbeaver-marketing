"""Verifikation: Websites besuchen, FiBu/Recruiting/Digital gezielt prüfen."""

import time
import re
from .enrich import fetch_page, html_to_text, _find_subpage_urls, _make_absolute
from .db import get_db, add_signal, upsert_score, update_kanzlei, get_signals

# Strenge Keyword-Sets: muss KLAR auf der Website stehen
FIBU_KEYWORDS = [
    "finanzbuchhaltung", "fibu", "laufende buchhaltung", "monatliche buchhaltung",
    "buchführung", "belegbearbeitung", "vorkontierung", "buchungsstapel",
    "buchhaltung für mandanten", "belegmanagement", "rechnungswesen",
    "anlagenbuchhaltung", "debitoren", "kreditoren", "kontierung",
    "jahresabschluss", "einnahmenüberschussrechnung", "bilanz",
]

RECRUITING_KEYWORDS = [
    "stellenangebot", "karriere", "offene stellen", "jobs",
    "wir suchen", "verstärkung", "bewerbung", "team wächst",
    "mitarbeiter gesucht", "steuerfachangestellte", "bilanzbuchhalter",
    "finanzbuchhalter", "lohnbuchhalter", "steuerberater gesucht",
    "jetzt bewerben", "initiativbewerbung", "ausbildungsplatz",
    "(m/w/d)", "arbeiten bei", "werde teil",
]

DIGITAL_KEYWORDS = [
    "digitalisierung", "digitale kanzlei", "digitale buchhaltung",
    "datev unternehmen online", "duo", "datev", "dms",
    "dokumentenmanagement", "e-rechnung", "papierlos", "cloud",
    "mandantenportal", "belegupload", "scan", "automatisierung",
    "digitale prozesse", "digital", "datev smarttransfer",
    "datev meine steuern", "online buchhaltung",
]


def _check_keywords(text: str, keywords: list[str]) -> dict:
    """Prüft ob Keywords klar im Text vorkommen."""
    text_lower = text.lower()
    found = []
    for kw in keywords:
        if kw.lower() in text_lower:
            found.append(kw)
    return {
        "found": found,
        "count": len(found),
        "present": len(found) >= 2,  # Mindestens 2 verschiedene Keywords
    }


def verify_kanzlei(kanzlei_id: int, verbose: bool = True) -> dict:
    """Besucht Website und prüft FiBu, Recruiting, Digital."""
    with get_db() as conn:
        row = conn.execute("SELECT * FROM kanzleien WHERE id = ?", (kanzlei_id,)).fetchone()
        if not row:
            return {"id": kanzlei_id, "error": "nicht gefunden"}
        k = dict(row)

    domain = k["domain"]
    website = k["website"] or f"https://{domain}"

    if verbose:
        print(f"  [{kanzlei_id:3d}] {domain:42s}", end=" ", flush=True)

    # Homepage lesen
    html, text = fetch_page(website)
    if not text or len(text) < 50:
        if verbose:
            print("SKIP (kein Inhalt)")
        return {"id": kanzlei_id, "domain": domain, "status": "no_content",
                "fibu": False, "recruiting": False, "digital": False, "verified_tier": "C"}

    all_text = text

    # Subpages suchen und lesen (Team, Karriere, Leistungen)
    subpages = _find_subpage_urls(html, domain)

    # Auch Leistungs-Seite suchen
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', html, re.IGNORECASE)
    for href in hrefs:
        href_lower = href.lower()
        if href.startswith("/") or domain in href:
            if any(p in href_lower for p in ["leistung", "service", "angebot", "beratung"]):
                if "leistung" not in subpages:
                    subpages["leistung"] = href

    for page_type in ["team", "career", "leistung"]:
        if page_type in subpages:
            url = _make_absolute(subpages[page_type], website)
            _, page_text = fetch_page(url)
            if page_text:
                all_text += " " + page_text
            time.sleep(0.2)

    # Prüfung
    fibu_result = _check_keywords(all_text, FIBU_KEYWORDS)
    recruiting_result = _check_keywords(all_text, RECRUITING_KEYWORDS)
    digital_result = _check_keywords(all_text, DIGITAL_KEYWORDS)

    fibu_present = fibu_result["present"]
    recruiting_present = recruiting_result["present"]
    digital_present = digital_result["present"]

    # Verified Tier bestimmen
    all_three = fibu_present and recruiting_present and digital_present
    two_of_three = sum([fibu_present, recruiting_present, digital_present]) >= 2

    if all_three:
        verified_tier = "A"
    elif two_of_three:
        verified_tier = "B"
    else:
        verified_tier = "C"

    # Scores aktualisieren
    fibu_score = 2 if fibu_result["count"] >= 3 else (1 if fibu_result["count"] >= 1 else 0)
    recruiting_score = 2 if recruiting_result["count"] >= 3 else (1 if recruiting_result["count"] >= 1 else 0)
    digital_score = 2 if digital_result["count"] >= 3 else (1 if digital_result["count"] >= 1 else 0)

    # Bestehenden Score laden und nur die 3 verifizierten Dimensionen aktualisieren
    with get_db() as conn:
        existing = conn.execute("SELECT * FROM scores WHERE kanzlei_id = ?", (kanzlei_id,)).fetchone()
        if existing:
            existing = dict(existing)
            conn.execute("""
                UPDATE scores SET
                    fibu_score = ?,
                    recruiting_score = ?,
                    digital_score = ?,
                    summary = ?,
                    scored_by = 'verified'
                WHERE kanzlei_id = ?
            """, (fibu_score, recruiting_score, digital_score,
                  f"Verified {verified_tier}: FiBu={'JA' if fibu_present else 'NEIN'}, "
                  f"Recruiting={'JA' if recruiting_present else 'NEIN'}, "
                  f"Digital={'JA' if digital_present else 'NEIN'}",
                  kanzlei_id))

        # Verified Tier in notes speichern
        conn.execute("""
            UPDATE kanzleien SET
                review_notes = ?,
                updated_at = datetime('now')
            WHERE id = ?
        """, (f"verified_tier={verified_tier} | "
              f"FiBu: {', '.join(fibu_result['found'][:4])} | "
              f"Recruiting: {', '.join(recruiting_result['found'][:4])} | "
              f"Digital: {', '.join(digital_result['found'][:4])}",
              kanzlei_id))

    if verbose:
        f = "+" if fibu_present else "-"
        r = "+" if recruiting_present else "-"
        d = "+" if digital_present else "-"
        print(f"FiBu:{f} Recruit:{r} Digital:{d} → Tier {verified_tier}")

    return {
        "id": kanzlei_id,
        "domain": domain,
        "status": "verified",
        "fibu": fibu_present,
        "fibu_keywords": fibu_result["found"][:5],
        "recruiting": recruiting_present,
        "recruiting_keywords": recruiting_result["found"][:5],
        "digital": digital_present,
        "digital_keywords": digital_result["found"][:5],
        "verified_tier": verified_tier,
    }


def batch_verify(verbose: bool = True) -> list[dict]:
    """Verifiziert alle nicht-KO Kanzleien mit Score >= 11."""
    with get_db() as conn:
        rows = conn.execute("""
            SELECT k.id, k.domain, s.total
            FROM kanzleien k
            JOIN scores s ON k.id = s.kanzlei_id
            WHERE s.ko_hit = 0 AND s.total >= 11 AND k.review_status != 'rejected'
            ORDER BY s.total DESC
        """).fetchall()

    candidates = [dict(r) for r in rows]
    if verbose:
        print(f"Verifikation: {len(candidates)} Kanzleien\n")

    results = []
    for c in candidates:
        result = verify_kanzlei(c["id"], verbose=verbose)
        results.append(result)
        time.sleep(0.3)

    # Zusammenfassung
    verified = [r for r in results if r.get("status") == "verified"]
    tier_a = [r for r in verified if r.get("verified_tier") == "A"]
    tier_b = [r for r in verified if r.get("verified_tier") == "B"]
    tier_c = [r for r in verified if r.get("verified_tier") == "C"]

    if verbose:
        print(f"\n{'='*60}")
        print(f"Verifiziert: {len(verified)}/{len(candidates)}")
        print(f"Verified Tier A (alle 3 klar): {len(tier_a)}")
        print(f"Verified Tier B (2 von 3):     {len(tier_b)}")
        print(f"Verified Tier C (< 2):         {len(tier_c)}")

        if tier_a:
            print(f"\n=== VERIFIED TIER A ===")
            for r in tier_a:
                print(f"  {r['domain']:42s} | FiBu: {', '.join(r['fibu_keywords'][:3])}")

    return results
