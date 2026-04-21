# Session-Handoff: Website-Überarbeitung

Erstellt 2026-04-21. Bündelt die Erkenntnisse aus der Community-Recherche-Session als Input für die Überarbeitung von flowbeaver.de.

---

## Zu verweisende Dokumente in der nächsten Session

Der nächsten Session diese Dateien explizit nennen — dann hat sie den Kontext ohne erneute Recherche:

1. **[strategie/Fachcommunitys-Anknuepfungspunkte.md](Fachcommunitys-Anknuepfungspunkte.md)** — Community-Strategie, 16 konkrete DATEV-Thread-URLs, Priorisierung der Kanäle
2. **[linkedin/kommentar-leitfaden.md](../linkedin/kommentar-leitfaden.md)** — Tonalität, Kommentarstruktur, Dos/Don'ts für LinkedIn
3. **[CLAUDE.md](../CLAUDE.md)** — Projekt-Grundlagen, STAX-Daten, Kunden-Insights
4. **Memory-Einträge** (werden automatisch geladen): `project_positioning_techniker_not_steuerberater`, `reference_linkedin_hashtag_follow_removed`, `project_brand_unified`, `reference_stax2024`

---

## Kern-Erkenntnisse für Website-Copy

### 1. Positionierung

Andreas = **Techniker, der das Werkzeug baut** — nicht Branchen-Insider. Die Website muss diese Ehrlichkeit transportieren, statt so zu tun, als käme Flowbeaver aus einer Kanzlei. Solo-Founder-Status ist Vorteil (Direktzugang, schnelle Iteration), nicht Schwäche.

### 2. Tonalität

- Konservativ, ruhig, fachlich. Nicht clever, nicht provokant, nicht Startup-hip.
- Siezen. Keine Emojis. Keine Füllfloskeln.
- Spezifität statt Meinung: Zahlen, Belegtypen, Fehlermuster — nicht "KI revolutioniert".
- Eine Nuance pro Abschnitt. Nicht alle Argumente in jeden Absatz quetschen.

### 3. Kern-Differenzierer, neu geschärft

Der in der Community-Recherche bestätigte Wedge:

> **LLM versteht jede Sprache und leitet aus exotischen Rechnungen klare Geschäftsvorfälle ab → weniger Rückfragen beim Mandanten.**

Das unterscheidet Flowbeaver vom DATEV-Automatisierungsservice (Pattern-Matching auf deutschen Layouts). In der DATEV-Community sind **fremdsprachige Belege** und **Rückfragen-Last** zwei wiederkehrende Schmerzpunkte — beide schweigen bei den etablierten Anbietern laut.

### 4. Schmerzpunkte, die Kanzleien öffentlich beschreiben

Aus den analysierten DATEV-Threads (siehe Fachcommunitys-Doc) kristallisieren sich diese O-Töne heraus, die 1:1 auf der Website als Überschriften oder Hero-Zeilen funktionieren können:

- "Belegerkennung treibt mich in den Wahnsinn" (Thread 348355)
- "Belegerkennung funktioniert zu 99 % nicht" (Thread 445895)
- "Rückfragen kosten mehr Zeit als das Abtippen" (validierter Insight)
- "Die OCR merkt sich falsche Werte — und man kann sie nicht trainieren" (Thread 348355)
- "ZUGFeRD-XML wird als fehlerhaft abgelehnt, PDF muss weiter gelesen werden" (Thread 176385)
- "Englische Rechnungen: 'Invoice No.' wird als Barcode erkannt" (Thread 328159)

Das sind keine Marketing-Floskeln, sondern echte Community-Zitate. Sie wirken, weil sie aus dem Mund der Zielgruppe stammen.

### 5. Was die Website NICHT tun darf

- **Keine Anti-DATEV-Rhetorik.** Flowbeaver ist Ergänzung, nicht Alternative. Steht schon in CLAUDE.md, bleibt zentral.
- **Keine Überversprechen.** "100 % automatisch" ist tot. Besser: konkrete Trefferquoten pro Belegtyp.
- **Keine Startup-Sprache.** Pioneer, Disruption, Game-Changer — alles raus.
- **Keine Stock-Fotos mit lächelnden Geschäftsleuten.** Wirkt generisch. Lieber Screenshots der Lösung oder abstrakte Grafiken aus dem Brandbook.
- **Keine verkappten Dark Patterns** (falsche Counter, unnötige Pflichtfelder im Waitlist-Formular). Zielgruppe erkennt das und verliert Vertrauen.

### 6. Brand-Regeln

Seit 2026-04-20 gilt einheitliches Brandbook (Skill `flowbeaver-brand`): Lila #52267a, feste Typografie, einheitlich für Web + Print + Office + Bilder. Bei Website-Arbeiten das Brand-Skill aktiv triggern.

### 7. Conversion-Realität

GA4 zeigt aktuell unzuverlässige Conversions (Button-Clicks statt echte Formular-Submits, siehe Memory-Eintrag `project_test_conversions`). Bei Website-Überarbeitung zwingend das Tracking auf echte Formular-Events umstellen — sonst bleibt jede A/B-Aussage wertlos.

---

## Empfohlener Einstieg in die nächste Session

**Prompt-Vorlage:**

> Ich will die Website flowbeaver.de überarbeiten. Bitte lies zuerst `strategie/Session-Handoff-Website-Ueberarbeitung.md`, `strategie/Fachcommunitys-Anknuepfungspunkte.md` und die aktuelle `landingpages/landingpage-waitlist-v2.html`. Dann lass uns Stück für Stück durchgehen: Hero, Problem-Framing, Differenzierer, Social Proof, CTA. Nutze das Brandbook (Skill `flowbeaver-brand`).

Dadurch hat die Session sofort:
- Positionierung (Techniker)
- Tonalität (konservativ, spezifisch)
- Community-O-Töne als Copy-Rohmaterial
- Brand-Regeln

und kann direkt mit der Überarbeitung starten.

---

## Offene Fragen, die vor Website-Arbeit geklärt sein sollten

1. **Welche Trefferquoten-Zahlen** kannst du öffentlich nennen? (z. B. "90 % korrekte Vorkontierung bei deutschen Standardrechnungen nach drei Wochen Einlernphase")
2. **Welche Kanzleien** sind als anonyme Referenz ("eine Berliner Einzelkanzlei mit 6 MA") verwendbar?
3. **Waitlist vs. echtes Demo-Formular** — was ist das aktuelle Primärziel der Seite?
4. **Preis öffentlich oder nicht?** Aktuelle Website deutet an, aber nennt nicht. Entscheidung vor Relaunch fällen.
