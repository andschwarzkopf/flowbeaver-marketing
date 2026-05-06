# Homepage — Anforderungen

Stand: 2026-04-22.
Zweck dieses Dokuments: In einer frischen Session die Homepage sauber aufbauen, ohne die Verhedderungen der bisherigen Iterationen.

---

## 1. Rolle der Homepage

- **Trust-Hub**, nicht SEO-Eintrittsseite. Traffic kommt über LinkedIn, DMs, Community-Antworten, Email-Outreach, direkte Nennung.
- **Kein Unternehmens-Traffic.** Der Unternehmens-Track lebt auf `/rechnungseingang-automatisieren`. Dual-Track-Disziplin nach Positionierung.md 6.4: Steuerberater sieht Unternehmens-Seite nie, und umgekehrt.
- **Kein direktes Verkaufsziel.** Conversion-Ziel ist die 15-Minuten-Demo, nichts darunter, nichts darüber.

## 2. Zielgruppe (ICP)

- Steuerberater in Kanzleien mit ≥4 Mitarbeitern (Einzelkanzlei ⌀ 4,5 MA oder BÄG ⌀ 24 MA).
- Kritische, rationale Leser. Akzeptieren keine Übertreibung, keine Startup-Theatralik.
- Kennen DATEV, ASR, Finmatics, BuchhaltungsButler. Können nicht belehrt werden — nur eingeordnet werden.
- Erwarten Zahlen mit Quellen, klare Preisangabe, DSGVO-Konkretion, DATEV-Einbettung.

## 3. Ton und Stil (bindend)

- Sie-Anrede durchgängig. Keine Emojis. Keine Superlative.
- Humanizer-Regeln aus `~/.claude/skills/flowbeaver-marketing/humanizer/references/criteria-german.md` einhalten: keine AI-Signalwörter (umfassend, nahtlos, ganzheitlich, robust, Mehrwert, Synergie, eintauchen, navigieren …), keine Monotonie der Satzlängen, maximal zwei Halbgeviertstriche pro Block.
- **Andreas' Voice bewahren.** Parallel-Konstruktionen ("Ich bin X. Ich bin Y.") sind Stil, nicht AI-Tell. Pointierte Meinungen sind erwünscht, nicht zu glätten. Siehe Memory `feedback_andreas_voice_not_jargon.md`.
- Kein Startup-Jargon: "erste Runde" statt "Pioneer-Kohorte"; "Ergänzung" statt "Disruption"; keine vergleichenden Herabsetzungen anderer Systeme ("nicht wie ein Quartals-Backlog" — genau das ist der Jargon, den man vermeiden will).
- Positionierung: DATEV-**Ergänzung**, niemals DATEV-Alternative. Flowbeaver setzt **vor** DATEV an.

## 4. Sachliche Grenzen

- **Keine erfundenen Validierungen.** Der Sprachen/Rückfragen-Wedge ist NICHT community-validiert. Nur als produkttechnische Fähigkeit formulieren ("Flowbeaver verarbeitet fremdsprachige Belege"), nicht als "Kanzleien sagen uns …". Siehe Memory `feedback_wedge_not_validated.md`.
- **Keine Pseudo-Scarcity.** Kein "Pilotpartner-Programm", keine "10 Plätze", keine "2 Jahre festgeschriebener Preis". Kapazitätsgrenze als operative Realität benennen, nicht als Marketing-Hebel.
- **Keine fiktiven Kundenzitate.** Es gibt aktuell keine zahlenden Kunden. Szenarien müssen als Produktfähigkeit formuliert sein, nicht als Case Study.
- **Keine Werbung für nicht existente Assets.** Kein "Blog mit 2–4 Artikeln pro Monat", solange der Blog nicht läuft.
- **Fachliche Korrektheit geht vor Elegance.** Ein Kurtaxe-Fehler killt das Vertrauen sofort. Jeder Buchhaltungs-Claim muss einer steuerberaterlichen Prüfung standhalten.

## 5. Block-Struktur und Anforderungen

Zehn Blöcke, in dieser Reihenfolge. Jeder Block hat eine klare Aufgabe.

### Block 1 — Hero
- H1: Produktbeschreibung, kein Slogan. Vorschlag: "Das KI-Vorsystem für Steuerkanzleien".
- Subline: Zwei Sätze. Erster Satz sagt, was Flowbeaver mit dem Beleg macht. Zweiter Satz sagt, wie das in DATEV ankommt. SKR03/04 darf konkret benannt werden.
- Ein einziger primärer CTA: "Demo buchen (15 Min.)". Ein Subline-Hinweis dazu ("direkt mit dem Gründer").
- Rechts neben dem Text ein Visual (Screenshot Beleg-Durchlauf oder Prozess-Mockup). Aktuell Platzhalter.

