# Vision: Säule B — Mandanten-Agent

**Status:** Roadmap, Demand-Test läuft. Suche nach 3–5 Partnerkanzleien für die gemeinsame Entwicklung.
**Stand:** 06. Mai 2026 | Version 1.0
**Eigentümer:** Andreas Schwarzkopf
**Verbindlichkeit:** Master-Referenz für alle Content-Erzeugung zu Säule B (LinkedIn, Blog, Landingpages, Webinar, E-Mail). Diese Datei ist die Single Source of Truth.

---

## 1. Worum es geht

Flowbeaver hat heute eine produktive Säule (A) und eine Roadmap-Säule (B). Beide tragen denselben technologischen Kern (LLM + KI-OCR + deterministische Regeln) und enden im selben Ergebnis: ein DATEV-kompatibler Buchungsstapel.

| | **Säule A — Vorkontierung (heute, produktiv)** | **Säule B — Mandanten-Agent (Roadmap, in Entwicklung)** |
|---|---|---|
| **Wer arbeitet** | Kanzleimitarbeiter prüft den vorkontierten Stapel | Mandant liefert Belege, KI-Agent klärt mit ihm |
| **Eingangskanäle** | Belege aus DUO / Mandanten-Upload / E-Mail | WhatsApp / E-Mail / Drag-and-Drop / automatische Abholung aus Lieferantenportalen |
| **Was die KI tut** | Extraktion, Zuordnung, Vorkontierung | Vorgängige Klärung mit Mandant: fehlende Belege anfordern, unklare Geschäftsvorfälle nachfragen, schlechte Scans erneut anfordern, Problembelege als solche markieren |
| **Ergebnis** | Vorkontierter Buchungsstapel im DATEV-Workflow | Vollständiger, geklärter, vorkontierter Buchungsstapel — Kanzlei sieht nur noch eine sehr kleine Restmenge an echten Klärfällen |
| **Differenzierung** | LLM versteht Belege jeder Sprache | Mandant arbeitet mit Werkzeugen, die er ohnehin täglich nutzt — kein Portal-Lernen |

**Wesentliche These zu Säule B:** ~90 % der Belege laufen ohne menschliches Anfassen durch. Was übrig bleibt, sind die echten Sonderfälle, die Fachwissen brauchen. Die Kanzlei wird vom Belegabtipp- und Rückfrage-Dienstleister zum Buchhaltungs-Spezialisten zurückbefördert.

---

## 2. Warum jetzt: Pain → Problems → Prize

Die ICP-Schärfung folgt dem Daniel-Priestley-Prinzip: *Who has the most to gain from the hardest problem I can solve?* Antwort: wachstumsorientierte Kanzleien, die unter Kapazitäts- und Margendruck stehen.

| Pain (was sie spüren) | Problem (warum es passiert) | Prize (was Säule A+B liefert) |
|---|---|---|
| Wachstum stockt — wir können keine Mandate mehr annehmen | Belegarbeit + Mandantenrückfragen blockieren jede freie Stunde im Team | Mehr Mandate ohne mehr Personal |
| Marge schrumpft trotz mehr Umsatz | Personalkosten 43,8 % vom Umsatz (STAX 2024) — jeder neue Mitarbeiter frisst die Marge auf | Marge wächst mit Volumen, nicht mit Headcount |
| Mandanten "kommen einfach nicht mit" | Komplexe Mandantenportale (DUO als bekanntes Beispiel) sind eine zu hohe Hürde — viele Mandanten haben weder Zeit noch Lust, ein neues System zu lernen | Belege fließen automatisch — auch von Mandanten, die nur WhatsApp und E-Mail bedienen |
| 59,1 % offene Stellen unbesetzt (STAX 2024) | Selbst wer wachsen will, findet niemanden | Wachstum entkoppelt sich vom Stellenmarkt |

