# Flowbeaver Profil-Slide, Playbook

**Zweck:** Personen-Profile im gleichen Design und Ton wie die Case-Study-Slides erstellen, als Team-/Gründer-Blatt im Flowbeaver-AI-Deck. Vorbild-Instanz: [profile-andreas-schwarzkopf-slide.html](profile-andreas-schwarzkopf-slide.html). Mechanische Vorlage: [profile-slide-TEMPLATE.html](profile-slide-TEMPLATE.html).

**Format:** Eine einzelne 16:9-Slide, HTML, druckbar als A4 quer. Teilt sich Design-System, Logo und CSS-Shell mit der Case-Study-Slide (siehe [case-study-slide-PLAYBOOK.md](case-study-slide-PLAYBOOK.md), Abschnitte 2, 5, 7, 9 gelten unverändert mit).

**Kontext:** Das Profil verkauft **die Person als Umsetzer von KI-Projekten** für den inhabergeführten Mittelstand, nicht als Berater. Es bedient dieselben drei Käuferängste wie die Liefer-Sparte (über den Tisch gezogen / Pilot stirbt / Daten unsicher).

**Kanonische Faktenquelle (verbindlich):** [`linkedin/profil-FINAL.md`](../linkedin/profil-FINAL.md) (Live-Fassung, kanonische Quelle). Headline, Proof-Punkte (§15), Stimme (§3), Kontakt (§14 → `info@flowbeaver.de`), Standort **Berlin**. **Deutsch primär, Englisch nur Spiegel** (§14). Vor jedem Profil-Slide-Text dort gegenprüfen, nicht aus Strategie-Entwürfen oder Case-Study-Material ableiten. Ergänzend: `strategie/Liefer-Sparte-Positionierung.md`.

---

## 1. Wann diese Slide

- **Gründer-/Team-Blatt** im Pitch-Deck oder als Anhang zum Erstgespräch.
- **Ein Blatt pro Person.** Andreas zuerst; ein Mitwirkender (Partner) bekommt eine eigene, identisch gebaute Slide (Abschnitt 6).
- Nicht als Lebenslauf. Nur die Fakten, die Liefer-Kompetenz für KI-Projekte belegen.

---

## 2. Aufbau (fix)

Kopf (Name + Rolle) → Portrait links / Beweise rechts → Trust-Streifen (Daten) → Footer (Einordnung + Kontakt).

- **Links:** Portrait (Foto-Slot mit Monogramm-Fallback) + 3–6 Kontext-Chips (Stationen oder Schwerpunkte).
- **Rechts:** Stat-Band (3 harte Zahlen) → Positionierungs-Lead (1–2 Sätze) → 3 Beweis-Zeilen (Icon + fetter Vorspann + Beleg).
- **Reihenfolge der Beweise = Prioritäts-Keil:** das am wenigsten Fälschbare zuerst (Unternehmer/Seriengründer), dann Liefer-Beweis, dann Daten/Vertrauen. Trust-Streifen trägt die Daten-Souveränität.

Design-Tokens, Farben (`#52267a`), Font (DM Sans), Icon-Kit, Print-Regeln: identisch zur Case-Study-Slide. Logo (Base64) und `<style>` **nie** von Hand anfassen.

---

## 3. Content-Modell, Slot für Slot

Zeichenbudgets sind Richtwerte, damit nichts umbricht (an der Andreas-Instanz kalibriert).

