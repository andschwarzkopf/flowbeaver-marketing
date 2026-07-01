# Flowbeaver Case-Study-Slide — Playbook

**Zweck:** Neue Case-Study-Slides im exakt gleichen Format, Design und Ton erstellen wie [case-study-ai-company-memory-slide.html](case-study-ai-company-memory-slide.html). Dieses Dokument hält Struktur, Sprache, Stil und Prozess fest. Die mechanische Vorlage ist [case-study-slide-TEMPLATE.html](case-study-slide-TEMPLATE.html).

**Format:** Eine einzelne 16:9-Slide (kein Mehrseiter), HTML, druckbar als A4 quer. Gedacht als Sales-/Referenz-Slide (LinkedIn, Pitch-Deck-Einzelblatt, PDF-Anhang).

**Kontext:** Diese Slides belegen Liefer-Kompetenz der Sparte **Flowbeaver AI** (KI-Projekte für den Mittelstand). Kundennamen immer anonymisiert, Beweiskraft über harte Zahlen + Branche/Größenordnung. Siehe `strategie/Liefer-Sparte-Positionierung.md`.

---

## 1. Dateien & Workflow

| Datei | Rolle |
|---|---|
| `case-study-slide-TEMPLATE.html` | Ausfüllbare Vorlage mit `{{PLATZHALTER}}`. CSS + Logo fix. |
| `case-study-slide-PLAYBOOK.md` | Dieses Dokument: Regeln, Zeichenbudgets, Prozess. |
| `case-study-ai-company-memory-slide.html` | Referenz-Instanz DE (Vorbild). |
| `case-study-ai-company-memory-slide-en.html` | Referenz-Instanz EN (Spiegel). |

**Neue Slide erstellen:**
1. `TEMPLATE.html` kopieren → `case-study-<thema>-slide.html`.
2. Alle `{{PLATZHALTER}}` ersetzen (Inventar in Abschnitt 4).
3. Nicht passende Blöcke löschen (Kennzahl-Hero oder Chips-Karte sind optional, siehe Abschnitt 6). Layout bleibt stabil.
4. Im Browser öffnen und gegen die Checkliste (Abschnitt 9) prüfen.
5. **Logo (Base64) und `<style>` niemals von Hand anfassen** — nur Textinhalte.

**Wichtig:** HTML liefern, **kein PDF** erzeugen (User-Direktive). Wer ein PDF braucht, druckt die HTML über den Browser (Layout ist auf A4 quer eingerichtet).

---

## 2. Design-Prinzip (fix, nicht verhandeln)

- **Ein Bildschirm, ein Argument.** Alles muss ohne Scrollen auf die 16:9-Fläche. Wenn Text nicht passt, kürzen — nicht Schrift verkleinern, nicht Layout umbauen.
- **Skalierung über `cqw`** (Container-Query-Einheiten): Schrift und Abstände skalieren mit der Slide-Breite. Deshalb sieht die Slide auf jedem Bildschirm und im Druck gleich aus. Nicht auf `px` umstellen.
- **Dreiteilung:** Kopf (Ergebnis-Versprechen) → Mitte (Beweis links, Wie rechts) → Trust-Streifen (Fundament) → Footer (Einordnung).
- **Ruhe.** Viel Weißraum, eine Akzentfarbe, keine Deko.

### Design-Tokens (aus dem Brandbook, siehe Skill `flowbeaver-brand`)
| Token | Wert | Einsatz |
|---|---|---|
| `--fb-purple` | `#52267a` | Akzent: Zahlen, Rahmen-links, Icons, CTA-Farbe |
| `--fb-dark-red` | `#3c0f04` | Headline, Logo-Wortmarke, Chip-Text |
| `--fb-text` | `#404040` | Fließtext |
| `--fb-text-secondary` | `#606060` | Subline, „Bisher"-Zeile |
| `--fb-border` | `#e0e0e0` | Karten-Rahmen |
| Font | `DM Sans` (300–700) | überall |
| Aspect Ratio | `16 / 9` | fix |

