# Content-Strategie: Website, LinkedIn & Fachcommunitys
*Stand: März 2026 — 6-Wochen-Sprint bis Kohorte-1-Webinar*
*Letzte Überarbeitung: April 2026 (Community-Kanäle, Techniker-Positionierung, Dual-Track)*

---

## Changelog April 2026

- **Fachcommunitys als gleichrangige Content-Kanäle** aufgenommen (neuer Abschnitt 4b): DATEV-Community, Facebook "Steuerberater unter sich", newgen.tax — mit eigenem Antwort-Template und Zeitbudget.
- **Website-Startseite** an `Session-Handoff-Website-Ueberarbeitung.md` angeglichen: Techniker-Gründer-Sektion, konkrete Community-Zitate als Problem-Beleg, LLM-Sprach-Differenziator prominent.
- **Conversion-Tracking-Realitätscheck** ergänzt: GA4-Button-Clicks sind keine echten Conversions (keine verlässlichen Lead-Daten bisher). Primär zählt die Brevo-Waitlist-Liste.
- **LinkedIn Personal** auf Kommentar-Spiel + 2 Posts/Woche umgestellt; LinkedIn-Gruppen-Hinweis entfernt (in DE tot).
- **Dual-Track** andeuten: zweite Landingpage `/rechnungseingang-automatisieren` für Unternehmens-Track — getrenntes Vokabular, getrennte Hashtags.
- **Hierarchie-Satz** relativiert: DATEV-Community wird zum Primärkanal für fachliche Autorität, LinkedIn bleibt wichtig — aber nicht mehr allein an der Spitze.

---

## 1. Kanalrollen & Ziele

| Kanal | Primäre Funktion | Ziel (6 Wochen) |
|---|---|---|
| **DATEV-Community** | Fachliche Autorität, SEO-Sichtbarkeit, Profil-Klicks | 20–30 substantielle Thread-Antworten, 2–3 Folge-DMs |
| **Website (vollständig)** | SEO-Traffic + Conversion in Waitlist | 80–150 Waitlist-Anmeldungen |
| **LinkedIn Personal (CEO)** | Demand Generation + Vertrauen aufbauen | 2 Posts/Woche + 10 min/Tag Kommentare unter Multiplikatoren |
| **Facebook "Steuerberater unter sich"** | Reichweite über Multiplikatoren | Mitgliedschaft + erste 3–5 Posts nach Lurken |
| **LinkedIn Company Page** | Credibility Signal, Produktkommunikation | Page live, 50+ Follower |
| **newgen.tax Community** | Kuratierte Zielgruppe | Profil aktiv, 2–3 Fachbeiträge |

**Hierarchie (revidiert April 2026):** Fachcommunitys (DATEV, Facebook, newgen.tax) bauen über drei Monate die fachliche Autorität auf, die kein Ad-Budget kaufen kann. Parallel dazu LinkedIn Personal (Kommentar-Spiel + Posts) und Website als Traffic-Ziel. LinkedIn Company bleibt Credibility Signal, nicht Traffic-Treiber. Die ursprüngliche Einzel-Spitze "LinkedIn Personal" wird durch ein Kanal-Duo ersetzt: Community-Räume für fachliche Tiefe, LinkedIn für Breite.

---

## 2. Website

### Seitenarchitektur

| Seite | Zweck | Status-Ziel |
|---|---|---|
| **Startseite** | Kernbotschaft + Hauptkonversion | Woche 1 live |
| **Produkt/Funktionen** | Dreiklang erklären, Screenshots, Workflow | Woche 2 live |
| **Pricing** | 3 Kohorten, Beta-Scarcity sichtbar machen | Woche 3 live |
| **Über uns / Gründer** | Vertrauen durch Persönlichkeit + Expertise | Woche 1 live |
| **Blog** | SEO-Traffic, Long-Tail-Keywords, Awareness | Artikel 1 Woche 2 |
| **FAQ** | Einwände ausräumen (DATEV, Datenschutz, Genauigkeit) | Woche 2 live |