**Was die Vision NICHT ist:**
- Kein DATEV-Ersatz. Säule B fließt über DUO / Rechnungsdatenservice / Buchungsdatenservice in den DATEV-Workflow.
- Keine Mandanten-Self-Service-App im Sinne von Lexware oder sevdesk. Mandanten brauchen kein Konto, keine Schulung, kein Login.
- Kein Eigenbau für jede Schnittstelle. Lieferantenportal-Abholung wird über bestehende Spezial-Vendoren abgedeckt; Flowbeaver konzentriert sich auf den Klärungs-Agenten und die Konsolidierung.

---

## 3. Wie die Mandantenseite konkret funktioniert (für Vision-Content)

Diese Beschreibung ist die Grundlage für jede konkrete Szenario-Schilderung — LinkedIn-Post, Blog-Beispiel, Vision-LP-Walkthrough.

**Eingangskanäle (alle parallel nutzbar):**
1. **WhatsApp** — Mandant fotografiert Beleg, sendet kommentarlos an die Kanzlei-Nummer.
2. **E-Mail** — Mandant leitet Rechnung weiter (z. B. amazon-Rechnungs-PDF) oder sendet Foto.
3. **Drag-and-Drop** — Mandant zieht Datei in eine Mini-Web-Oberfläche. Keine Formulare, keine Pflichtfelder, keine Konfigurationsmenüs.
4. **Automatische Abholung** — eingebundener Spezial-Service holt Rechnungen aus typischen Lieferantenportalen (Telekom, Strom, Cloud-Tools etc.) ab.

**Was der Agent macht, sobald ein Beleg eintrifft:**
- LLM liest den Beleg, ordnet ihn dem Mandanten und dem Geschäftsvorfall zu.
- Wenn alles klar ist (etwa 90 % der Fälle): Beleg geht direkt in die Vorkontierung. Mandant bekommt nichts mehr zu sehen.
- Wenn etwas unklar ist: gezielte Rückfrage über denselben Kanal, in dem der Beleg kam — die Klärfall-Historie wird kanalübergreifend zu einem Vorgang zusammengeführt:
  - **WhatsApp-Beleg** → Rückfrage als WhatsApp-Nachricht, Mandant antwortet im selben Chat.
  - **E-Mail-Beleg** → Rückfrage als E-Mail mit Link in den Mandantenportal-Chat. Mandant klickt, beantwortet im Portal, Antwort fließt in dieselbe Klärfall-Historie.
  - **Drag-and-Drop-Beleg** → Klärfall öffnet sich direkt im selben Hochlade-Fenster.
  - **Lieferantenportal-Beleg** → Rückfrage geht an die in der Kanzlei hinterlegte Mandanten-Standardadresse (E-Mail oder WhatsApp, je nach Mandanten-Präferenz).

**Beispiele für Klärfälle, die der Agent direkt mit dem Mandanten klärt:**
- Bank- oder Kassenbuchung ohne dazugehörigen Beleg → "Zu Ihrer Kartenzahlung am 14. Mai über 87,40 € bei OBI haben wir noch keinen Beleg. Können Sie ihn fotografieren und antworten?"
- Beleg zu unscharf oder schief gescannt → "Der Beleg von gestern lässt sich nicht lesen. Bitte erneut fotografieren, möglichst gerade von oben."
- Geschäftsvorfall mehrdeutig → "Ist die OBI-Bestellung vom 14. Mai für Ihren eigenen Bürobedarf oder Lagerbestand für Weiterverkauf?"
- Beleg liegt formal falsch vor (Quittung statt Rechnung bei größeren Beträgen, falsche Adresse) → "Diese Quittung von Saturn über 1.450 € erfüllt nicht die Anforderungen für den Vorsteuerabzug. Bitte bei Saturn eine Rechnung auf Ihre Firmenadresse anfordern."

