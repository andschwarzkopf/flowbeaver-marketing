"""Konstanten, Signal-Definitionen, Regionen und KO-Kriterien für die Outbound Engine."""

import os
from pathlib import Path

DB_PATH = Path(__file__).parent / "data" / "outbound.db"
PROJECT_ROOT = Path(__file__).parent.parent.parent

# .env laden falls vorhanden
_env_file = PROJECT_ROOT / ".env"
if _env_file.exists():
    for line in _env_file.read_text().strip().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, val = line.partition("=")
            os.environ.setdefault(key.strip(), val.strip())

BRAVE_API_KEY = os.environ.get("BRAVE_API_KEY", "") or os.environ.get("BRAVE_SEARCH_API_KEY", "")
BRAVE_API_URL = "https://api.search.brave.com/res/v1/web/search"
BRAVE_RATE_LIMIT_SEC = 1.0  # 1 Request pro Sekunde (Free Tier)

REGIONS = {
    "muenchen_stuttgart": {
        "cities": ["München", "Stuttgart"],
        "label": "München/Stuttgart",
    },
    "berlin_brandenburg": {
        "cities": ["Berlin", "Potsdam"],
        "label": "Berlin/Brandenburg",
    },
    "nrw": {
        "cities": ["Köln", "Düsseldorf", "Dortmund", "Essen", "Bonn"],
        "label": "NRW",
    },
    "hamburg": {
        "cities": ["Hamburg"],
        "label": "Hamburg",
    },
    "rhein_main": {
        "cities": ["Frankfurt", "Wiesbaden", "Darmstadt", "Mainz"],
        "label": "Rhein-Main",
    },
}

# 10-Signal ICP-Scoring-Modell (je 0/1/2 Punkte, max 20)
SIGNAL_DEFINITIONS = {
    "size": {
        "label": "Kanzleigröße",
        0: "1–4 Mitarbeitende",
        1: "5–9 Mitarbeitende",
        2: "10+ Mitarbeitende",
    },
    "fibu": {
        "label": "FiBu-Relevanz",
        0: "Kaum sichtbar",
        1: "Vorhanden, nicht zentral",
        2: "Laufende Buchhaltung/FiBu = klarer Fokus",
    },
    "digital": {
        "label": "Digitalisierungs-Selbstbild",
        0: "Konservativ, minimale Tech-Sprache",
        1: "Generische Phrasen",
        2: "Konkrete digitale Prozesse, Portale, DUO, Automatisierung",
    },
    "datev": {
        "label": "DATEV-/Vorsystem-Fit",
        0: "DATEV nicht sichtbar",
        1: "DATEV erwähnt",
        2: "DATEV klar zentral, Vorsystem-Logik plausibel",
    },
    "growth": {
        "label": "Wachstumsorientierung",
        0: "Kein Wachstumssignal, Verwaltungsmodus",
        1: "Moderates Wachstum",
        2: "Aktives Wachstum, neue Mandate, neue Teams, Standorte",
    },
    "recruiting": {
        "label": "Recruiting-/Kapazitätsdruck",
        0: "Kein Signal",
        1: "Einzelne Stelle oder leichter Druck",
        2: "Mehrere Positionen, wiederholtes Hiring oder klarer Personalmangel",
    },
    "process": {
        "label": "Prozessreife",
        0: "Stark personenabhängig, wenig Struktur",
        1: "Erste Prozesssprache sichtbar",
        2: "Standardisierte Workflows, Teams, Portale, klare Prozesslogik",
    },
    "tools": {
        "label": "Offenheit für Zusatztools",
        0: "Nur Basisdarstellung",
        1: "Einzelne Hinweise auf Zusatztools",
        2: "DMS, Workflows, E-Rechnung, Mandantenportale, mehrere Systeme",
    },
    "decision_maker": {
        "label": "Entscheider auffindbar",
        0: "Kein direkter Zugang",
        1: "Teilweise identifizierbar",
        2: "Inhaber/Partner/Kanzleimanager klar sichtbar",
    },
    "trigger": {
        "label": "Trigger jetzt",
        0: "Kein aktueller Anlass",
        1: "Vages Signal",
        2: "Klarer Trigger: Hiring, Wachstum, Digitalisierungsinitiative, Prozessumbau",
    },
}

SIGNAL_KEYS = list(SIGNAL_DEFINITIONS.keys())

# Tier-Einteilung
TIER_BANDS = {
    "A": (16, 20),
    "B": (11, 15),
    "C": (0, 10),
}

# KO-Kriterien (überschreiben Score)
KO_CRITERIA = {
    "too_small": "Zu klein (Solo/Mini-Kanzlei)",
    "no_fibu": "Kein FiBu-Fokus",
    "no_datev": "Kein DATEV-Fit",
    "no_growth": "Kein Wachstumswille / Rentenmodus",
    "price_driven": "Rein preisgetrieben / offensichtlich träge",
}

# Such-Queries pro Stadt
TIER1_QUERY_TEMPLATES = [
    "Steuerkanzlei {city} digitalisierung",
    "Steuerberater {city} DATEV Unternehmen Online",
    "Steuerkanzlei {city} Team Karriere",
    "Steuerfachangestellte {city} Stellenangebot",
    "Steuerberater {city} FiBu Buchhaltung",
    "Steuerkanzlei {city} Mitarbeiter wachstum",
]

TIER2_QUERY_TEMPLATES = [
    "Steuerkanzlei {city} digitale Kanzlei",
    "Steuerberater {city} E-Rechnung DMS",
    "DATEV Kanzlei {city} modern",
]

# Review-Status-Werte
REVIEW_STATUSES = ("pending", "approved", "rejected", "needs_research")
