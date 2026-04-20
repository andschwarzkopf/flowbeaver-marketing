"""Website-Analyse-Helfer: Keyword-Listen und Parse-Funktionen.

Playwright MCP macht das eigentliche Laden der Seiten.
Dieses Modul analysiert den extrahierten Text.
"""

import re
from collections import Counter

# Signal-Keywords pro Dimension (Deutsch)
SIGNAL_KEYWORDS = {
    "digital": [
        "digitalisierung", "digital", "duo", "unternehmen online",
        "e-rechnung", "dms", "dokumentenmanagement", "cloud", "papierlos",
        "automatisierung", "digitale kanzlei", "digitale prozesse",
        "mandantenportal", "belegupload", "scan", "ocr",
    ],
    "datev": [
        "datev", "datevconnect", "buchungsassistent", "duo",
        "unternehmen online", "datev smarttransfer", "dms classic",
        "datev arbeitnehmer online", "datev meine steuern",
        "datev-ökosystem", "datev-partner",
    ],
    "fibu": [
        "finanzbuchhaltung", "fibu", "buchhaltung", "buchführung",
        "belegbearbeitung", "vorkontierung", "buchungsstapel",
        "laufende buchhaltung", "monatliche buchhaltung",
        "belegmanagement", "rechnungswesen", "anlagenbuchhaltung",
    ],
    "recruiting": [
        "stellenangebot", "karriere", "verstärkung", "suchen",
        "team wächst", "bewerbung", "jobs", "offene stellen",
        "mitarbeiter gesucht", "fachkräfte", "nachwuchs",
        "steuerfachangestellte gesucht", "bilanzbuchhalter gesucht",
    ],
    "growth": [
        "wachstum", "expansion", "neuer standort", "neue mandate",
        "wir wachsen", "team vergrößern", "zweigstelle",
        "partnerschaftsgesellschaft", "zusammenschluss", "übernahme",
    ],
    "process": [
        "workflow", "prozess", "standardisiert", "qualitätsmanagement",
        "iso", "handbuch", "checkliste", "ablauf", "struktur",
        "teamleitung", "abteilung", "spezialisierung",
    ],
    "tools": [
        "addison", "agenda", "lexware", "sevdesk", "fastbill",
        "candis", "getmyinvoices", "spendesk", "dms",
        "mandantenportal", "eigenorganisation", "kanzleisoftware",
        "zusatzsoftware", "schnittstelle", "integration",
    ],
    "decision_maker": [
        "inhaber", "partner", "geschäftsführer", "kanzleimanager",
        "kanzleileitung", "steuerberater", "wirtschaftsprüfer",
        "managing partner", "senior partner",
    ],
    "trigger": [
        "neu gegründet", "umzug", "fusion", "digitalisierungsinitiative",
        "prozessoptimierung", "restrukturierung", "generationswechsel",
        "nachfolge", "kanzleiübergabe",
    ],
}


def _count_keyword_matches(text: str, keywords: list[str]) -> list[str]:
    """Gibt gefundene Keywords zurück."""
    text_lower = text.lower()
    return [kw for kw in keywords if kw.lower() in text_lower]


def parse_homepage(text: str) -> dict:
    """Analysiert Homepage-Text auf Signale.

    Returns:
        Dict mit gefundenen Signalen pro Dimension.
    """
    results = {}
    for dimension, keywords in SIGNAL_KEYWORDS.items():
        matches = _count_keyword_matches(text, keywords)
        if matches:
            results[dimension] = {
                "matches": matches,
                "count": len(matches),
                "examples": matches[:3],
            }
    return results


def parse_team_page(text: str) -> dict:
    """Analysiert Team-Seite: Headcount-Schätzung und Rollen.

    Returns:
        Dict mit estimated_size, roles, signals.
    """
    text_lower = text.lower()

    # Headcount-Schätzung über Rollenbezeichnungen
    role_patterns = [
        r"steuerberater(?:in)?",
        r"steuerfachangestellte[r]?",
        r"bilanzbuchhalter(?:in)?",
        r"wirtschaftsprüfer(?:in)?",
        r"rechtsanwalt|rechtsanwältin",
        r"lohnbuchhalter(?:in)?",
        r"finanzbuchhalter(?:in)?",
        r"auszubildende[r]?",
        r"sekretariat|empfang|assistenz",
        r"kanzleimanager(?:in)?",
        r"partner(?:in)?",
    ]

    roles_found = []
    total_count = 0
    for pattern in role_patterns:
        found = re.findall(pattern, text_lower)
        if found:
            roles_found.extend(found)
            total_count += len(found)

    # Alternative: Zähle "Unser Team" oder explizite Zahlen
    size_matches = re.findall(r"(\d+)\s*(?:mitarbeiter|beschäftigte|köpfe|kollegen)", text_lower)
    estimated_from_text = max((int(n) for n in size_matches), default=0) if size_matches else 0

    estimated_size = max(total_count, estimated_from_text)

    # Signal-Keywords
    signals = {}
    for dim in ["decision_maker", "growth", "digital"]:
        matches = _count_keyword_matches(text, SIGNAL_KEYWORDS[dim])
        if matches:
            signals[dim] = matches

    return {
        "estimated_size": estimated_size,
        "role_count": total_count,
        "roles": list(set(roles_found)),
        "signals": signals,
    }