**Wenn alles geklärt ist:**
- Daten fließen über die DATEV-Schnittstellen (DUO / Rechnungsdatenservice / Buchungsdatenservice) in den Buchungsstapel.
- Kanzleimitarbeiter sieht im DATEV-Workflow den vorkontierten Stapel + sehr kleine Liste echter Restklärfälle, die Fachwissen brauchen (z. B. komplexe Splittbuchungen, Sonderfälle Vorsteuerabzug).

**Sprachgebrauch (für Content-Texte):**
- "KI-Agent" oder "Agent" — beides okay. Nicht "Bot", nicht "Chatbot".
- "Mandanten-Agent" als Produkt-Bezeichnung okay, sparsam einsetzen.
- "Kein Portal lernen" — als Schlagwort gut.
- "Werkzeuge, die der Mandant ohnehin nutzt" — präziser als "WhatsApp-Buchhaltung".
- Keine Übertreibung wie "vollautomatisch" — wir sagen "rund 90 % laufen automatisch durch".

---

## 4. Compliance: GoBD und DSGVO (verbindliche Argumentation)

Der Mandanten-Agent berührt zwei Compliance-Felder, die in jedem Kanzleigespräch innerhalb der ersten zehn Minuten kommen — GoBD und DSGVO (insbesondere WhatsApp). Beides ist architektonisch sauber lösbar; die Logik gehört zur verbindlichen Argumentation jedes Sales- und Marketing-Assets.

### 4.1 GoBD: Flowbeaver speichert keine Belege dauerhaft

Flowbeaver ist technisch ein **Sammel- und Transportkanal**, kein Belegarchiv. Belege kommen über die Eingangskanäle (WhatsApp, E-Mail, Drag-and-Drop, Lieferantenportal-Abholung) herein, werden vom KI-Agenten verarbeitet und vorkontiert und fließen in DATEV (oder eine andere vollumfängliche FiBu). Sobald der Beleg dort angekommen ist, hat Flowbeaver seine Aufgabe erfüllt. **Die GoBD-Aufbewahrungspflicht liegt — wie schon immer — bei der Kanzlei und ihrer Buchhaltungssoftware**, nicht bei einem zwischengeschalteten KI-System.

Konsequenzen für die Kommunikation:
- Flowbeaver speichert keine Belege im Sinne der GoBD-Aufbewahrungsfristen. Was wir technisch zur Verarbeitung kurzfristig zwischenspeichern, ist Verarbeitungsdaten, nicht Archivdaten.
- Unveränderbarkeit, Aufbewahrungszeitraum und Auffindbarkeit der Belege werden in DATEV (bzw. der jeweiligen FiBu) sichergestellt — also genau dort, wo sie heute schon liegen.
- Flowbeaver ist GoBD-relevant nur insofern, dass der Beleg vollständig, lesbar und unverändert an die FiBu weitergegeben wird — eine Transport-Anforderung, keine Archivierungs-Anforderung.

**Sprachregelung:** "Flowbeaver ist ein Sammel- und Transportkanal in Ihre FiBu. Die Aufbewahrung bleibt dort, wo sie hingehört — in Ihrem Buchhaltungssystem." NICHT formulieren: "GoBD-konform" oder "GoBD-zertifiziert" — diese Begriffe gehören einer Buchhaltungssoftware, nicht einem Vorsystem.

### 4.2 DSGVO und WhatsApp: Mandanten-Consent als Schlüssel

Der häufigste Einwand ist nicht GoBD, sondern WhatsApp. Die saubere Logik:

