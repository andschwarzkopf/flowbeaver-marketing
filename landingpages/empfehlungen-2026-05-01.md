# Website-Empfehlungen flowbeaver.de — 2026-05-01

Quelle: Live-Audit der Seite (Desktop + Mobile, Playwright) am 2026-05-01.
Gesamtnote: 8 / 10. Homepage stark, Schwächen v. a. in Sub-Pages, Mobile-Tabelle und CTA-Erwartung.

---

## Severity-Übersicht

| Nr. | Bereich | Severity | Aufwand |
|-----|---------|----------|---------|
| 1 | `/about` neu schreiben | KRITISCH | hoch |
| 2 | Demo-CTA: Erwartungslücke schließen | KRITISCH | mittel |
| 3 | Vergleichs-Tabelle Mobile | HOCH | niedrig |
| 4 | Branchenreport-Position im Funnel | HOCH | niedrig |
| 5 | Sparrechner-Ergebnis ohne CTA | MITTEL | niedrig |
| 6 | `/kontakt`-Sprache + Button | MITTEL | niedrig |
| 7 | "Schmerzen" → "Engpässe" | MITTEL | niedrig |
| 8 | "AKTUELLER EINFÜHRUNGSPREIS"-Stil | MITTEL | niedrig |
| 9 | Trust-Erweiterung (Demo-Loop, LinkedIn) | NIEDRIG | mittel |
| 10 | Footer ausbauen | NIEDRIG | niedrig |

---

## 1. KRITISCH — `/about`-Seite komplett neu schreiben

**Problem.** Die About-Seite zerstört die Marken-Story, die die Homepage aufgebaut hat. Drei Bruchstellen:

- **Solo-Founder-Inkonsistenz:** Homepage verkauft "Direkt mit dem Gründer" und "die ich persönlich einarbeite" (Singular). `/about` führt **Lilia Koch und Andreas Schwarzkopf als Mitgründer** auf. Wer beide Seiten liest, fragt sich: Was stimmt?
- **Sprache out-of-brand:** "Wir gestalten Ihre Zukunft in der Ära der KI", "Brücke zwischen Mensch und Maschine", "Wir nehmen Ängste, schaffen Klarheit und verwandeln Wandel in einen strategischen Vorteil", "Auf Augenhöhe / Praxisorientiert / Menschenzentriert" — komplett Beratungs-/Schulungs-Agentur-Sprech, gegen CLAUDE.md-Brand-Liste.
- **Falscher Produkt-Frame:** Sektion stammt aus einem KI-Berater-Template, nicht aus Flowbeaver-dem-Vorsystem.
- **Visueller Defekt:** Riesige weiße Lücke zwischen Sektionen.
- **Title-Tag:** "Über uns | Flowbeaver AI" — Brand heißt "Flowbeaver", nicht "Flowbeaver AI".

**Maßnahme.**
- Eine Seite, ein Founder, eine Sache: Warum Andreas Flowbeaver gebaut hat (vorbereitende Buchhaltung, KI-Erfahrung, Kanzleien-Realität).
- Lilia entweder ganz raus oder klar als operative Mitstreiterin (kein Co-Founder-Frame).
- Sprache an Homepage angleichen: sachlich, "Sie", keine Buzzwords aus der CLAUDE.md-Sperrliste.
- Title-Tag korrigieren: "Über uns | Flowbeaver".
- Whitespace-Lücke fixen.

**Akzeptanzkriterium.** Wer Homepage → About klickt, erlebt keinen Tonalitäts- oder Storybruch.

---

## 2. KRITISCH — CTA "Demo buchen (15 Min.)" hält nicht, was sie verspricht

**Problem.** Klick auf "Demo buchen" öffnet ein **Lead-Form** (Vorname/Nachname/E-Mail), keinen Kalender. Popup-Headline verspricht "15 Minuten, 1:1, direkt mit dem Gründer" — User erwartet Slot-Auswahl, bekommt "wir melden uns". Erwartungs-Realitäts-Lücke an genau dem Conversion-Engpass.

