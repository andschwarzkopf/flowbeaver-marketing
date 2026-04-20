"""Export-Funktionen: CSV und Markdown für Kanzlei-Daten."""

import csv
import io
from pathlib import Path

from .config import SIGNAL_DEFINITIONS, SIGNAL_KEYS
from .db import get_approved_icps, get_signals, search_kanzleien


def export_csv(kanzleien: list[dict], filepath: str) -> str:
    """Exportiert Kanzleien als CSV (Playbook Tab-Struktur).

    Args:
        kanzleien: Liste von Kanzlei-Dicts (mit Score-Feldern)
        filepath: Zielpfad für CSV

    Returns:
        Pfad der geschriebenen Datei.
    """
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "id", "name", "domain", "website", "city", "region",
        "estimated_size", "total", "tier",
        "size_score", "fibu_score", "digital_score", "datev_score",
        "growth_score", "recruiting_score", "process_score", "tools_score",
        "decision_maker_score", "trigger_score",
        "review_status", "summary",
        "contact_1_name", "contact_1_role", "contact_1_linkedin",
        "linkedin_company",
    ]

    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore", delimiter=";")
        writer.writeheader()
        for k in kanzleien:
            writer.writerow(k)

    return str(path)


def export_markdown(kanzleien: list[dict]) -> str:
    """Gibt Kanzleien als Markdown-Tabelle zurück."""
    if not kanzleien:
        return "Keine Kanzleien zum Exportieren."

    lines = [
        "| # | Name | Stadt | Region | Größe | Score | Tier | Status |",
        "|---|------|-------|--------|-------|-------|------|--------|",
    ]
    for i, k in enumerate(kanzleien, 1):
        name = k.get("name", "?")[:40]
        city = k.get("city", "")
        region = k.get("region", "")
        size = k.get("estimated_size", "?")
        total = k.get("total", "?")
        tier = k.get("tier", "?")
        status = k.get("review_status", "?")
        lines.append(f"| {i} | {name} | {city} | {region} | {size} | {total}/20 | {tier} | {status} |")

    return "\n".join(lines)


def export_approved_csv(filepath: str) -> str:
    """Exportiert nur approved ICPs als CSV."""
    kanzleien = get_approved_icps()
    if not kanzleien:
        return "Keine approved Kanzleien vorhanden."
    return export_csv(kanzleien, filepath)


def export_review_batch(kanzleien: list[dict]) -> str:
    """Formatiert einen Review-Batch als Markdown für Human-in-the-Loop."""
    if not kanzleien:
        return "Keine Kanzleien zum Reviewen."

    lines = ["# Review-Batch\n"]

    for i, k in enumerate(kanzleien, 1):
        kid = k.get("id", "?")
        name = k.get("name", "Unbekannt")
        domain = k.get("domain", "")
        city = k.get("city", "")
        total = k.get("total", "?")
        tier = k.get("tier", "?")

        lines.append(f"## {i}. {name} (ID: {kid})")
        lines.append(f"- **Domain:** {domain}")
        lines.append(f"- **Stadt:** {city} | **Region:** {k.get('region', '')}")
        lines.append(f"- **Score:** {total}/20 — Tier {tier}")

        if k.get("estimated_size"):
            lines.append(f"- **Geschätzte Größe:** {k['estimated_size']} MA")

        summary = k.get("summary", "")
        if summary:
            lines.append(f"- **Summary:** {summary}")

        lines.append(f"- **Website:** {k.get('website', '')}")
        lines.append("")
        lines.append("**Bewertung:** approve / reject / needs_research")
        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)