- **WhatsApp ist optional, kein Pflichtkanal.** Mandanten, die WhatsApp nicht nutzen wollen, nutzen einen anderen Kanal — E-Mail, Drag-and-Drop, Lieferantenportal-Abholung. Keine Funktion des Mandanten-Agenten setzt WhatsApp voraus.
- **Wenn ein Mandant WhatsApp nutzt, ist es seine Einwilligung.** Der Mandant entscheidet selbst, über welchen Kanal er Belege einreicht. Eine dokumentierte Einwilligung (Opt-in) zur Nutzung von WhatsApp deckt die DSGVO-Anforderung an die Datenverarbeitung ab.
- **Auftragsverarbeitungsvertrag liegt zwischen Kanzlei und Mandant.** Die Kanzlei schließt mit dem Mandanten den AVV ab, nicht Flowbeaver direkt mit dem Mandanten. Flowbeaver tritt gegenüber der Kanzlei als Auftragsverarbeiter auf — dieselbe Logik, die Kanzleien für DATEV, GetMyInvoices oder Microsoft 365 längst etabliert haben.
- **Alternative ohne WhatsApp ist gleichwertig.** Der Klärungs-Chat des KI-Agenten läuft auch über E-Mail mit Mandantenportal-Link: Agent schickt Frage per E-Mail, Mandant klickt auf den Link, beantwortet im Mandantenportal, Antwort fließt in dieselbe Klärfall-Historie wie die WhatsApp-Variante. Der Mehrwert (Klärfälle automatisiert) ist nicht an WhatsApp gebunden.

**Sprachregelung:** "WhatsApp ist ein Kanal von vielen. Welcher Kanal genutzt wird, entscheidet der Mandant — mit dokumentierter Einwilligung. Die Klärungs-Logik funktioniert auf jedem Kanal gleich." NICHT formulieren: "WhatsApp ist DSGVO-sicher" — Meta sitzt in den USA, eine technische Behauptung über WhatsApp selbst hält keiner Prüfung stand. Die DSGVO-Lösung ist Mandanten-Consent plus freie Kanalwahl, nicht eine Aussage über das Tool.

### 4.3 Sales-Argumentation in einem Absatz

Direkt verwendbar in Outbound-Mail, Webinar-FAQ, Sales-Gespräch:

> "Flowbeaver ist ein Sammel- und Transportkanal in Ihre Buchhaltungssoftware — DATEV oder eine andere vollumfängliche FiBu. Die GoBD-Aufbewahrung bleibt dort, wo sie hingehört, im Buchungssystem; Flowbeaver speichert keine Belege im Sinne der Aufbewahrungspflichten. Die Eingangskanäle — WhatsApp, E-Mail, Drag-and-Drop, automatische Abholung aus Lieferantenportalen — wählt der Mandant selbst. Wer WhatsApp nicht nutzen will, nutzt E-Mail mit Portal-Link; die Klärungs-Logik des KI-Agenten ist auf jedem Kanal identisch. Mandanten-Consent zur Kanalwahl wird einmal dokumentiert, der Auftragsverarbeitungsvertrag liegt wie üblich zwischen Kanzlei und Mandant."

---

## 5. Gründer-Positionierung: Unternehmer zu Unternehmer (Master-Version)

**Frame (verbindlich für alle Vision-B-Inhalte):**
Andreas spricht die Kanzleiinhaberschaft auf Augenhöhe an — als **Unternehmer zum
Unternehmer**, nicht als Tech-Anbieter zum Steuerberater. Eine Steuerkanzlei ist
in erster Linie ein Unternehmen mit Personal, Prozessen, Mandantenstruktur und
Wachstumsambition. Auf dieser Ebene findet das Gespräch statt — Wachstum, Marge,
Prozessoptimierung, Kapazität. Die fachliche Steuer-Tiefe gehört der Kanzlei,
nicht uns.

**Vier Schichten der Gründer-Position (in dieser Reihenfolge):**
1. **Unternehmer (primär)** — über 30 Jahre eigene unternehmerische Verantwortung. Spricht die Sprache jeder Kanzleiinhaberin, die wachsen will.
2. **Diplom-Kaufmann mit Buchhaltungsverständnis** — substantiell fundiert, nicht Insider. BWL, Bilanzierung, Buchführung sind Werkzeuge, nicht Geheimwissen.
3. **Mandant der eigenen Steuerkanzlei** — kennt die Belegarbeit aus eigener Erfahrung, hat sie gehasst, baut, was er sich gewünscht hätte.
4. **15 Jahre KI-Erfahrung (u.a. Mercedes-Benz)** — Werkzeug, mit dem die Lösung gebaut wird. Steht im Dienst des Problems, nicht im Brand-Frame.