### Block 2 — Problem
- H2: "Die Lage in den Kanzleien".
- Teil 1: **Drei** Zahlen, nicht vier. Jede mit Quelle in Klammern. Keine zwei Zahlen, die dasselbe sagen. Aktuell festgelegte drei: 23,2 % Stellenbesetzung (STAX), 43,8 % Personalkostenquote (STAX), 91,6 %/~30 % KI-Relevanz vs. -Nutzung (SWI Finance).
- Teil 2: **Drei** konkrete Schmerzen, die diese Zahlen in der Kanzlei erzeugen. Jeder Schmerz als Fett-Lead-In, ein bis zwei Sätze Prosa. Aktuell festgelegt: Rückfragen-Schleifen mit Mandant / qualifizierte Fachkräfte in Routinearbeit gebunden / Monatsrhythmus-Spitzen.
- **Keine Mandanten-Schmerzen** (Skonti, Mahngebühren). Das ist nicht der Schmerz des ICP.

### Block 3 — Antwort
- H2: "Wie Flowbeaver diese drei Engpässe auflöst".
- **Drei Karten, 1:1 zu den drei Schmerzen aus Block 2, in derselben Reihenfolge.**
- Jede Karte: kurze Überschrift, expliziter Bezug auf den Schmerz ("Antwort auf Rückfragen-Schleifen"), zwei bis drei Sätze Prosa.
- Keine neue Aussage in Block 3, die nicht aus der Schmerz-Antwort-Logik folgt.

### Block 4 — Konkreter Durchlauf
- H2: "Wie ein Belegdurchlauf konkret aussieht".
- Prosa, keine Karten. Bricht den Rhythmus nach Block 3.
- Ein konkretes Belegbeispiel. Aktuell: italienische Hotelrechnung mit Übernachtung, Frühstück, Tourismusabgabe. **Vor Veröffentlichung von einem Steuerberater fachlich prüfen lassen**, idealerweise an einem echten Beleg durchspielen.
- Zwei bis drei kurze Absätze: (1) der Beleg, (2) was eine klassische OCR damit macht, (3) was Flowbeaver damit macht.

### Block 5 — DATEV und Sicherheit
- H2: "DATEV-Ergänzung, nicht DATEV-Ersatz" (oder ähnlich positiv).
- Zwei Listen: "So kommt das Ergebnis in DATEV" (CSV-Buchungsstapel, Belegbilder-ZIP, Ausblick auf Services) und "Datenschutz, konkret" (Server in DE, LLM in EU, Art. 28 AVV, keine dauerhafte Belegspeicherung, Human-in-the-loop).
- **Keine vagen Formulierungen** wie "EU-Verarbeitungspartner". Wenn unsicher: fragen, bevor geschrieben.
- Der DATEV-Marktplatz-Status aktuell: nicht gelistet. Das wird nicht verschleiert.

### Block 6 — Rechenbeispiel
- H2: "Ein Rechenbeispiel".
- Prosa-Rahmen mit offengelegten Annahmen (Belegzahl, Minuten pro Beleg, Stundensatz, Automatisierungsgrad). Eine eingebettete Rechnungs-Liste. Ein Satz am Ende mit Link auf den interaktiven Rechner auf `/produkt#rechner`.
- Der Rechner selbst lebt nicht hier, sondern auf der Produkt-Seite.

### Block 7 — Wer Flowbeaver baut
- H2: "Wer Flowbeaver baut" (oder vergleichbar).
- Harte Fakten: Name, Rolle, Hintergrund (Diplom-Kaufmann, 15 Jahre KI, Mercedes-Benz).
- **Zitat und Prosa: Andreas schreibt selbst.** Keine AI-Vorschläge, keine "überschreiben Sie das". Bis Andreas den Text liefert: Platzhalter, der sichtbar als solcher markiert ist — kein AI-Text, der sich als Gründerzitat tarnt.
- Kontaktzeile: LinkedIn + Email.
- Foto-Platzhalter rechts, bis Foto vorliegt.