### Startseite — Pflicht-Elemente (überarbeitet April 2026)

Die Elemente folgen `Session-Handoff-Website-Ueberarbeitung.md`. Tonalität: leise, technisch, konkret — keine Stockfotos lachender Buchhalter, keine Emojis, keine Dark Patterns.

- **Hero:** DATEV-Ergänzung als Kernbotschaft, keine Alternative. Kein "KI revolutioniert …"-Opener. Konkret formulieren: *"Flowbeavers KI-Vorsystem liefert fertig vorkontierte Belege direkt in Ihren DATEV-Workflow — auch bei englischen Rechnungen, Schweizer Belegen und exotischen Geschäftsvorfällen."*
- **Differenziator prominent:** LLM versteht jede Sprache → weniger Rückfragen beim Mandanten. Das ist der April-2026-geschärfte Hebel aus `Positionierung.md` 1.1.
- **Problem-Section mit konkreten Community-Zitaten:** Rückfragen als versteckter Zeitkiller, fremdsprachige Belege, abgelehnte Mandate. Original-Zitate aus DATEV-Community nutzen (aus `Session-Handoff-Website-Ueberarbeitung.md`), nicht erfinden: *"Belegerkennung treibt mich in den Wahnsinn"*, *"'Invoice No.' wird als Barcode erkannt"*, *"OCR merkt sich falsche Werte"* — jeweils mit "Stimme aus der DATEV-Community" gekennzeichnet.
- **Dreiklang-Erklärung:** LLM + KI-OCR + Regelwerk (visuell, nicht textlastig).
- **Techniker-Gründer-Sektion (neu):** "Ich bin der Techniker, der das Werkzeug baut — nicht der Kanzlei-Insider." Andreas mit Foto, 15 Jahre KI, Mercedes-Benz, Diplom-Kaufmann. Ehrlichkeit schlägt Tarnung.
- **Trust-Sektion:** DATEV-Kompatibilitätshinweis (Logo nur, wenn lizenzrechtlich geklärt — sonst Text-Badge "kompatibel mit DATEV Unternehmen Online"), Datenschutz Deutschland, Gründer-Foto.
- **Beta-Einladung:** "10 Plätze — wenn vergeben, frühestens in 6 Monaten wieder verfügbar."
- **CTA:** "Jetzt Platz sichern" → Waitlist-Formular. Ob Waitlist oder echtes Demo-Formular primär sein soll, ist offen (15 Sessions auf `/ki-belegerkennung` reichen statistisch nicht — siehe `STRATEGY.md`).

### Conversion-Pfade

```
Blog-Artikel
    └─→ Inline-CTA im Artikel ("Jetzt Beta-Platz sichern") → Waitlist-Formular

Startseite
    └─→ Beta-Section → Waitlist-Formular

Pricing-Seite
    └─→ "Platz sichern für €299/Monat" → Waitlist-Formular

Über uns / Gründer
    └─→ "Ich zeige es Ihnen persönlich — melden Sie sich an" → Waitlist-Formular
```

**UTM-Tracking:** Jeder LinkedIn-Post, der auf die Website verlinkt, erhält einen UTM-Parameter (`utm_source=linkedin&utm_medium=social&utm_campaign=personal` bzw. `company`), um den Kanal-Beitrag zur Waitlist messbar zu machen.

**Conversion-Tracking-Realitätscheck (April 2026):** GA4-Conversions sind aktuell unzuverlässig — Button-Clicks werden als Conversions gezählt, es gibt keine verlässlichen echten Lead-Daten aus Paid-Search über den gesamten Zeitraum März/April. Primäre Wahrheit ist die Brevo-Waitlist-Liste (tatsächlich abgeschickte Formulare), nicht GA4- oder Ads-Events. Konsequenz: keine Paid-Budget-Entscheidungen auf GA4-Conversion-Zahlen stützen, bis echtes Server-Side-Tracking oder Brevo-Logs als Grundlage hinterlegt sind.