**Was geschrieben werden darf — Kernfakten:**
- Diplom-Kaufmann mit Buchhaltungsverständnis.
- Über 30 Jahre selbst Unternehmer.
- Gleichzeitig Mandant einer Steuerkanzlei — kennt die Belegarbeit aus erster Hand.
- 15 Jahre KI-Erfahrung als Werkzeug, nicht als Identität.
- Nicht Steuerberater. Tarnt sich auch nicht als einer.

**Master-Formulierungen (können 1:1 verwendet werden):**

Lange Variante (About-Block, dezidierter LinkedIn-Post):
> "Ich bin seit über 30 Jahren Unternehmer. Ich kenne Wachstumsdruck, ich kenne Margenstress, ich kenne den Personalengpass — nicht aus Beratung, sondern aus eigener Verantwortung. Und ich bin gleichzeitig Mandant einer Steuerkanzlei, also auf der Seite, die jeden Monat den Beleg-Schuhkarton zusammensucht. Beides zusammen ist der Grund, warum es Flowbeaver gibt: Ich baue das Werkzeug, das ich mir als Mandant immer gewünscht hätte — und das gleichzeitig der Kanzlei genau die Last abnimmt, die heute Wachstum blockiert."

Kurze Variante (Vision-LP-Subheadline, Outbound):
> "Unternehmer baut für Unternehmer. Die fachliche Steuer-Tiefe holen wir uns von den Partnerkanzleien."

**Dosierung — wo die Origin-Story prominent erzählt wird:**
- About-Sektion auf der Website (1×, ausführlich, lange Variante)
- Vision-Landingpage (About-Block, mittlere Länge)
- Positionierung.md Section 1.2 (intern, Referenz)
- Ein dezidierter LinkedIn-Post im Launch-Sprint (mittel-prominent)

**Wo NICHT:**
- Nicht in jedem LinkedIn-Post wiederholen.
- Nicht im Homepage-Hero (dort: Funktion vor Person — was die Lösung tut, kommt zuerst).
- Nicht in Outbound-DMs.
- Nicht in der Webinar-Eröffnung (kommt höchstens kurz im Outlook-Block).

**Brand-Voice-Risiken (vermeiden):**
- "Tech-Founder" / "Techniker" als Hauptframe — die Tech ist Werkzeug, nicht Identität. Die KI-Erfahrung kommt als vierte Schicht, nicht als Headline.
- "Solo-Founder mit persönlichem Schmerz baut Hobby-Lösung" — Andreas ist substantiell fundiert (Unternehmer + Diplom-Kaufmann + KI). Mandanten-Erfahrung ist *zusätzliche* Glaubwürdigkeit, kein Ersatz für Fachlichkeit.
- "Wir kennen den Kanzleialltag" ohne Beleg — wir kennen Unternehmensalltag und Mandanten-Schmerz. Steuerfachliche Tiefe holen wir uns von den Partnerkanzleien.

---

## 6. Brand-Disziplin (verbindlich für jeden Asset)