### Block 8 — Ressourcen / Trust-Hub
- H2: "Wenn Sie uns erst einmal lesen wollen" (oder vergleichbar).
- Drei Karten. **Nur Inhalte, die heute tatsächlich existieren.** Aktuell: Branchenreport 2026 / Andreas auf LinkedIn / Community-Präsenz (DATEV-Community, „Steuerberater unter sich", newgen.tax).
- Sobald ein Blog live ist: vierte Karte oder LinkedIn-Karte ersetzen. Vorher nicht.

### Block 9 — Demo-CTA
- H2: "15 Minuten, direkt mit dem Gründer".
- Prosa: Was in den 15 Minuten passiert, wo die Grenze der Beratung liegt ("wenn der Fit nicht da ist, sage ich es in der Sitzung").
- **Ein einziger CTA**: "Demo buchen (15 Min.)". Kein zweiter Pfad daneben.
- Darunter ein kurzer Kapazitätshinweis als ehrliche Realität des Ein-Personen-Unternehmens, kein Verknappungsmechanismus.

### Block 10 — FAQ (kurz)
- H2: "Häufige Fragen".
- Sechs Fragen, nicht mehr. Die tiefe FAQ lebt auf `/produkt#faq`.
- Feste Frageset: Was macht Flowbeaver? / Muss an DATEV etwas geändert werden? / Unterschied zu DATEV-Buchungsassistent und ASR? / Was kostet Flowbeaver? / Ist das DSGVO-konform? / Wie startet eine Zusammenarbeit?
- Wichtig bei der ASR-Antwort: **ehrliche Grenze** — "Bei Standardrechnungen deutscher Lieferanten ist der Abstand kleiner. Spürbar wird der Unterschied bei fremdsprachigen, ungewöhnlich layouteten, gemischten Belegen." Kein Pauschal-"besser".
- Link am Ende auf die vollständige FAQ auf der Produkt-Seite.

## 6. CTA-Ökonomie

- Ein Haupt-CTA über die gesamte Seite: **Demo buchen (15 Min.)**.
- Kein sekundärer CTA ("Pilotpartner-Programm", "Waitlist eintragen" etc.). Zwei CTAs verwässern.
- Der Demo-CTA taucht drei Mal auf: Hero, Mitte (nach ROI oder nach FAQ), Ende.

## 7. Preis-Kommunikation

- Überall einheitlich: **299 € pro Monat, Flatrate, monatlich kündbar, keine Setup-Gebühr, keine Pro-Beleg-Abrechnung.**
- Keine 2-Jahres-Festschreibung, keine Einstiegspreis-Versprechen, keine Staffeln.
- Preis erscheint in FAQ, nicht als Hero-Angebot.

## 8. Was ausdrücklich NICHT auf die Homepage gehört

- Interaktiver Sparrechner (lebt auf `/produkt`).
- Vollständige FAQ (13+ Fragen, lebt auf `/produkt`).
- Technik-Deep-Dive (VLM, LLM, Regelwerk im Detail — lebt auf `/produkt`).
- Pilotpartner-Mechanik (komplett gestrichen, auch auf Produkt-Seite nicht mehr vorhanden).
- Unternehmens-Track-Inhalte (lebt auf `/rechnungseingang-automatisieren`).

## 9. Offene Punkte vor Go-Live

- Gründer-Block: Andreas' eigener Text für Zitat und Prosa.
- Hero-Visual: Screenshot oder Mockup des Beleg-Durchlaufs.
- Foto Andreas Schwarzkopf.
- Fachliche Prüfung des Belegbeispiels in Block 4 durch einen Steuerberater.
- Entscheidung: Bleibt der DSGVO-Claim "Server in Deutschland, LLM-Verarbeitung in EU-RZ" so stehen? Falls konkretere Aussagen möglich sind (Provider-Name, Zertifizierungen), präzisieren.
- Community-Präsenz-Karte in Block 8: bestätigen, dass wir in den genannten Communitys aktiv sind und antworten.

## 10. Arbeits-Regeln für die nächste Session

- **Kleine Schritte.** Ein Block pro Iteration, nicht alle zehn gleichzeitig.
- **Nach jedem Block Feedback abholen**, bevor der nächste angefasst wird. Nicht die ganze Seite durchrauschen.
- **Keine stilistischen Freiheiten an Andreas' eigenem Text.** Was Andreas wörtlich diktiert, wird wörtlich platziert.
- **Fakt-Checks vor Formulierung.** Bei jeder steuerlich relevanten Aussage: verifizieren oder weglassen.
- **Bei Unsicherheit: fragen, nicht glätten.** Gerade bei Voice-Themen.

## 11. Aktueller Zustand der Datei

`landingpages/homepage-v2-draft.html` enthält den Stand nach mehreren Iterationen. Er entspricht in weiten Teilen den oben formulierten Anforderungen, hat aber folgende bekannte Schwächen:
- Gründer-Block (Block 7) enthält AI-generiertes Zitat, nicht Andreas' eigenen Text.
- Hero-Visual und Gründer-Foto sind Platzhalter.
- Belegbeispiel (Block 4) fachlich nicht geprüft.
- `block-note`-Kommentare (gelbe Hinweiskästen) sind noch im HTML — vor Veröffentlichung entfernen.

Für die nächste Session: entweder auf diesem Stand aufbauen und Punkt für Punkt nachziehen, oder die Seite aus diesem Anforderungsdokument neu aufbauen.
