"""ICP-Scoring-Logik: 10-Signal-Modell mit KO-Kriterien."""

from .config import SIGNAL_DEFINITIONS, SIGNAL_KEYS, KO_CRITERIA, TIER_BANDS


def suggest_scores(kanzlei: dict, signals: list[dict]) -> dict:
    """Schlägt Scores basierend auf gesammelten Signalen vor.

    Args:
        kanzlei: Dict mit Kanzlei-Daten (aus DB)
        signals: Liste von Signal-Dicts (aus DB)

    Returns:
        Dict mit scores (dict), ko_hit (bool), ko_reason (str), summary (str),
        reasoning (dict pro Dimension)
    """
    scores = {}
    reasoning = {}

    # Signale nach Typ gruppieren
    signals_by_type = {}
    for s in signals:
        stype = s.get("signal_type", "")
        if stype not in signals_by_type:
            signals_by_type[stype] = []
        signals_by_type[stype].append(s)

    # Größe
    est_size = kanzlei.get("estimated_size") or 0
    if est_size >= 10:
        scores["size"] = 2
        reasoning["size"] = f"{est_size} Mitarbeitende geschätzt"
    elif est_size >= 5:
        scores["size"] = 1
        reasoning["size"] = f"{est_size} Mitarbeitende geschätzt"
    elif est_size > 0:
        scores["size"] = 0
        reasoning["size"] = f"Nur {est_size} Mitarbeitende"
    else:
        # Aus Signalen ableiten
        size_signals = signals_by_type.get("size", [])
        if size_signals:
            scores["size"] = 1  # Konservativ, da unklar
            reasoning["size"] = f"Größe aus Signal: {size_signals[0].get('observation', '')}"
        else:
            scores["size"] = 0
            reasoning["size"] = "Keine Größeninformation gefunden"

    # Für jede andere Dimension: Anzahl und Qualität der Signale bewerten
    for key in SIGNAL_KEYS:
        if key == "size":
            continue  # Schon behandelt
        if key in scores:
            continue

        dim_signals = signals_by_type.get(key, [])
        if not dim_signals:
            scores[key] = 0
            reasoning[key] = "Kein Signal gefunden"
        elif len(dim_signals) == 1:
            scores[key] = 1
            reasoning[key] = dim_signals[0].get("observation", "Ein Signal")
        else:
            scores[key] = 2
            reasoning[key] = f"{len(dim_signals)} Signale: " + "; ".join(
                s.get("observation", "")[:60] for s in dim_signals[:3]
            )

    # KO-Check
    ko_hit = False
    ko_reasons = []

    if scores.get("size", 0) == 0 and est_size > 0 and est_size < 4:
        ko_hit = True
        ko_reasons.append("too_small")

    if scores.get("fibu", 0) == 0 and not signals_by_type.get("fibu"):
        # Nur KO wenn gar kein FiBu-Signal
        if len(signals) > 3:  # Genug Daten, trotzdem kein FiBu
            ko_hit = True
            ko_reasons.append("no_fibu")

    if scores.get("datev", 0) == 0 and not signals_by_type.get("datev"):
        if len(signals) > 3:
            ko_hit = True
            ko_reasons.append("no_datev")

    ko_reason = ", ".join(ko_reasons) if ko_reasons else ""

    # Tier berechnen
    total = sum(scores.values())
    if total >= 16:
        tier = "A"
    elif total >= 11:
        tier = "B"
    else:
        tier = "C"

    # Summary
    top_signals = sorted(
        ((k, v) for k, v in scores.items() if v > 0),
        key=lambda x: x[1], reverse=True
    )[:3]
    summary_parts = [f"{SIGNAL_DEFINITIONS[k]['label']}={v}" for k, v in top_signals]
    summary = f"Tier {tier} ({total}/20): " + ", ".join(summary_parts) if summary_parts else f"Tier {tier} ({total}/20)"

    return {
        "scores": scores,
        "total": total,
        "tier": tier,
        "ko_hit": ko_hit,
        "ko_reason": ko_reason,
        "summary": summary,
        "reasoning": reasoning,
    }


def format_scorecard(kanzlei: dict, score: dict, signals: list[dict]) -> str:
    """Formatiert eine vollständige Scorecard als Markdown."""
    name = kanzlei.get("name", "Unbekannt")
    domain = kanzlei.get("domain", "")
    city = kanzlei.get("city", "")

    lines = [
        f"## Scorecard: {name}",
        f"**Domain:** {domain} | **Stadt:** {city} | **Region:** {kanzlei.get('region', '')}",
        "",
    ]

    # Score-Tabelle
    total = score.get("total", 0)
    tier = score.get("tier", "?")
    lines.append(f"### Score: {total}/20 — Tier {tier}")
    if score.get("ko_hit"):
        lines.append(f"**KO-Kriterium:** {score.get('ko_reason', '')}")
    lines.append("")
    lines.append("| Signal | Score | Begründung |")
    lines.append("|--------|-------|------------|")

    for key in SIGNAL_KEYS:
        label = SIGNAL_DEFINITIONS[key]["label"]
        val = score.get(f"{key}_score", score.get("scores", {}).get(key, 0))
        # Beschreibung aus Signal-Definition
        desc = SIGNAL_DEFINITIONS[key].get(val, "")
        lines.append(f"| {label} | {val}/2 | {desc} |")

    lines.append("")

    # Signale
    if signals:
        lines.append("### Gesammelte Signale")
        lines.append("")
        for s in signals:
            stype = SIGNAL_DEFINITIONS.get(s.get("signal_type", ""), {}).get("label", s.get("signal_type", ""))
            obs = s.get("observation", "")
            src = s.get("source_type", "")
            anchor = s.get("personalization_anchor", "")
            line = f"- **{stype}** ({src}): {obs}"
            if anchor:
                line += f" → *Anker: {anchor}*"
            lines.append(line)
        lines.append("")

    # Summary
    if score.get("summary"):
        lines.append(f"**Zusammenfassung:** {score['summary']}")

    return "\n".join(lines)