| Regel | Konkret für Säule B |
|---|---|
| DATEV-Ergänzung, nicht Alternative | Säule B fließt über DUO / Rechnungsdatenservice / Buchungsdatenservice. Klar so kommunizieren. Webinar zeigt am Ende immer den DATEV-Buchungsstapel. |
| Compliance-Sprache präzise | "Sammel- und Transportkanal" / "FiBu führt die Aufbewahrung" / "Mandanten-Consent für Kanalwahl". NIE: "GoBD-zertifiziert", "GoBD-konformes Belegarchiv", "WhatsApp ist DSGVO-sicher". Volle Argumentation in Section 4. |
| DUO-Kritik moderat | DUO darf namentlich als Beispiel für "komplexes Mandantenportal" auftauchen — niemals als "DATEV ist zu kompliziert". DUO ist ein Modul von DATEV, kein Synonym für DATEV. Format: "Komplexe Mandantenportale wie DUO sind für Kanzleien wertvoll, aber nicht für jeden Mandanten zugänglich." |
| Whitelabel-Vendor (Lieferantenportal-Abholung) anonym | Funktion beschreiben — Vendor nicht namentlich nennen. Formulierung: "automatische Abholung aus Lieferantenportalen". |
| Vision als Roadmap framen | "Wir bauen", "Partnerkanzleien gesucht", "kommt", "in Entwicklung". Niemals als bereits verfügbare Funktion implizieren. Säule B steht NIE auf der gleichen Aktivitäts-Ebene wie Säule A. |
| Origin-Story dosieren | Master-Version siehe oben. Nur an den dort genannten 4 Stellen prominent. |
| Kein Startup-Jargon | "erste Runde", "Partnerkanzleien", "Vorhaben". Nicht: "Kohorte", "Pioneer-Kohorte", "Disruption", "Skalierung", "Onboarding", "Activation", "Funnel", "Game-Changer". |
| Andreas-Voice bewahren | Direkte Aussagen, Parallel-Konstruktionen, pointierte Meinungen nicht glätten. Memory `feedback_andreas_voice_not_jargon.md`. |
| Umlaute korrekt | ä/ö/ü/ß überall, nie ae/oe/ue. |
| Keine Emojis | Default keine Emojis in Posts oder Texten. |
| Sie-Anrede | Konsequent förmlich. |

---

## 7. Awareness-Stufen-Mapping

Inhalte, Hooks, Vokabular und CTA pro Awareness-Stufe — bindend für die Content-Erzeugung.

### Stufe 1 — Unaware ("Mein Wachstum läuft, alles okay")
- **Erkenntnis-Niveau**: Kanzleiinhaber spürt latenten Druck, hat aber noch nicht erkannt, dass Wachstum und Marge in entgegengesetzte Richtungen laufen.
- **Hook-Logik**: Daten konfrontieren, Reframe anbieten. Kein Pitch, keine Lösung.
- **Vokabular**: Personalkosten, Umsatzanteil, Wachstumsbremse, Margendruck, STAX 2024, Allensbach, Beschäftigtenstruktur.
- **Beispiel-Hooks**:
  - "43,8 % Personalkosten. Das ist der Branchendurchschnitt 2024. 2018 waren es 37 %. Was läuft hier?"
  - "Sie wachsen jedes Jahr — und Ihre Marge schrumpft jedes Jahr. Zufall ist das nicht."
- **Format**: LinkedIn-Edu, Blog Cornerstone, Branchenreport-Teaser.
- **CTA**: Keiner. Reine Aufmerksamkeit. Bestenfalls "weiterdenken in [Branchenreport]".

### Stufe 2 — Problem aware ("Personal ist das Problem")
- **Erkenntnis-Niveau**: Druck ist erkannt, Diagnose lautet "wir brauchen Personal". Es wird verzweifelt rekrutiert.
- **Hook-Logik**: Diagnose hinterfragen. Reframe: nicht Personal ist der Engpass, sondern die Belegarbeit + Mandantenkommunikation, die Personalkapazität verbraucht.
- **Vokabular**: Engpass, blockierte Stunden, Mandantenkommunikation, Pingpong, Klärschleifen, FiBu-Stunden, Stellenanzeigen.
- **Beispiel-Hooks**:
  - "Sie haben fünf Stellen ausgeschrieben, drei davon seit Monaten. Wenn Sie alle morgen besetzen könnten — würde es reichen?"
  - "5 Mandate abgelehnt im letzten Quartal. Nicht, weil die Mandate schlecht waren. Weil keine Hand frei war."
- **Format**: LinkedIn-Story, Blog-Reframe, E-Mail-Sequenz-Stufe.
- **CTA**: Branchenreport-Download.