**Maßnahme — eine von zwei Varianten:**

**Variante A (empfohlen): Cal.com / Calendly einbetten.**
- 15-Min-Slots direkt buchbar.
- Form-Felder im Cal.com: Vorname, Nachname, E-Mail, Kanzleigröße (optional als Pre-Qualifier).
- Vorteil: Kein Medienbruch, sofortige Bestätigung.

**Variante B (falls Vorqualifizierung gewollt): CTA-Wording ehrlicher.**
- Button-Text: "Demo anfragen (15 Min.)" statt "Demo buchen".
- Popup-Heading: zusätzlicher Erwartungssatz: "Sie bekommen innerhalb von 1 Werktag Terminvorschläge per E-Mail."

**Akzeptanzkriterium.** Was der Button verspricht, ist auch das, was der nächste Schritt einlöst.

---

## 3. HOCH — Vergleichs-Tabelle auf Mobile reparieren

**Problem.** Die Tabelle "Klassische Belegverarbeitung vs. Flowbeaver KI-Pipeline" ist auf Mobile 780 px breit bei 390 px Viewport, scrollt horizontal — aber **ohne Scroll-Hinweis**. Kein Edge-Shadow, kein "← swipen →"-Hint. Viele User glauben, die rechte Spalte fehle schlicht.

**Maßnahme — eine von zwei:**
- **Option A:** Edge-Shadow / Fade rechts + dezenter "→ swipen"-Hinweis unter der Tabelle.
- **Option B (besser):** Mobile-Variante als **gestapelte Vergleichskarten**: Pro Funktion eine Karte mit "Klassisch ✗ / Flowbeaver ✓". Keine horizontale Scroll-Mechanik.

**Akzeptanzkriterium.** Mobile-User sieht ohne Aktion sofort, dass beide Spalten existieren und worin sie sich unterscheiden.

---

## 4. HOCH — Branchenreport im Funnel nach vorn ziehen

**Problem.** Aktuelle Reihenfolge: Pricing → Founder → Branchenreport → Final-CTA. Der Report ist ein **Top-of-Funnel-Asset** (E-Mail gegen Wert) und steht zwischen zwei Bottom-of-Funnel-Steps. Hand-Raiser, die noch nicht demo-reif sind, gehen verloren.

**Maßnahme.** Branchenreport-Sektion direkt nach "Drei Zahlen, die den Druck erklären" einbauen. Anker-Link zum Report dort, wo aktuell "jetzt herunterladen" steht — der Report soll dann tatsächlich gleich danach kommen. Demo-Klicker und Report-Downloader sind unterschiedliche Personas; nicht am Ende stapeln.

**Akzeptanzkriterium.** Besucher, die nicht demo-reif sind, finden den Report bevor sie an der Pricing-Card vorbeiscrollen.

---

## 5. MITTEL — Sparrechner-Ergebnis ohne Anschluss-CTA

**Problem.** Nach Klick auf "Ersparnis berechnen" erscheint "3.181 Euro / Monat netto" — und dann nichts. Der nächste Demo-CTA steht erst hinter der Pricing-Card. Die emotionale Hochphase wird nicht abgefangen.

**Maßnahme.** Direkt im Ergebnis-Block einen sekundären CTA: "Diese Zahl in der 15-Minuten-Demo gegen Ihre Belege rechnen" → Demo-Popup.

**Akzeptanzkriterium.** Ergebnis-Block hat eigenen CTA, der das Aha-Moment nicht verwaisen lässt.

---

## 6. MITTEL — `/kontakt`-Seite vom Tilda-Default lösen

**Problem.**
- "Wir lieben es, mit unseren Kunden zu kommunizieren" — Tilda-Floskel, bricht das Sprachregister.
- Button "absenden" kleingeschrieben.
- Keine Brücke zur Demo (viele klicken zuerst "Kontakt").

**Maßnahme.**
- Headline-Subline ersetzen, z. B.: "Schreiben Sie uns. Sie erreichen Andreas direkt."
- Button: "Absenden" (Großschreibung, konsistent mit Homepage-CTAs).
- Sekundärer CTA: "Lieber direkt eine 15-Min-Demo? → [Demo buchen]".