def parse_career_page(text: str) -> dict:
    """Analysiert Karriere-/Jobs-Seite.

    Returns:
        Dict mit offenen Stellen, Keywords, Recruiting-Signalen.
    """
    text_lower = text.lower()

    # Job-Titel finden
    job_patterns = [
        r"steuerfachangestellte[r]?\s*\(m/w/d\)?",
        r"bilanzbuchhalter(?:in)?\s*\(m/w/d\)?",
        r"steuerberater(?:in)?\s*\(m/w/d\)?",
        r"finanzbuchhalter(?:in)?\s*\(m/w/d\)?",
        r"lohnbuchhalter(?:in)?\s*\(m/w/d\)?",
        r"buchhalter(?:in)?\s*\(m/w/d\)?",
        r"wirtschaftsprüfer(?:in)?\s*\(m/w/d\)?",
    ]

    jobs_found = []
    for pattern in job_patterns:
        found = re.findall(pattern, text_lower)
        jobs_found.extend(found)

    # Recruiting-Keywords
    recruiting_matches = _count_keyword_matches(text, SIGNAL_KEYWORDS["recruiting"])

    # DATEV/FiBu-Bezug in Stellenanzeigen
    datev_in_jobs = _count_keyword_matches(text, SIGNAL_KEYWORDS["datev"])
    fibu_in_jobs = _count_keyword_matches(text, SIGNAL_KEYWORDS["fibu"])

    return {
        "jobs_found": list(set(jobs_found)),
        "job_count": len(set(jobs_found)),
        "recruiting_signals": recruiting_matches,
        "datev_mentioned": bool(datev_in_jobs),
        "fibu_mentioned": bool(fibu_in_jobs),
        "has_career_page": True,
    }


def get_scrape_checklist(kanzlei: dict) -> str:
    """Gibt strukturierte Anleitung für Claude/Playwright zurück."""
    website = kanzlei.get("website", "")
    domain = kanzlei.get("domain", "")

    return f"""## Scrape-Checklist für {kanzlei.get('name', domain)}

### 1. Homepage ({website})
Suche nach:
- Kanzleigröße (Mitarbeiter, Standorte)
- FiBu/Buchhaltung als Leistung
- Digitalisierungs-Sprache
- DATEV / DUO / Portale / E-Rechnung / DMS
- Wachstumssignale

### 2. Team-/Über-uns-Seite
Suche nach:
- Anzahl Mitarbeitende (zähle Rollen)
- Inhaber/Partner-Namen
- Spezialisierungen
- Abteilungsstruktur

### 3. Karriere-/Jobs-Seite
Suche nach:
- Offene Stellen (besonders FiBu, Steuerfach, DATEV)
- Recruiting-Intensität
- DATEV-/Digital-Keywords in Stellenanzeigen
- Moderne-Arbeit-Signale

### 4. LinkedIn (falls bekannt)
Suche nach:
- Unternehmensseite aktiv?
- Posts zu Recruiting, Wachstum, Digitalisierung?
- Inhaber/Partner identifizierbar?

**Ergebnis notieren:** Score-Vorschlag + 1 klares Signal + 1 Personalisierungsanker
"""


def analyze_text(text: str) -> dict:
    """Komplettanalyse eines beliebigen Textes über alle Dimensionen.

    Returns:
        Dict mit allen gefundenen Signalen, aggregiert.
    """
    all_signals = {}
    for dimension, keywords in SIGNAL_KEYWORDS.items():
        matches = _count_keyword_matches(text, keywords)
        if matches:
            all_signals[dimension] = {
                "matches": matches,
                "count": len(matches),
                "unique": list(set(matches)),
            }
    return all_signals