### Stufe 3 — Solution aware ("Wir digitalisieren — DUO, andere Portale, OCR")
- **Erkenntnis-Niveau**: Kanzlei hat Digitalisierungsprojekte gestartet. Mandanten werden auf DUO umgestellt. Es funktioniert teilweise — bei einigen Mandanten hervorragend, bei vielen nicht.
- **Hook-Logik**: Reframe der Mauer. Mandanten scheitern nicht an Digitalisierungs-Wille, sondern an Portal-Komplexität. Das ist kein Schulungsproblem — es ist ein Werkzeug-Problem.
- **Vokabular**: Mandantenportal, Digitalisierungsmauer, Schulung, Akzeptanz, Werkzeuge des Alltags, Hürde, Lernkurve.
- **Beispiel-Hooks**:
  - "Sie schulen seit zwei Jahren Mandanten auf DUO. Wieviele nutzen es wirklich? Und wieviele schicken weiter Schuhkarton-Belege?"
  - "Komplexe Mandantenportale wie DUO sind für Kanzleien hervorragend. Für viele Mandanten sind sie eine Mauer."
- **Format**: Blog-Vergleichsartikel, Webinar-Block, LinkedIn-Reframe.
- **CTA**: Webinar-Anmeldung, Vision-LP.

### Stufe 4 — Product aware ("KI-Tools für Buchhaltung gibt es viele")
- **Erkenntnis-Niveau**: Kanzlei kennt das Marktangebot — Finmatics, Candis, BuchhaltungsButler, DATEV ASR. Sucht Differenzierung.
- **Hook-Logik**: Säule B als Differenzierungsmerkmal. Wir lösen beide Seiten — Mandant + Kanzlei. Mandanten arbeiten mit Werkzeugen, die sie ohnehin nutzen. Origin-Story (sparsam) als Glaubwürdigkeits-Anker.
- **Vokabular**: Mandanten-Agent, WhatsApp, Drag-and-Drop, Lieferantenportal-Abholung, Klärfälle automatisiert, Restklärfälle, vollständiger Buchungsstapel.
- **Beispiel-Hooks**:
  - "Stellen Sie sich vor, Ihr Mandant fotografiert einen Beleg per WhatsApp — und Sie sehen ihn vorkontiert in DATEV. Genau daran arbeiten wir."
  - "Das Mandantenportal, das kein Portal ist."
- **Format**: Vision-LP, Behind-the-Scenes-Post, Demo-Video, Cornerstone-Blog.
- **CTA**: Vision-LP-Sign-up, Partnerkanzlei-Bewerbung, Demo.

### Stufe 5 — Most aware ("Flowbeaver kenne ich, ich überlege")
- **Erkenntnis-Niveau**: Kanzlei kennt Flowbeaver bereits aus Content/Webinar. Sie wägt ab.
- **Hook-Logik**: Direct. 3–5 Partnerkanzleien für Säule-B-Entwicklung. Klare Voraussetzungen, klarer Ablauf.
- **Vokabular**: Partnerkanzlei, gemeinsame Entwicklung, Pilot, Voraussetzungen, Ablauf, Kommitment.
- **Beispiel-Hooks**:
  - "Wir suchen 3 bis 5 Partnerkanzleien für die Entwicklung des Mandanten-Agenten. Voraussetzungen: 4+ Mitarbeiter, Wachstumsdruck, DATEV. Ablauf in 6 Wochen."
- **Format**: Direct-LinkedIn-Post, DM-Outbound, Vision-LP-Bewerbungsformular.
- **CTA**: Bewerbung als Partnerkanzlei.

---

## 8. Validation-Loop und Decision-Gate

Säule B wird **nicht entwickelt**, bevor reale Demand-Signale aus dem Markt kommen. Der 3-Wochen-Launch-Sprint dient explizit als Demand-Test.