| Platzhalter | Slot | Regel | Budget |
|---|---|---|---|
| `{{ROLLE_EYEBROW}}` | Eyebrow (Versal) | Funktion im Deck, z. B. „Gründer & Umsetzung", „Technischer Partner". | 2–4 Wörter |
| `{{NAME}}` | H1 | Voller Name, keine Titel davor. | 2–3 Wörter |
| `{{ROLLE}}` | Rollen-Zeile (Akzent, fett-Teil) | Identitäts-Treffer, kein Satz. Z. B. „Unternehmer & KI-Architekt". | 2–4 Wörter |
| `{{ROLLE_ZUSATZ}}` | Rollen-Zeile (grau, `span`) | Ergänzender Halbsatz. Z. B. „baut produktive KI für den Mittelstand". | 4–7 Wörter |
| `{{INITIALEN}}` | Portrait-Monogramm | Fallback, wenn kein Foto. Wird vom `<img>` überdeckt. | 2 Buchstaben |
| `{{FOTO_DATEI}}` | Portrait `<img src>` | Dateiname/Pfad des Fotos. `object-fit: cover`, oben ausgerichtet. Monogramm-Span dann löschen. |, |
| `{{CHIPS_TITEL}}` | Label über Chips | Was die Chips sind, z. B. „Ausgewählte Stationen", „Schwerpunkte". | 2–3 Wörter |
| `{{CHIP_1..5}}` | Chips | Stationen (Arbeitgeber) oder Schwerpunkte. 3–6 Stück, Rest löschen. | je 1–3 Wörter |
| `{{STAT_n_ZAHL}}` | Stat-Band, große Zahl | Zahl + kurzes Wort. Z. B. „16 J.", „2 Exits", „3 Mio.". | 1–2 Tokens |
| `{{STAT_n_LABEL}}` | unter der Zahl | Woran gemessen. Eine Zeile. | 2–4 Wörter |
| `{{LEAD_SATZ}}` / `{{LEAD_KERN}}` / `{{LEAD_REST}}` | Positionierungs-Lead | 1–2 Sätze, was die Person liefert. `KERN` = ein Fettwort für den Kern. | zusammen 130–200 Z. |
| `{{BEWEIS_n_LEAD}}` | Beweis-Zeile, fett | Der Punkt in 2–4 Wörtern, mit Punkt am Ende. | 2–4 Wörter |
| `{{BEWEIS_n_TEXT}}` | Beweis-Zeile, Fließtext | Der Beleg. Konkret, mit Zahl/Referenz wo möglich. | 90–150 Z. |
| `{{TRUST_LEAD}}` | Trust-Streifen, fett | Governance-Versprechen in 2–3 Wörtern. | 2–3 Wörter |
| `{{TRUST_PUNKT_1..4}}` | Trust-Streifen, `·`-getrennt | Konkrete Kontroll-/Sicherheits-Fakten. Nicht benötigte löschen. | je ~4–8 Wörter |
| `{{FOOT_LINKS}}` | Footer links | Einordnung: Abschluss · Region · Zielmarkt. | kurz |
| `{{FOOT_KONTAKT}}` | Footer rechts (Akzent) | Website · E-Mail (oder LinkedIn). | kurz |

Icons in den Beweis-Zeilen (Aktentasche / Code-Klammern / Haken-im-Kreis) sind austauschbar, 24×24 viewBox, `stroke="#52267a"`, nie gefüllt.

---

## 4. Sprache & Stil

Es gelten `CLAUDE.md`, der Brand-Voice-Check und die Humanizer-Regeln (siehe Case-Study-Playbook, Abschnitt 5) zusätzlich:

- **„Sie", sachlich-selbstbewusst.** Die Fakten tragen. Keine Slogans, keine Provokation, keine Ausrufezeichen.
- **„Ich" ist hier erlaubt**, auf einer Personen-Slide für Haltung und Positionierung. Kein flächiges „wir".
- **Unternehmer zuerst, Technik als Werkzeug.** Rolle und Lead sprechen Ergebnis/ROI. Stack-Begriffe (RAG, MCP, Entra ID) gehören in Chips oder in die Beweis-Belege, nicht in H1/Rolle.
- **Zahlen belegbar.** Keine Zahl behaupten, die nicht durch einen echten Case gedeckt ist.
- **Verbotene Wörter** (CLAUDE.md): „Kohorte", „Skalierung", „Disruption", „revolutionär", „transformieren". Kunden-Cases anonymisiert (Branche + Größenordnung, keine Namen ohne Freigabe). Eigene Arbeitgeber-Stationen dürfen genannt werden.
- **Kein „kein Berater".** Andreas ist in der Beratungsbranche und will als Berater ernst genommen werden, der zusätzlich selbst umsetzt. Niemals „Unternehmer, kein Berater" o. Ä. als Beweis-Lead. Abgrenzung höchstens „Hands-on Entwicklung statt reiner Beratung".
- **Kein Em-Dash (`—` / `&mdash;`), niemals.** Harte Grenze (siehe CLAUDE.md und Humanizer §9a). Komma, Doppelpunkt, Klammern oder neuer Satz; Trenner ist der Mittelpunkt `&middot;`.
- **Solo-Founder nicht ausstellen.** Diese Slide ist eine der 1–2 gestatteten Stellen mit persönlichem Fokus, hier trägt der Personen-Frame. Nicht zusätzlich „Ein-Mann"/„alleine" hineinschreiben.
- **Umlaute** als Entities (`&auml;` etc.), wie in der Vorlage.

---

## 5. Andreas-Instanz (Dichte-Maßstab)