**Dual-Track-Landingpages (April 2026):** Neben `/ki-belegerkennung` (Kanzlei-Track) entsteht eine zweite Landingpage `/rechnungseingang-automatisieren` (Unternehmens-Track). Copy, Keywords, CTA und Lead-Magnete sind strikt getrennt (siehe `Positionierung.md` 6.4). LinkedIn-Posts verlinken abhängig von Hashtag-Welt auf jeweils eine der beiden Seiten — kein Mischen.

### Lead-Magnet (ab Woche 4, optional)
Checkliste: *"Rechnungseingang digitalisieren — 7 Schritte für Steuerkanzleien"* als PDF.
- Zugang per E-Mail-Adresse → direkt in Brevo-Sequenz
- Verlinkt aus Blog-Artikel 1 (KI-Belegerkennung) und Startseite
- Niedrigschwelliger Einstieg für Kanzleien, die noch nicht bereit sind für Waitlist

### SEO-Content-Plan
Der Blog-Artikel-Backlog wird in `seo/content-plan.md` gepflegt (7 Artikel in 3 Phasen über 9–16 Wochen). Priorität im Sprint: Artikel 1 (KI-Belegerkennung vs. OCR) in Woche 2 — als Grundlage für LinkedIn-Post-Themen und frühen SEO-Einstieg.

---

## 3. LinkedIn Company Page

### Setup (einmalig, Woche 1)
- **Name:** Flowbeaver
- **Tagline:** "KI-Vorsystem für vorbereitende Buchhaltung — DATEV-kompatibel"
- **Logo:** Flowbeaver-Logo
- **Banner:** Dreiklang-Grafik oder angepasstes Hero-Bild von Landingpage
- **Website:** flowbeaver.de mit UTM-Tracking-Link
- **Beschreibung:** 3–4 Sätze: Was ist Flowbeaver, für wen, warum DATEV-kompatibel, wo anmelden

### Kanalrolle vs. Personal Page

| Dimension | LinkedIn Personal | LinkedIn Company |
|---|---|---|
| Reichweite | Hoch (persönliche Verbindungen) | Niedrig (Algorithmus benachteiligt Pages) |
| Vertrauen | Sehr hoch (menschliche Stimme) | Mittel (Unternehmensformat) |
| Content | Persönliche Anekdoten, Meinungen, Einblicke | Produktfokus, Sachlichkeit, Fakten |
| Aufwand | Hoch (eigene Posts) | Niedrig (Reposts + 1 Eigenpost/Woche) |
| Funktion | Demand Generation | Credibility Signal |

### Content-Typen (2x/Woche)

**1. Unternehmens-Repost (1x/Woche, Dienstag)**
CEO-Post reposten, kurze Unternehmens-Perspektive ergänzen (1–2 Sätze).
Beispiel: "Andreas beschreibt hier genau das Problem, das Flowbeaver löst. Mehr zu unserem Ansatz auf flowbeaver.de [Link]."

**2. Produktschaufenster (1x/Woche, Freitag)**
Screenshot aus der Anwendung + 2–3 sachliche Sätze was zu sehen ist.
Beispiele: DATEV-Export-Vorschau, Belegerkennungs-Interface, Vorkontierungs-Vorschlag, Buchungsstapel-Übersicht.

**3. Meilensteine (bei Bedarf)**
Waitlist-Zahlen, Webinar-Ankündigung, Beta-Start-Datum. Kein Dauerfeuer — nur bei echten Ereignissen.

### Ton
Sachlich, produktzentriert. Keine persönlichen Anekdoten, kein Startup-Jargon. "Sie"-Anrede. DATEV-Kompatibilität in jedem zweiten Post erwähnen.

### KPIs Company Page
- Follower: 50+ nach 6 Wochen
- Post-Impressionen: 100–400 pro Post
- Klicks auf Website-Link: messbar über UTM