**KPIs während des Sprints (laufend tracken):**
- Conversions auf Vision-LP (Partnerkanzlei-Bewerbungsformular)
- LinkedIn-DM-Anfragen mit Bezug zur Vision
- Webinar-Q&A-Fragen zu Mandantenseite, WhatsApp-Belegerfassung, Klärungs-Agent
- E-Mail-Replies zu Vision-Posts in der Welcome-Sequenz
- Kommentar-Engagement auf den Vision-LinkedIn-Posts

**Decision-Gate Mitte Juni 2026 (Ende Woche 4 nach Sprint-Start):**

| Demand-Signal | Entscheidung |
|---|---|
| ≥ 3 Partnerkanzlei-Bewerbungen mit ICP-Fit | **Säule B priorisieren** — Entwicklung starten, Säule-A-Beta läuft parallel |
| 1–2 Bewerbungen | **Vision weiter teasern** — Content-Maschine läuft, keine Entwicklungs-Kapazität binden |
| 0 Bewerbungen | **Vision pausieren** — Origin-Story behalten, Säule A bleibt voller Fokus, neue Hypothese suchen |

---

## 9. Was sich gegenüber der bisherigen Strategie ändert (und was nicht)

**Bleibt unverändert:**
- DATEV-Ergänzungs-Position (`Positionierung.md` Section 6.1) — Säule B verstärkt sie sogar.
- Dual-Track Kanzlei + Unternehmen (`Positionierung.md` Section 6.4) — Säule B betrifft zunächst nur den Kanzlei-Track.
- LLM-versteht-jede-Sprache-Differenzierung (`Positionierung.md` Section 1.1) — wird zur technologischen Grundlage beider Säulen.
- Dreiklang LLM + KI-OCR + Regeln — bleibt der technologische Kern.
- LinkedIn 5-Pillar-Struktur — Säule B passt in Pillar 2 (KI-Expertise) als Sub-Theme. Keine sechste Pillar.
- Beta-Pricing 299 €/Monat — Säule B ist im Bewerbungsverfahren ein eigener Vertrags-Strang (Partnerkanzlei-Programm), nicht im normalen Beta-Pricing enthalten.

**Wird geschärft:**
- ICP-Definition: weg von "tech-affin", hin zu "wachstumsorientiert + Kapazitätsdruck + Margendruck". Tech-Affinität wird sekundär — der Mandanten-Agent macht die Bedienung sogar einfacher.
- Origin-Story: zweite Perspektive (Andreas als Mandant) wird Teil der Gründer-Positionierung.

**Wird neu eingeführt:**
- Zwei-Säulen-Architektur als Positionierungs-Kern.
- Pain-Problems-Prize-Framework als Awareness-Logik.
- Compliance-Argumentation (GoBD + DSGVO/WhatsApp) als verbindlicher Pflicht-Block für jedes Sales- und Marketing-Asset (Section 4).
- Vision-LP mit Partnerkanzlei-Bewerbungsformular.
- Roadmap-Sektion auf Homepage und Produkt-Seite.
- Webinar-Outlook-Block (5 Min am Ende).

---

## 10. Querverweise

- Strategische Einbettung: [Positionierung.md](Positionierung.md) Sections 1.2, 1.3, 6.5, 7.2, 7.3
- Roadmap-Section: [STRATEGY.md](STRATEGY.md) Abschnitt "Roadmap-Erweiterung Säule B"
- Sprint-Plan: [Aktionsplan.md](Aktionsplan.md) Section 12
- GTM-Anpassungen: [GTM-Strategie.md](GTM-Strategie.md) Executive Summary + Welcome-Mail
- Content-Skill: `~/.claude/skills/flowbeaver-marketing/` (LinkedIn, E-Mail, Landingpage, Webinar)
- Brand-Skill: `~/.claude/skills/flowbeaver-marketing/` und `flowbeaver-brand`
- STAX 2024 Daten: [CLAUDE.md](../CLAUDE.md) Branchendaten-Block