**Akzeptanzkriterium.** Kontakt-Seite klingt wie die Homepage, nicht wie eine Tilda-Vorlage.

---

## 7. MITTEL — "Schmerzen" → "Engpässe"

**Problem.** Headline "Gebaut von jemandem, der Ihre Schmerzen kennt" verwendet Gründer-/Marketing-Vokabel. Steuerberater sprechen nicht von "Schmerzen". Die Lage-Section verwendet bereits den präziseren Begriff "Engpässe".

**Maßnahme.** Headline angleichen: **"Gebaut von jemandem, der diese Engpässe kennt"**. Konsistent zum Lage-Frame und sachlicher.

**Akzeptanzkriterium.** Begriffslandschaft (Engpässe, Reibungen, Lastspitzen) ist über die Seite konsistent.

---

## 8. MITTEL — "AKTUELLER EINFÜHRUNGSPREIS" entdramatisieren

**Problem.** Allcaps + Sperrschrift wirkt wie Sale-Banner, hebt sich aus dem Sachstil heraus.

**Maßnahme.** Normale Kapitalisierung, kleinformatige Caption: "Einführungspreis — gilt dauerhaft für die ersten zehn Kanzleien."

**Akzeptanzkriterium.** Pricing-Card wirkt nicht wie Webshop-Promo, sondern wie sachliches Angebot.

---

## 9. NIEDRIG — Trust gezielt erweitern

Das Solo-Founder-/erste-zehn-Kanzleien-Frame verbietet Fake-Social-Proof. Aber zwei sichere Hebel:

- **6-Sekunden-Produkt-Loop im Hero:** "Beleg rein → Vorschlag raus" als kurze Animation/MP4 statt statischem Macbook-Mockup. Konkretes Beleg-Beispiel (z. B. das polnische Bauleistungs-Beispiel aus dem Belegdurchlauf) zeigen.
- **LinkedIn-Verweis** auf Andreas im Founder-Block und Footer. Solo-Founder-Story braucht ein verifizierbares Gesicht außerhalb der Webseite.

Was bewusst **nicht** rein soll: Logo-Leisten "Bekannt aus", Fake-Beratergremien, Stockfoto-Berufsträger.

---

## 10. NIEDRIG — Footer als zweites Conversion-Netz

**Problem.** Footer hat nur Copyright + Pflichtlinks. Scroller, die unten landen, fallen leer aus.

**Maßnahme.**
- E-Mail (`info@flowbeaver.de`) und Telefon (+49 30 20169735) im Footer.
- LinkedIn-Link Andreas / Flowbeaver.
- Mini-CTA: "15-Min-Demo → [Demo buchen]".
- Optional: Newsletter-Hinweis, falls Branchenreport als regelmäßiger Funnel geplant ist.

**Akzeptanzkriterium.** Footer fängt Scroll-zu-Ende-User ab statt sie zu verabschieden.

---

## Was beibehalten werden muss

- Hero-Wortlaut und Subline ("Ohne neue Software. Ohne Umstellung bestehender Prozesse.") — stärkste Stelle der Seite.
- 3-Engpass-Framing und parallele Lösungs-Bullets.
- Polnischer-Subunternehmer-Belegdurchlauf — sehr konkretes Wedge-Beispiel.
- DATEV-Ergänzungs-Positionierung (mehrfach, exakt richtig).
- Datenschutz-Sektion (§203 StGB, §62a StBerG, Hetzner, EU AI Act, kein US-Hyperscaler).
- 30-Tage-Rückerstattung + monatlich kündbar.
- FAQ-Block — Antworten sind ehrlich und scharf, nicht weichgespült.
- Brand-Visualität: Lila #52267a, Mint-Akzente, ruhige Typo.

---

## Technischer Befund

- Console: 0 Fehler, 0 Warnings.
- SEO-Basics sauber: H1 (1×), Meta-Description, OG-Image, Canonical, `lang="de"`, Viewport.
- Keine Network-Issues.