Deutsch, alle Werte 1:1 aus `linkedin/profil-FINAL.md`.

| Slot | Wert |
|---|---|
| ROLLE_EYEBROW | Gründer & KI-Entwickler (Experience-Titel §7) |
| NAME / ROLLE | Andreas Schwarzkopf / Produktive KI für den Mittelstand · die im Tagesgeschäft wirklich läuft |
| CHIPS ("Das baue ich") | RAG auf Unternehmenswissen · KI-Support-Assistenten · Dokumentenverarbeitung · Evaluation & Monitoring · EU- / Self-Hosting (§7) |
| STATS | 16 J. (KI-Erfahrung) · 3 Mio. (Kunden, 94 % Treffer) · 100+ (MA-Wissensplattform), alle aus §3/§15 |
| LEAD | "Ich entwickle sichere KI für mittelständische Unternehmen. **Erst wenn der Business Case steht, baue ich etwas.** Und wenn KI das falsche Tool ist, sage ich das auch." (§3, wörtlich) |
| BEWEISE (§15-Reihenfolge) | 1) Unternehmer mit Eigentümer-Blick (30+ J.) · 2) Architektur und Code aus einer Hand (eigenes Entwicklerteam, Übergabe-Problem) · 3) Erprobt, wo Fehler teuer sind (Mercedes-Benz, Bank/Produktion/Wissenssysteme) |
| TRUST | Datensouveränität von Anfang an: EU-/Self-Hosting · Regeln gegen Halluzination · gegen reale Fälle geprüft, nicht Demo · Daten unter Ihrer Kontrolle (Post C) |
| FOOTER | Diplom-Kaufmann (Wirtschaftsinformatik) · Berlin · LinkedIn Top Voice, linkedin.com/in/schwarzkopf · info@flowbeaver.de |

**Nicht verwenden** (alte/falsche Werte): „2 Exits", „Raum München" (Andreas sitzt in Berlin; München ist nur der anonymisierte Kunden-Kontext der Wissensplattform), `accounting@flowbeaver.de`, „senior engineering team" mit Partner-Nennung (Partner noch nicht öffentlich, §9). §203 StGB gehört zum Produkt Flowbeaver Accountant, nicht in die persönliche Trust-Zeile.

---

## 6. Mitwirkenden-/Partner-Slide erstellen

Gleiche Vorlage, zweite Person. **Disziplin (aus der Liefer-Positionierung):**

- **Titel exakt** übernehmen (der ICP prüft nach). Herkunft des technischen Partners nur umschreibend („eine der führenden europäischen KI-Umsetzungs-Initiativen"), **nicht namentlich** (appliedAI nie nennen).
- **Seniorität betonen, Verfügbarkeit nicht.** Keine „2 Tage/Woche" als Vollzeit-Team framen.
- **Erst wenn die schriftliche Partner-Vereinbarung steht** (Rollen, Beteiligung, öffentliche Nennung) veröffentlichen. Bis dahin bleibt die Partner-Slide intern; Name = Platzhalter.
- Rolle so wählen, dass sie Andreas ergänzt, nicht dupliziert: er = Strategie/Architektur/Akquise, Partner = Architektur/Umsetzung. Zusammen: „zwei, die beide selbst bauen".

---

## 7. EN-Spiegel & Freigabe-Checkliste

- **EN nie neu tippen**, per Textersetzung aus der DE-Datei erzeugen (Case-Study-Playbook, Abschnitt 7). Tech-Begriffe englisch lassen, „Mittelstand" stehen lassen, `§203 StGB` behalten, britische Schreibweise.
- [ ] Alle `{{PLATZHALTER}}` ersetzt (Suche nach `{{` leer).
- [ ] Foto eingesetzt **oder** Monogramm bewusst belassen.
- [ ] Passt ohne Überlauf auf 16:9 (im echten Browser prüfen; Druckvorschau A4 quer sauber). Hinweis: Headless-/DevTools-Fenster mit sehr breiter Viewport blähen die `cqw`-Ränder auf und täuschen einen Überlauf vor, im normalen Browserfenster gegenprüfen.
- [ ] Rolle/Lead = Ergebnis, kein Buzzword; „Sie"/„Ich" konsistent.
- [ ] Zahlen belegbar; fremde Cases anonymisiert; keine ungefreigegebenen Namen (inkl. Partner-Herkunft).
- [ ] Umlaute als Entities; Akzentfarbe `#52267a`, Logo/CSS unverändert.