Keine Emojis, keine Stockfotos, keine Farbverläufe im Inhalt.

---

## 3. Icon-Kit

Inline-SVG im Feather-Stil (1,6–1,7 stroke, `#52267a`). Vorhandene Icons und ihre Rolle:

| Slot | Icon (im Template) | austauschbar gegen |
|---|---|---|
| Beispiel | Person | Doc/Clipboard, wenn kein Personen-Bezug |
| Feature | Blitz | Zahnrad, Roboter, Sparkle |
| Quellen | Datenbank-Zylinder | Ordner, Netzwerk-Knoten |
| Trust | Schloss | Schild, Haken-im-Kreis |

Icons dürfen getauscht werden (24×24 viewBox, gleiche stroke-Werte behalten). Quelle: feathericons.com / lucide.dev. Immer `stroke="#52267a"`, nie gefüllt.

---

## 4. Content-Modell — Slot für Slot

Reihenfolge = Lesefluss. Zeichenbudgets sind Richtwerte, damit nichts umbricht (an der Referenz kalibriert).

| Platzhalter | Slot | Regel | Budget |
|---|---|---|---|
| `{{THEMA_KURZ}}` | Eyebrow (oben, Versal) | Angebots-/Themenname. Kein Satz. | 2–4 Wörter |
| `{{HEADLINE_ERGEBNIS}}` | H1 | **Ergebnis, aktiv formuliert.** Nutzen, nicht Technik. Verb steckt drin. | 3–6 Wörter, ~30–45 Z. |
| `{{LOESUNG_NAME}}` | fett in Subline + in „Mit …"-Zeile | Name des Angebots/Systems (z. B. „AI Company Memory"). Überall identisch. | 1–3 Wörter |
| `{{EINLEITUNG_1_2_SAETZE}}` | Subline | Was ist es, was tut es. Kein Marketing-Superlativ. | 130–220 Z. |
| `{{KENNZAHL}}` | Hero-Zahl (groß) | **Der eine härteste Beweis.** Prozent, Faktor, Menge. | z. B. „80 %", „94 %", „3 Mio." |
| `{{KENNZAHL_LABEL}}` | neben der Zahl, fett | Woran gemessen. | 2–4 Wörter |
| `{{KENNZAHL_BELEG}}` | unter dem Label | Ein Satz, der die Zahl greifbar macht (vorher/nachher). | 60–95 Z. |
| `{{ANWENDUNGSFALL}}` | Beispiel-Titel (nach „Beispiel:") | Konkreter, benennbarer Fall. | 4–7 Wörter |
| `{{SCHMERZ_VORHER}}` | „Bisher:"-Zeile | Der Ist-Zustand, der wehtut. Konkret, nicht abstrakt. | 110–180 Z. |
| `{{NUTZEN_NACHHER}}` | „Mit …:"-Zeile | Was die Lösung daraus macht. Enthält oft den Trust-Haken (Quellen, Berechtigung). | 110–180 Z. |
| `{{FEATURE_NAME}}` | Feature-Karten-Titel | Das prägnanteste Wie-Merkmal. | 1–2 Wörter |
| `{{FEATURE_TEXT}}` | Feature-Text | Wie es funktioniert, in Nutzen übersetzt. **Ein** Fettwort für den Kern. | 140–200 Z. |
| `{{QUELLEN_TITEL}}` | Chips-Karten-Titel | Was die Chips sind (z. B. „Erschlossene Wissensquellen", „Angebundene Systeme", „Bausteine"). | 2–3 Wörter |
| `{{CHIP_1..5}}` | Chips | Kurze Schlagworte (Systeme, Datenquellen, Module). 4–8 Stück, nicht benötigte löschen. | je 1–3 Wörter |
| `{{TRUST_LEAD}}` | Trust-Streifen, fett | Governance-Versprechen in 2–3 Wörtern (z. B. „Sicher und kontrolliert"). | 2–3 Wörter |
| `{{TRUST_PUNKT_1..3}}` | Trust-Streifen, `·`-getrennt | Drei konkrete Kontroll-/Sicherheits-Fakten. | je ~5–9 Wörter |
| `{{BRANCHE}}` | Footer links | Branche/Typ des Kunden (anonymisiert). | 2–4 Wörter |
| `{{GROESSE}}` | Footer links | Größenordnung (z. B. „100+ Mitarbeitende"). | kurz |
| `{{REGION}}` | Footer links | grobe Region (z. B. „Raum München"). Steht vor „(anonymisiert)". | kurz |
| `{{ABSENDER}}` | Footer rechts | Wer geliefert hat. **Vor Verwendung bestätigen:** „Flowbeaver AI" (Sparte) vs. „Flowbeaver GmbH" (Rechtsträger) einheitlich wählen. | kurz |
| `{{ZEITRAUM}}` | Footer rechts | Quartal/Jahr (z. B. „Q2 2026"). | kurz |

---

## 5. Sprache & Stil

Gilt zusätzlich zu `CLAUDE.md` und dem Memory-Brand-Voice-Check.

- **Anrede „Sie", sachlich-selbstbewusst.** Die Fakten tragen. Keine Slogans, keine Provokation, keine Ausrufezeichen.
- **Ergebnis vor Technik.** Headline und Subline sprechen Nutzen. Stack-Begriffe (RAG, Entra ID, MCP) gehören in Feature-Text/Chips, nicht in die Headline.
- **Zahlen konkret und ehrlich.** „80 % weniger Onboarding-Zeit", nicht „massive Effizienzgewinne". Keine Zahl behaupten, die nicht belegbar ist.
- **Keine KI-Sprachmuster** (Humanizer-Regeln): keine Gedankenstrich-Dramatik, kein „nicht X, sondern Y" als Dauerschleife, keine dramatischen Ein-Wort-Fragmente, keine Füllwörter („genau", „exakt").
- **Anglizismen zulässig**, wo im deutschen Tech-Sprech normal (RAG, Monitoring, Onboarding, Business Case, Use Case). Nicht zwanghaft eindeutschen.
- **Verbotene Wörter** (aus CLAUDE.md): „Kohorte", „Skalierung", „Disruption", „revolutionär", „transformieren". Kunden nie namentlich ohne Freigabe.
- **Umlaute korrekt** (ä/ö/ü), im HTML als Entities (`&auml;` etc.) wie in der Vorlage.

**Gut vs. schlecht (Headline):**
- Gut: „Ihr Firmenwissen arbeitet mit" · „Belege rein, DATEV-Stapel raus"
- Schlecht: „Revolutionäre KI-Plattform für maximale Effizienz" (Superlativ, Buzzword, kein konkretes Ergebnis)

---

## 6. Varianten

Das Grundgerüst bleibt, einzelne Blöcke sind schaltbar:

- **Ohne harte Kennzahl:** Hero-Block (`.hero`) löschen. Die Beispiel-Karte rückt hoch. Nutzen, wenn (noch) keine belastbare Zahl vorliegt.
- **Ohne Chips:** Chips-Karte (`.card.sources`) löschen; Feature-Karte füllt die rechte Spalte. Nutzen, wenn keine sinnvolle Aufzählung existiert.
- **Zwei Kennzahlen:** einen zweiten `.hero`-Block in die linke Spalte duplizieren (dann Beispiel ggf. kürzen).
- **Produkt-Kontext (Flowbeaver Accountant):** gleiches Layout, aber Eyebrow „Case Study · Flowbeaver Accountant", Trust-Punkte auf §203/DATEV/EU-Hosting, Footer-Absender = Produktseite. Voice bleibt.
- **CTA-Zeile** (optional): Es gibt bewusst keine CTA im Footer — die Slide ist Beweis, kein Angebot. Wenn eine CTA nötig ist, in die rechte Footer-Zeile statt „Erfolgreich umgesetzt …".

---

## 7. EN-Spiegel erzeugen (Pflichtverfahren)

Englische Version **nie neu tippen** — das Base64-Logo und die Struktur würden dabei beschädigt. Stattdessen aus der fertigen DE-Datei per Textersetzung erzeugen:

1. DE-Datei einlesen, `<html lang="de">` → `<html lang="en">`.
2. Jede sichtbare deutsche Zeichenkette per `.replace()` gegen die EN-Fassung tauschen (Skript, wie bei `case-study-ai-company-memory-slide-en.html` erstellt).
3. Prüfen: alle Ersetzungen matchen, keine deutschen Reste, Datei endet auf `</html>`, `base64,iVBOR` noch vorhanden.
4. Speichern als `…-slide-en.html`.

Übersetzungslinie: Tech-Begriffe englisch lassen; „Mittelstand" stehen lassen; britische Schreibweise (analyse, anonymised); rechtliche Anker (`§203 StGB`) behalten.

---

## 8. Neue Slide bei Claude bestellen — Brief-Vorlage

Diese Felder ausfüllen und schicken, dann wird die Slide erstellt:

```
Thema/Angebot:        (z. B. "AI Service Layer")
Kunde (anonymisiert): Branche · Größe · Region
Headline-Ergebnis:    (der eine Nutzen in 3-6 Wörtern)
Härteste Kennzahl:    (Zahl + woran gemessen + 1 Beleg-Satz)   [optional]
Beispiel-Fall:        Bisher (Schmerz) → Mit uns (Nutzen)
Kern-Feature:         Name + 1-2 Sätze wie es wirkt
Chips:                4-8 Systeme/Quellen/Bausteine            [optional]
Trust:                3 Governance-Fakten
Absender/Zeitraum:    (z. B. Flowbeaver AI · Q3 2026)
Sprache:              DE / EN / beide
```

---

## 9. Checkliste vor Freigabe

- [ ] Alle `{{PLATZHALTER}}` ersetzt (Suche nach `{{` muss leer sein).
- [ ] Passt ohne Scrollen/Überlauf auf die 16:9-Fläche (im Browser prüfen).
- [ ] Headline = Ergebnis, kein Buzzword; kein Superlativ.
- [ ] Keine Gedankenstrich-Dramatik, keine Emojis, „Sie"-Anrede.
- [ ] Zahlen belegbar; Kunde anonymisiert; keine ungefreigegebenen Namen.
- [ ] Umlaute als Entities, korrekt.
- [ ] Akzentfarbe `#52267a`, Logo/CSS unverändert.
- [ ] Druckvorschau A4 quer sauber (kein Abschnitt abgeschnitten).
- [ ] Falls EN nötig: per Textersetzung erzeugt, Logo intakt.

---

## 10. Referenz-Instanz (ausgefülltes Beispiel)

Die Vorlage, gefüllt = `case-study-ai-company-memory-slide.html`:

| Platzhalter | Wert |
|---|---|
| THEMA_KURZ | AI Company Memory |
| HEADLINE_ERGEBNIS | Ihr Firmenwissen arbeitet mit |
| LOESUNG_NAME | AI Company Memory |
| KENNZAHL / LABEL | 80 % / weniger Onboarding-Zeit |
| KENNZAHL_BELEG | Neue Projektmitglieder sind in Stunden produktiv, früher dauerte das Tage. |
| ANWENDUNGSFALL | Entwickler-Onboarding im Kundenprojekt |
| FEATURE_NAME / TEXT | Agent-first / KI-Agenten lösen komplexe, systemübergreifende Fragen … |
| QUELLEN_TITEL | Erschlossene Wissensquellen |
| CHIPS | CRM · SharePoint/OneDrive · Jira · Wiki · Slack · freigegebene E-Mails · Meeting-Transkripte |
| TRUST | Sicher und kontrolliert: rollenbasierte Zugriffe · Freigabe/Löschung durch Information Owner · jede Anfrage von einem Menschen |
| FOOTER | Wissensintensiver Dienstleister · 100+ Mitarbeitende · Raum München (anonymisiert) — Flowbeaver GmbH · Q2 2026 |

Nutze diese Instanz als Tonfall- und Dichte-Maßstab für jede neue Slide.
