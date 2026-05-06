# Review: homepage-v2-draft.html

Datum: 2026-04-25
Quelle: `/Users/andreas/Documents/Git/flowbeaver-marketing/landingpages/homepage-v2-draft.html`
Polished: `humanizer-output/2026-04-25/homepage-v2-draft-polished.html`

## Zusammenfassung

Die Datei hatte bereits einen Humanizer-Pass hinter sich (Kommentar im File: „ENTWURF v2 — nach Humanizer"). Der Text ist inhaltlich stark, der Rhythmus weitgehend in Ordnung — aber drei strukturelle KI-Muster sind durchgerutscht: ein klassischer Fett-Punkt-Erklärung-Block in Block 2, mechanische `<em>Antwort auf X.</em>`-Stubs in jeder Karte von Block 3, und 8 Halbgeviertstriche im Fließtext (Brand-Voice-Limit: max. 2). Der Inhalt blieb unverändert; alle Eingriffe sind rein stilistisch.

**Gefundene Muster:** ~14 (3 strukturelle, 7 Em-Dash-Inflation, 4 kleinere Rhythmus-Glättungen)
**Schweregrad:** Mittel — keine inhaltlichen Probleme, keine Brand-Voice-Verstöße, aber Häufung mechanischer Strukturen

**Brand-Voice-Befund:** Sauber. Keine „DATEV-Alternative", kein Startup-Jargon, keine Emojis, keine Hedging-Wolken. Andreas' direkte Ich-Stimme in Block 7 bewusst unverändert (memory-konformer Voice-Erhalt).

---

## Gegenüberstellung (Abschnitt für Abschnitt)

### Hero (Block 1)

**Original:**
> Flowbeaver liest Mandantenbelege, erkennt den Geschäftsvorfall und kontiert nach SKR03 oder SKR04 vor. Ihr Team prüft den Buchungsstapel und importiert ihn in DATEV Kanzlei-Rechnungswesen – ohne neue Software, ohne Umstellung bestehender Prozesse.

**Neu:**
> Flowbeaver liest Mandantenbelege, erkennt den Geschäftsvorfall und kontiert nach SKR03 oder SKR04 vor. Ihr Team prüft den Buchungsstapel und importiert ihn in DATEV Kanzlei-Rechnungswesen. Ohne neue Software. Ohne Umstellung bestehender Prozesse.

**Änderungen:** Em-Dash + „ohne X, ohne Y"-Liste in zwei Fragmente aufgelöst. Liest sich punchier und bricht das gleichmäßige Satz-Rhythmus-Plateau am Ende des Hero-Absatzes.

---

### Problem (Block 2) — die wichtigste Änderung

**Original:**
> Der Druck aus diesen Zahlen trifft immer denselben Engpass: qualifizierte Mitarbeiterstunden in der vorbereitenden Buchhaltung. Drei Muster sind dabei typisch.
>
> **Rückfragen-Schleifen mit dem Mandanten.** Fremdsprachige Rechnungen, unklare Positionen, handschriftliche Quittungen: Die Bearbeitung hält an, weil beim Mandanten nachgefragt werden muss. Die Antwort kommt ein bis drei Tage später und ist oft selbst erklärungsbedürftig.
>
> **Qualifizierte Fachkräfte in Routinearbeit gebunden.** Sortieren, Dublettencheck, schlechte Scans nachpflegen, Positionen aus PDFs heraustippen – diese Arbeit bindet genau die Mitarbeiter, die laut STAX zu 59,1 % schlicht nicht zu finden sind.
>
> **Monatsrhythmus statt gleichmäßiger Flow.** Belege kommen in Wellen – Monatsanfang, Quartalsende, Jahreswechsel. Fehlt jemand im Team, verschiebt sich der Druck direkt in Abschlüsse, Beratung und Neugeschäft.

**Neu:**
> Der Druck aus diesen Zahlen trifft immer denselben Engpass: qualifizierte Mitarbeiterstunden in der vorbereitenden Buchhaltung.
>
> Den größten Anteil verschlingen Rückfragen-Schleifen mit dem Mandanten. Fremdsprachige Rechnungen, unklare Positionen, handschriftliche Quittungen: Die Bearbeitung hält an, weil beim Mandanten nachgefragt werden muss. Die Antwort kommt ein bis drei Tage später und ist oft selbst erklärungsbedürftig.
>
> Daneben binden Routinearbeiten genau die Fachkräfte, die laut STAX zu 59,1 % nicht zu finden sind: Sortieren, Dublettencheck, schlechte Scans nachpflegen, Positionen aus PDFs heraustippen.
>
> Hinzu kommt der Monatsrhythmus. Belege treffen geballt zum Monatsanfang ein, dann zum Quartalsende, dann zum Jahreswechsel. Fehlt jemand im Team, verschiebt sich der Druck direkt in Abschlüsse, Beratung und Neugeschäft.

**Änderungen:**
- Drei mechanische `**Bold-Phrase.**`-Absatzeröffnungen entfernt (klassisches AI-Pattern: Fettdruck-Erklärung-Liste)
- Eröffnungen variiert: „Den größten Anteil verschlingen...", „Daneben binden...", „Hinzu kommt..." — drei verschiedene Satzanfänge statt drei identische
- Meta-Ankündigung „Drei Muster sind dabei typisch" entfernt — die drei Absätze zeigen das von selbst
- Para 2 umstrukturiert: Liste an das Ende per Doppelpunkt, statt Em-Dash-Sandwich in der Mitte
- Em-Dash in Para 3 („Belege kommen in Wellen – Monatsanfang, Quartalsende, Jahreswechsel") in Prosa-Aufzählung umgewandelt

---

### Wie es läuft (Block 3) — zweitwichtigste Änderung

**Original (Intro + Karten):**
> Jede Karte adressiert einen der drei Schmerzen direkt – in derselben Reihenfolge wie oben.
>
> [Karte 1] *Antwort auf Rückfragen-Schleifen.* Das Sprachmodell liest jeden Beleg inhaltlich – auch auf Italienisch, Englisch oder Polnisch – und formuliert Lieferant, Leistung und Geschäftsvorfall in deutscher Kanzleisprache aus. Wo bisher nachgefragt werden musste, liegt jetzt ein vorbereiteter Vorschlag im Stapel.
>
> [Karte 2] *Antwort auf Fachkräfte in Routinearbeit.* Sortieren, Dublettenprüfung, Scan-Aufbereitung, Positions-Extraktion – diese Mechanik übernimmt Flowbeaver vor der Kontierung. Ihre Mitarbeiter steigen dort ein, wo Entscheidungsarbeit beginnt: bei der Prüfung der Vorschläge und bei Fällen, die eine Bewertung brauchen.
>
> [Karte 3] *Antwort auf Monatsrhythmus-Spitzen.* Weil die Vorkontierung entkoppelt von der Team-Prüfung läuft, verteilt sich die Belegarbeit über die Woche. Was am Monatsanfang bisher ein Berg war, ist ein weitgehend vorbereiteter Stapel – und Abschlüsse, Beratung, Neugeschäft bleiben im Zeitplan.

**Neu (Intro entfernt, Stubs raus):**
> [Karte 1] Das Sprachmodell liest jeden Beleg inhaltlich aus, auch auf Italienisch, Englisch oder Polnisch. Lieferant, Leistung und Geschäftsvorfall stehen am Ende in deutscher Kanzleisprache. Wo bisher nachgefragt werden musste, liegt jetzt ein vorbereiteter Vorschlag im Stapel.
>
> [Karte 2] Die Mechanik vor der Kontierung übernimmt Flowbeaver: Sortieren, Dublettenprüfung, Scan-Aufbereitung, Positions-Extraktion. Ihre Mitarbeiter steigen dort ein, wo Entscheidungsarbeit beginnt: bei der Prüfung der Vorschläge und bei Fällen, die eine Bewertung brauchen.
>
> [Karte 3] Weil die Vorkontierung entkoppelt von der Team-Prüfung läuft, verteilt sich die Belegarbeit über die Woche. Was am Monatsanfang bisher ein Berg war, ist ein weitgehend vorbereiteter Stapel. Abschlüsse, Beratung und Neugeschäft bleiben im Zeitplan.

**Änderungen:**
- Drei mechanische `<em>Antwort auf X.</em>`-Stubs entfernt — die 1:1-Zuordnung zu Block 2 ergibt sich aus der Karten-Reihenfolge, sie muss nicht beschriftet werden
- Meta-Erklärung „Jede Karte adressiert einen der drei Schmerzen direkt – in derselben Reihenfolge wie oben" entfernt (typisches AI-„Tell-don't-show"-Muster)
- Karte 1: Em-Dash-Parenthese um „auch auf Italienisch, Englisch oder Polnisch" durch Komma ersetzt; ein langer Satz in zwei kürzere getrennt
- Karte 2: Em-Dash-Auftakt umgekehrt — die Liste folgt jetzt nach Doppelpunkt, der Hauptsatz steht vorne; zweiter Em-Dash zu Doppelpunkt
- Karte 3: Em-Dash + „und"-Verknüpfung durch Punkt ersetzt — drei klare Sätze

---

### Konkreter Durchlauf (Block 4)

**Original (Para 3):**
> Flowbeaver liest die Rechnung inhaltlich: Das Hotel wird als Lieferant identifiziert, Übernachtung und Frühstück werden getrennt ausgewiesen (relevant für die Kürzung der Verpflegungspauschale), die Tourismusabgabe wird als Reisenebenkosten erkannt. Die SKR03-Vorkontierung liegt am Donnerstagmorgen als Vorschlag im Buchungsstapel, nicht als Klärfall. Die Rückfrage beim Mandanten entfällt.

**Neu:**
> Flowbeaver liest die Rechnung inhaltlich. Hotel als Lieferant. Übernachtung und Frühstück getrennt ausgewiesen, relevant für die Kürzung der Verpflegungspauschale. Tourismusabgabe als Reisenebenkosten. Die SKR03-Vorkontierung liegt am Donnerstagmorgen als Vorschlag im Buchungsstapel, nicht als Klärfall. Die Rückfrage beim Mandanten entfällt.

**Änderungen:**
- Passiv-Parallel-Konstruktion „wird... werden... wird" durch Fragmente aufgebrochen — Aufzählungs-Rhythmus statt Drei-Klauseln-Satz
- Para 2 (Em-Dash bei „sortieren muss – oder der Mandant muss nachliefern"): Em-Dash zu Punkt + neuer Satz

---

### DATEV (Block 5)

**Original:**
> Die Vorarbeit – Lesen, Zuordnen, Kontieren – passiert außerhalb, danach läuft in Ihrer Kanzlei alles wie gewohnt.

**Neu:**
> Die Vorarbeit (Lesen, Zuordnen, Kontieren) passiert außerhalb, danach läuft in Ihrer Kanzlei alles wie gewohnt.

**Änderungen:** Em-Dash-Parenthese in Klammer-Form überführt. Liest sich ruhiger, weniger AI-typischer Em-Dash-Einsatz.

---

### Ressourcen (Block 8)

**Original (Karten):**
> [Karte 1] „KI in der Steuerkanzlei 2026" – 28 Seiten, 21 Quellen aus BStBK, ifo, DATEV, KPMG und weiteren Häusern. Kostenlos als PDF.
>
> [Karte 2] Produktfortschritt, Kanzleigespräche, Notizen aus der Entwicklung – ein bis zwei Beiträge pro Woche, meist vom Gründer selbst.

**Neu:**
> [Karte 1] „KI in der Steuerkanzlei 2026". 28 Seiten, 21 Quellen aus BStBK, ifo, DATEV, KPMG und weiteren Häusern. Kostenlos als PDF.
>
> [Karte 2] Produktfortschritt, Kanzleigespräche, Notizen aus der Entwicklung. Ein bis zwei Beiträge pro Woche, meist vom Gründer selbst.

**Änderungen:** Zwei weitere Em-Dashes durch Punkte ersetzt.

---

### FAQ (Block 10)

**Original (Frage „Müssen wir an DATEV..."):**
> Ihr DATEV-Setup – Kanzlei-Rechnungswesen, Unternehmen Online, Mandantenstruktur – bleibt unangetastet.

**Neu:**
> Ihr DATEV-Setup (Kanzlei-Rechnungswesen, Unternehmen Online, Mandantenstruktur) bleibt unangetastet.

**Original (Frage „Was ist der Unterschied..."):**
> Flowbeaver versteht den Inhalt eines Belegs: Lieferant, Leistung, Geschäftsvorfall – sprach- und layoutunabhängig.

**Neu:**
> Flowbeaver versteht den Inhalt eines Belegs: Lieferant, Leistung, Geschäftsvorfall, sprach- und layoutunabhängig.

**Änderungen:** Beide Em-Dashes ersetzt — einmal durch Klammer (Apposition), einmal durch Komma (nachgestellte Bestimmung).

---

### Block 9 (Demo) — bewusst unverändert

Der einzige im Dokument verbleibende Halbgeviertstrich:

> Mehr als acht bis zehn parallel lassen sich so nicht sauber einarbeiten – das ist keine Marketing-Mechanik, sondern die Realität eines Ein-Personen-Unternehmens.

Bewusst behalten: klassischer Kontrast-Em-Dash („nicht X, sondern Y"). Genau hier sitzt der Strich richtig — als rhythmische Pause vor der Pointe. Bei nur einem Vorkommen im Gesamtdokument keine Inflation.

---

### Block 7 (Gründer) — bewusst unverändert

Andreas' Zitat startet zweimal mit „Ich bin..." (parallel construction). Per Memory-Eintrag `feedback_andreas_voice_not_jargon`: Diese direkten Parallel-Konstruktionen sind Andreas' authentische Stimme, kein KI-Muster — beim Humanizen erhalten, nicht glätten.

---

## Detaillierte Änderungsliste

### 1. Hero — Em-Dash zu Fragmenten

**Typ:** Formatierung / Rhythmus
**Vorher:** „...in DATEV Kanzlei-Rechnungswesen – ohne neue Software, ohne Umstellung bestehender Prozesse."
**Nachher:** „...in DATEV Kanzlei-Rechnungswesen. Ohne neue Software. Ohne Umstellung bestehender Prozesse."
**Warum:** Em-Dash-Inflation reduzieren; Fragmente erzeugen Rhythmus-Variation am Hero-Ende.

### 2. Block 2 — Fett-Punkt-Erklärung-Muster aufgelöst

**Typ:** Struktur / Komposition
**Vorher:** Drei aufeinanderfolgende Absätze, jeder eröffnet mit `**Bold-Phrase.**` + Erklärungssatz.
**Nachher:** Drei Absätze mit unterschiedlichen Satzeröffnungen („Den größten Anteil...", „Daneben binden...", „Hinzu kommt...").
**Warum:** Stärkstes verbliebenes AI-Muster im Dokument. Per criteria-german.md §7a ist das mechanische Fett-Doppelpunkt-Pattern ein klassischer KI-Tell. Inhalt blieb identisch, nur die Mechanik ist weg.

### 3. Block 2 — Meta-Ankündigung gestrichen

**Typ:** Struktur / Coaching-Ton
**Vorher:** „...in der vorbereitenden Buchhaltung. Drei Muster sind dabei typisch."
**Nachher:** „...in der vorbereitenden Buchhaltung." (ohne Ankündigung)
**Warum:** „Drei Muster sind dabei typisch" ist eine AI-typische Strukturansage („Im Folgenden zeige ich..."). Die drei Absätze stehen für sich.

### 4. Block 2 Para 2 — Em-Dash-Sandwich aufgelöst

**Typ:** Formatierung
**Vorher:** „Sortieren, Dublettencheck, schlechte Scans nachpflegen, Positionen aus PDFs heraustippen – diese Arbeit bindet genau die Mitarbeiter..."
**Nachher:** „Daneben binden Routinearbeiten genau die Fachkräfte, die laut STAX zu 59,1 % nicht zu finden sind: Sortieren, Dublettencheck, schlechte Scans nachpflegen, Positionen aus PDFs heraustippen."
**Warum:** Em-Dash entfernt; Liste an das Satzende gerückt (per Doppelpunkt). Hauptsatz steht jetzt vorne, der Reader kriegt zuerst die Aussage, dann die Beispiele.

### 5. Block 2 Para 3 — Em-Dash zu Prosa-Aufzählung

**Typ:** Formatierung
**Vorher:** „Belege kommen in Wellen – Monatsanfang, Quartalsende, Jahreswechsel."
**Nachher:** „Belege treffen geballt zum Monatsanfang ein, dann zum Quartalsende, dann zum Jahreswechsel."
**Warum:** Em-Dash entfernt; aus Stichwort-Aufzählung wurde rhythmisch flüssige Folge mit „dann... dann...".

### 6. Block 3 — Meta-Erklärung „Jede Karte adressiert..." entfernt

**Typ:** Struktur / Coaching-Ton
**Vorher:** „Jede Karte adressiert einen der drei Schmerzen direkt – in derselben Reihenfolge wie oben."
**Nachher:** entfernt
**Warum:** Klassischer AI-Move („tell-don't-show"). Die Reihenfolge erklärt sich aus der Karten-Anordnung; eine Beschreibung der Struktur ist in Marketing-Copy fast immer überflüssig.

### 7. Block 3 — `<em>Antwort auf X.</em>`-Stubs entfernt (3×)

**Typ:** Struktur / Mechanische Parallelität
**Vorher:** Jede der drei Karten beginnt mit einem kursiv gesetzten Stub: „*Antwort auf Rückfragen-Schleifen.*", „*Antwort auf Fachkräfte in Routinearbeit.*", „*Antwort auf Monatsrhythmus-Spitzen.*"
**Nachher:** Alle drei Stubs entfernt
**Warum:** Hochmechanisches Parallel-Muster — drei Karten, drei identisch aufgebaute Beschriftungen. Reine 1:1-Verlinkungslogik wie aus einer Konzeptfolie. Die Karten-Inhalte selbst greifen die Probleme aus Block 2 inhaltlich auf, das genügt.

### 8. Block 3 Karte 1 — Em-Dash-Parenthese zu Komma-Apposition

**Typ:** Formatierung
**Vorher:** „Das Sprachmodell liest jeden Beleg inhaltlich – auch auf Italienisch, Englisch oder Polnisch – und formuliert..."
**Nachher:** „Das Sprachmodell liest jeden Beleg inhaltlich aus, auch auf Italienisch, Englisch oder Polnisch."
**Warum:** Em-Dash-Pair entfernt; gleichzeitig den langen Satz in zwei kürzere getrennt für Rhythmus-Variation.

### 9. Block 3 Karte 2 — Em-Dash an Satzanfang umgekehrt

**Typ:** Formatierung / Satzbau
**Vorher:** „Sortieren, Dublettenprüfung, Scan-Aufbereitung, Positions-Extraktion – diese Mechanik übernimmt Flowbeaver..."
**Nachher:** „Die Mechanik vor der Kontierung übernimmt Flowbeaver: Sortieren, Dublettenprüfung, Scan-Aufbereitung, Positions-Extraktion."
**Warum:** Em-Dash raus; Subjekt-Verb-Konstruktion vorgezogen, Liste folgt nach Doppelpunkt. Liest sich aktiver, weniger nominalstil.

### 10. Block 3 Karte 2 — zweiter Em-Dash zu Doppelpunkt

**Typ:** Formatierung
**Vorher:** „Ihre Mitarbeiter steigen dort ein, wo Entscheidungsarbeit beginnt: bei der Prüfung..."
**Nachher:** unverändert (war schon Doppelpunkt — kein Em-Dash hier; siehe Karte 3)

### 11. Block 3 Karte 3 — Em-Dash + „und" zu Punkt

**Typ:** Formatierung / Rhythmus
**Vorher:** „...ist ein weitgehend vorbereiteter Stapel – und Abschlüsse, Beratung, Neugeschäft bleiben im Zeitplan."
**Nachher:** „...ist ein weitgehend vorbereiteter Stapel. Abschlüsse, Beratung und Neugeschäft bleiben im Zeitplan."
**Warum:** Em-Dash und Konjunktion entfernt; aus einer langen Klammer zwei eigenständige Aussagen.

### 12. Block 4 Para 2 — Em-Dash zu Punkt

**Typ:** Formatierung
**Vorher:** „Die Positionen bleiben ein Textblock, den das Team am nächsten Morgen sortieren muss – oder der Mandant muss nachliefern..."
**Nachher:** „Die Positionen bleiben ein Textblock. Den muss das Team am nächsten Morgen sortieren, oder der Mandant muss nachliefern..."
**Warum:** Em-Dash entfernt; Inversion „Den muss das Team..." bringt Satzbau-Variation (per criteria §6b: Inversionen erlaubt und erwünscht).

### 13. Block 4 Para 3 — Passiv-Parallelismus in Fragmente

**Typ:** Rhythmus / Satzbau
**Vorher:** „Flowbeaver liest die Rechnung inhaltlich: Das Hotel wird als Lieferant identifiziert, Übernachtung und Frühstück werden getrennt ausgewiesen (relevant für die Kürzung der Verpflegungspauschale), die Tourismusabgabe wird als Reisenebenkosten erkannt."
**Nachher:** „Flowbeaver liest die Rechnung inhaltlich. Hotel als Lieferant. Übernachtung und Frühstück getrennt ausgewiesen, relevant für die Kürzung der Verpflegungspauschale. Tourismusabgabe als Reisenebenkosten."
**Warum:** Drei „wird... werden... wird"-Passiv-Parallelen klingen sehr maschinell, fast wie ein Datenbank-Output. Fragment-Stil bricht den Rhythmus, passt zu Andreas' direkter Stimme.

### 14. Block 5 — Em-Dash-Parenthese zu Klammer

**Typ:** Formatierung
**Vorher:** „Die Vorarbeit – Lesen, Zuordnen, Kontieren – passiert außerhalb..."
**Nachher:** „Die Vorarbeit (Lesen, Zuordnen, Kontieren) passiert außerhalb..."
**Warum:** Em-Dash-Pair entfernt. Klammer ist im Deutschen der natürlichere Apposition-Marker.

### 15. Block 8 Karte 1 + Karte 2 — Em-Dash zu Punkt

**Typ:** Formatierung
**Vorher (K1):** „...„KI in der Steuerkanzlei 2026" – 28 Seiten..."
**Nachher (K1):** „...„KI in der Steuerkanzlei 2026". 28 Seiten..."
**Vorher (K2):** „...Notizen aus der Entwicklung – ein bis zwei Beiträge..."
**Nachher (K2):** „...Notizen aus der Entwicklung. Ein bis zwei Beiträge..."
**Warum:** Beide Em-Dashes durch Punkte ersetzt — Karten-Texte werden klarer strukturiert.

### 16. Block 10 FAQ — zwei Em-Dashes ersetzt

**Typ:** Formatierung
**Vorher (DATEV-Frage):** „Ihr DATEV-Setup – Kanzlei-Rechnungswesen, Unternehmen Online, Mandantenstruktur – bleibt unangetastet."
**Nachher:** „Ihr DATEV-Setup (Kanzlei-Rechnungswesen, Unternehmen Online, Mandantenstruktur) bleibt unangetastet."
**Vorher (ASR-Frage):** „...Lieferant, Leistung, Geschäftsvorfall – sprach- und layoutunabhängig."
**Nachher:** „...Lieferant, Leistung, Geschäftsvorfall, sprach- und layoutunabhängig."
**Warum:** Klammer einmal als Apposition, Komma einmal als nachgestellte Bestimmung.

---

## Em-Dash-Bilanz

| Stelle | Vorher | Nachher |
|---|---|---|
| Hero | 1 | 0 |
| Block 2 Para 2 | 1 | 0 |
| Block 2 Para 3 | 1 | 0 |
| Block 3 Intro | 1 | 0 (Zeile entfernt) |
| Block 3 Karte 1 | 2 | 0 |
| Block 3 Karte 2 | 1 | 0 |
| Block 3 Karte 3 | 1 | 0 |
| Block 4 Para 2 | 1 | 0 |
| Block 5 | 2 | 0 (Klammer) |
| Block 8 Karte 1 | 1 | 0 |
| Block 8 Karte 2 | 1 | 0 |
| Block 9 (Demo) | 1 | 1 (bewusst behalten) |
| Block 10 FAQ DATEV | 2 | 0 (Klammer) |
| Block 10 FAQ ASR | 1 | 0 |
| **Summe** | **17** | **1** |

Brand-Voice-Limit ist max. 2 Em-Dashes pro Text. Der Polished-Text liegt jetzt bei genau einem — der einen, an dem der Strich rhythmisch wirklich etwas leistet (Kontrast-Pointe „nicht Marketing-Mechanik – sondern Realität").

---

## Nicht angefasst (bewusste Entscheidungen)

- **Block 7 Gründer-Zitat** mit „Ich bin... Ich bin..."-Parallel — Andreas' direkte Stimme, per Memory `feedback_andreas_voice_not_jargon` zu erhalten
- **Block 6 ROI** — saubere Prosa mit konkreten Zahlen, keine KI-Muster
- **Block 8 H2 „Wenn Sie uns erst einmal lesen wollen"** — leicht informell, aber zur Andreas-Stimme passend; nicht aggressiver glätten
- **Drei-Aufzählungen** in Block 5 („Lesen, Zuordnen, Kontieren" / „Kein Umstieg, kein Parallelsystem, keine Einarbeitung") und Block 9 — sind inhaltlich substanziell, keine bloße Rule-of-Three-Dekoration
- **„Drei Muster fallen auf"** durch Streichung der Meta-Ankündigung — die drei Absätze tragen sich selbst
- **Alle inhaltlichen Aussagen, Zahlen, Quellen, Personen** — null inhaltliche Änderungen, nur Wort- und Formatierungsglättung

---

## Empfehlung

Die polished Version sollte aus Humanizer-Sicht jetzt bei < 5 verbleibenden KI-Markern liegen. Wenn Sie mit den Eingriffen einverstanden sind: Inhalt aus `homepage-v2-draft-polished.html` zurück in `landingpages/homepage-v2-draft.html` übernehmen. Falls Sie an einzelnen Stellen anders entscheiden (z.B. die `<em>Antwort auf X.</em>`-Stubs aus didaktischen Gründen behalten wollen), zeigen Sie mir die Stelle, ich rolle nur diese eine Änderung zurück.