---

## 4. LinkedIn Personal (CEO — Andreas Schwarzkopf)

### Kanalrolle
Primärer Awareness- und Vertrauenskanal auf LinkedIn. Andreas' persönliche Stimme erreicht mehr Kanzleien als die Company Page. Solo-Founder-Vorteil wird explizit eingesetzt: direkter Zugang, schnelle Iteration, persönliche Haftung für Produktqualität. Die **Techniker-Positionierung** (Andreas = baut das Werkzeug, ist nicht Kanzlei-Insider) ist der rote Faden — siehe `Positionierung.md` 1.2.

### Mechanik (April 2026)
- **Keine Gruppen.** LinkedIn-Gruppen sind in Deutschland tot.
- **Hashtag-Folgen wurde Ende 2024 abgeschafft.** Hashtags sind nur noch Suchfilter. Trotzdem unter jedem Post setzen (#steuerberater, #steuerkanzlei, #datev, #digitalisierung, #erechnung, #zugferd, #kanzleimanagement) — für Auffindbarkeit, nicht für Follower.
- **Kommentar-Spiel (10 Min./Tag):** 3–5 substantielle Kommentare unter Posts von Jens Henke, Sebastian Merla, Gregor Ganschow, Carola Heinen, Benjamin Herz, Falk Weinreich. Kein Selbstpromotion, keine Links. Nur fachlicher Beitrag.
- **Eigene Posts (2×/Woche):** Di und Do, nach unten aufgelisteten Pillars.
- **Unternehmens-Track separat:** Posts für Buchhaltungsleitungen laufen unter #buchhaltung, #rechnungseingang, verlinken auf `/rechnungseingang-automatisieren`.

### 6 Content-Pillar (inkl. Pillar 6 neu)

| # | Pillar | Thema | Frequenz |
|---|---|---|---|
| 1 | **Fachkräftemangel & Skalierung** | Schmerz der Kanzlei, keine Lösung pitchen | 1–2x/Monat |
| 2 | **KI-Expertise** | Edukativ: OCR vs. LLM, Grenzen der KI, was Dreiklang bedeutet | 1–2x/Monat |
| 3 | **Behind the Scenes / Techniker-Gründer** | Screenshots, Loom-Videos, Entwicklungsfortschritt, Fehler — mit Techniker-Stimme | 1x/Monat |
| 4 | **Scarcity / Waitlist-Updates** | Echte Zahlen, Plätze werden knapp, Webinar-Ankündigung | 1x/Monat |
| 5 | **DATEV-Optimierung** | DATEV-Frustration aufnehmen, Flowbeaver als Ergänzung positionieren | 1x/Monat |
| 6 | **Sprach- und Kontextrobustheit** (neu) | Fremdsprachige Belege, exotische Rechnungen, Rückfragen-Reduktion | 1–2x/Monat |

### Wöchentlicher Rhythmus
- **Dienstag:** Pillar 1 oder 2 (Problem/Expertise — wachstumsstärkstes Format)
- **Donnerstag:** Pillar 3, 4 oder 5 (Variation, Persönlichkeit, Aktualität)

### Post-Format
- Länge: 800–1.300 Zeichen
- Hook: Zeile 1–2 muss allein stehen und neugierig machen
- Kein Link im Post-Text → Link in ersten Kommentar oder Profil-CTA ("Link in meinem Profil")
- Kein AI-Feeling: konkrete Details, Zahlen, unvollständige Sätze, echte Anekdoten
- ICP-Vokabular: Mandanten, FiBu, Buchungsstapel, Vorkontierung, Belegpflege, Rückfragen, Geschäftsvorfall

### KPIs Personal
- Follower-Wachstum: +100–200 in 6 Wochen
- Avg. Impressionen/Post: 500–1.500
- Profil-Aufrufe: steigend Woche über Woche
- Waitlist-Anmeldungen aus LinkedIn: messbar per UTM

---

## 4b. Fachcommunitys als Content-Kanäle (neu, April 2026)

Parallel zu Website und LinkedIn wird Content in drei Fachcommunitys produziert — als Antworten, nicht als Posts. Kein Pitch, keine Links, keine Selbstpromotion. Die vollständige Channel-Mechanik steht in `Kanalstrategie.md` 3.8–3.10; hier nur der Content-Aspekt.

### DATEV-Community (datev-community.de)

- **Zeitbudget:** 60 Min./Woche, 2–3 substantielle Thread-Antworten.
- **Boards:** "Unternehmen online", "Betriebliches Rechnungswesen", "Ideen zu Unternehmen online".
- **Anknüpfungspunkte:** 16 konkrete Threads in `Fachcommunitys-Anknuepfungspunkte.md` gelistet — priorisiert nach Match-Stärke (ASR-Erfahrungen, DUO-Belegerkennung, Pre-Kontierung, Fremdsprachen-Belege, E-Rechnung).
- **Antwort-Template:** Paraphrase → fachliche Nuance → offene Rückfrage → kein Link/Pitch. (Siehe `Content-Framework.md` Hook-Bibliothek.)

### Facebook-Gruppe "Steuerberater unter sich"

- **Zeitbudget:** 30 Min./Woche.
- **Phasierung:** Aufnahme beantragen → 2 Wochen Lurken → erste gezielte Beiträge zu Digitalisierung, Belegverarbeitung, Fachkräftemangel.
- **Multiplikatoren:** Jens Henke, Sebastian Merla, Gregor Ganschow sind hier aktiv — Beiträge unter ihren Posts erreichen die weiteste Kanzlei-Audience.

### New Generation Steuerberater Community (community.newgen.tax)

- **Zeitbudget:** 20 Min./Woche.
- **Fokus:** Kuratierte Audience, passt exakt auf Flowbeaver-ICP. Beiträge in Fach-Foren, persönlicher als in der DATEV-Community.

### Messgrößen Community-Content

Nicht Impressionen oder Likes, sondern:
- Profil-Klicks auf "Andreas Schwarzkopf"
- Folge-Direktnachrichten mit konkreten Rückfragen
- Indirekt: Google-Sichtbarkeit alter Threads (SEO)
- Indirekt: Waitlist-Einträge, die in Brevo "über Empfehlung" oder ohne UTM auftauchen

---

## 5. Inhaltsfluss zwischen den Kanälen

```
SEO-Artikel (Website/Blog)
        ↓
LinkedIn Personal: Kernthese aus Artikel als eigenständiger Post
        ↓
LinkedIn Company: Repost mit 1-Satz-Produktkontext
        ↓
Traffic auf Artikel via UTM-Link im Kommentar
        ↓
Artikel → Inline-CTA → Waitlist
        ↓
E-Mail-Sequenz (Brevo Welcome) → Webinar-Einladung → Beta-Auswahl
```

**Content-Recycling-Regel:**
- Jeder SEO-Artikel liefert 1–2 LinkedIn-Posts (Kernthesen extrahieren)
- Jede LinkedIn-Diskussion in den Kommentaren ist ein potenzielles FAQ-Element für die Website
- Webinar-Content → Blog-Zusammenfassung nach dem Webinar

---

## 6. Muster-Woche (Redaktionsrhythmus)

| Tag | Kanal | Content-Typ | Aufwand |
|---|---|---|---|
| Mo | DATEV-Community | 1 substantielle Thread-Antwort | 20–25 Min. |
| Di | LinkedIn Personal | Pillar 1 oder 2 (Eigenpost) | 30–45 Min. |
| Di | LinkedIn Company | Repost des CEO-Posts + 1 Satz | 5 Min. |
| Mi | DATEV-Community + Facebook | 1 DATEV-Antwort + 1 Facebook-Beitrag | 30–40 Min. |
| Do | LinkedIn Personal | Pillar 3, 4, 5 oder 6 (Eigenpost) | 30–45 Min. |
| Fr | LinkedIn Company | Produktschaufenster-Post | 15 Min. |
| Fr | newgen.tax | 1 Fachbeitrag oder Kommentar | 20 Min. |
| Täglich | LinkedIn Feed | 3–5 Kommentare unter Multiplikator-Posts | 10 Min. |
| Laufend | Website/Blog | SEO-Artikel (lt. content-plan.md) | 2–4 Std./Woche |

**Wochentotal Aufwand:** ca. 6–8 Stunden (inkl. Claude-unterstützter Erstellung und Community-Präsenz). Die zusätzliche Zeit für Community-Antworten zahlt sich über fachliche Autorität und SEO-Sichtbarkeit aus, nicht über kurzfristige Klicks.

---

## 7. 6-Wochen-Redaktionsplan

### Woche 1 — KW 12: Setup & erste Signale

**LinkedIn Personal:**
- Di: *"Warum lehnen Steuerkanzleien Mandate ab?"* — Kapazitätsproblem, keine Lösung (Pillar 1)
- Do: *"OCR erkennt Buchstaben. LLM versteht Geschäftsvorfälle."* — Kernunterschied ohne Fachchinesisch (Pillar 2)

**LinkedIn Company:**
- Di: Repost CEO-Post (Di)
- Fr: Produktschaufenster — Belegeingang-Übersicht Screenshot

**Website:**
- Startseite live (oder finalisiert)
- Über uns / Gründer-Seite live
- LinkedIn Company Page erstellt und befüllt

---

### Woche 2 — KW 13: Inhaltsmaschine läuft

**LinkedIn Personal:**
- Di: *Behind the Scenes: Erste Beta-Kanzlei im Onboarding — was wir lernen* (Pillar 3)
- Do: *Fachkräftemangel: Warum Automatisierung nicht die Antwort ist, die Kanzleien erwarten* (Pillar 1)

**LinkedIn Company:**
- Di: Repost CEO-Post (Di)
- Fr: *"Von der Eingangsrechnung zum DATEV-Buchungsstapel — wie Flowbeaver den Schritt dazwischen übernimmt"*

**Website:**
- Produkt/Funktionen-Seite live
- Blog-Artikel 1 live: *"KI-Belegerkennung vs. OCR: Was Steuerkanzleien wirklich brauchen"*

---

### Woche 3 — KW 14: Vertrauen + Differenzierung

**LinkedIn Personal:**
- Di: *"Fremdsprachige Rechnungen — der unterschätzte Zeitfresser in der Kanzlei"* (Pillar 5)
- Do: *Waitlist-Update: X Kanzleien auf der Liste, noch Y Plätze offen* (Pillar 4)

**LinkedIn Company:**
- Di: Repost CEO-Post (Do) — Waitlist-Zahlen als Unternehmens-Signal
- Fr: Screenshot: Fremdsprachige Rechnung → deutschsprachiger Buchungsvorschlag

**Website:**
- Pricing-Seite live
- FAQ-Seite live

---

### Woche 4 — KW 15: Expertise vertiefen

**LinkedIn Personal:**
- Di: *"Was passiert, wenn das LLM die Rechnung nicht versteht? Unser Sicherheitsnetz."* (Pillar 2)
- Do: *Behind the Scenes: Welche Fehler wir in Woche 3 gemacht haben — und was wir geändert haben* (Pillar 3)

**LinkedIn Company:**
- Di: Repost CEO-Post (Di)
- Fr: FAQ-Snippet: *"Ist Flowbeaver mit DATEV Unternehmen Online kompatibel? Ja — hier wie."*

**Website:**
- Blog-Artikel 2 live: *"Finmatics vs. Flowbeaver: Was passt zu welcher Kanzlei?"*
- Lead-Magnet Checkliste optional live schalten

---

### Woche 5 — KW 16: Webinar-Ankündigung

**LinkedIn Personal:**
- Di: *Webinar-Ankündigung: "10 Beta-Plätze werden an diesem Abend vergeben — live, mit Demo"* (Pillar 4)
- Do: *Teaser: "Was ich live zeigen werde: Rechnung rein, DATEV-Export raus — in unter 60 Sekunden"* (Pillar 3)

**LinkedIn Company:**
- Di: Webinar-Ankündigung als formeller Company-Post (Datum, Uhrzeit, Registrierungslink)
- Fr: Repost CEO-Teaser (Do)

**Website:**
- Webinar-Registrierungsseite live
- Brevo Webinar-Einladungs-Sequenz aktiviert (Emails A–C)

---

### Woche 6 — KW 17: Webinar-Woche

**LinkedIn Personal:**
- Di: *Erinnerung: 3 Tage bis zum Webinar — Registrierung noch offen* (Pillar 4)
- Do (Webinar-Tag): *"Heute Abend, 18 Uhr. 10 Plätze. Danach Warteliste bis Kohorte 2."* (Pillar 4)

**LinkedIn Company:**
- Di: Webinar-Erinnerung Company-Post
- Nach Webinar: Rückblick-Post ("10 Plätze vergeben, Kohorte 2 ab [Datum]")

**Website:**
- Nach Webinar: Beta-Erfolgs-Banner / "Kohorte 1 voll — Kohorte 2 Warteliste"-Seite
- Blog-Artikel 3 (DATEV ASR vs. KI) vorbereiten

---

## 8. KPI-Dashboard

| Kanal | Metrik | Ziel nach 6 Wochen |
|---|---|---|
| Website | Organische Sitzungen (Blog) | 200–500 |
| Website | Waitlist-Conversion Rate | ≥ 5% |
| Website | Seiten live | 6 (Start, Produkt, Pricing, Über uns, Blog, FAQ) |
| LinkedIn Personal | Follower-Wachstum | +100–200 |
| LinkedIn Personal | Avg. Impressionen/Post | 500–1.500 |
| LinkedIn Personal | Profil-Aufrufe/Woche | steigend |
| LinkedIn Company | Follower | 50+ |
| LinkedIn Company | Impressionen/Post | 100–400 |
| E-Mail/Waitlist | Waitlist-Größe (Woche 4) | 80–150 |
| E-Mail/Waitlist | Waitlist-Größe (Woche 6, post-Webinar) | 150–300 |

---

## 9. Referenzen & verknüpfte Dokumente

| Dokument | Inhalt |
|---|---|
| `strategie/Kanalstrategie.md` | Kanalpriorisierung (Version 2.0), Community-Kanäle, Paid-Reality-Check |
| `strategie/GTM-Strategie.md` | 12-Wochen-Gesamtplan, Funnel-Übersicht |
| `strategie/Positionierung.md` | Messaging-Framework, Differenziator 1.1, Gründer-Positionierung 1.2, Dual-Track 6.4 |
| `strategie/Content-Framework.md` | Awareness-Stufen-Matrix, Hook-Bibliothek, Community-Antwort-Template |
| `strategie/Fachcommunitys-Anknuepfungspunkte.md` | 16 konkrete DATEV-Threads mit Antwortmustern, Hashtag-Liste, Multiplikatoren |
| `strategie/Session-Handoff-Website-Ueberarbeitung.md` | Website-Pflicht-Elemente, konkrete Community-Zitate, Tonalität |
| `strategie/STRATEGY.md` | Dual-Track-Daten (Ads 292,90 €/0 Conv.), Keyword-Volumen, Kampagnen A/B/C |
| `seo/content-plan.md` | Artikel-Backlog mit Status (Phasen 1–3) |
| `email/` | Brevo-Sequenzen Welcome + Webinar |
| `~/.claude/skills/flowbeaver-marketing/references/linkedin.md` | LinkedIn-Post-Formatregeln + Beispiele |
| `~/.claude/skills/flowbeaver-marketing/references/seo.md` | SEO-Artikel-Formatregeln + Strukturvorgaben |
