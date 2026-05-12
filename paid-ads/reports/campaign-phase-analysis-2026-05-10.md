# Kampagnen-Phasen-Analyse — Stand 2026-05-10

**Zeitraum:** 2024-01-01 bis 2026-05-10

## Kontext (fuer Claude-Chat-Analyse)

**Produkt:** Flowbeaver — KI-Vorsystem fuer die vorbereitende Buchhaltung in Steuerkanzleien. 
Kombination aus LLM, KI-OCR und deterministischen Regeln. Output: DATEV-kompatibler Buchungsstapel. 
Flowbeaver ist eine **DATEV-Ergaenzung**, niemals eine DATEV-Alternative.

**ICP:** Wachstumsorientierte Steuerkanzleien mit 4-10 Mitarbeitern. 
Validierter Insight: Rueckfragen mit Mandanten sind der groesste Zeitkiller (nicht das Abtippen). 
Flowbeaver-Differenzierung: LLM versteht jede Sprache und leitet aus exotischen Rechnungen klare Geschaeftsvorfaelle ab.

**Aktuelle Kampagnen-Regeln:** Nur Exact-Match Keywords, kein Display, kein PMax, 
Anzeigentexte muessen 'Steuerkanzlei' oder 'Kanzlei' enthalten.

## Methodik

Eine **Phase** = eine **Anzeigengruppe** innerhalb einer Kampagne. 
Phase-Zeitraum = vom ersten bis zum letzten Tag mit Impressions in dieser Anzeigengruppe.

**Final URLs** = alle URL-Versionen, die in der Phase aktiv waren (auch wenn ueber die Lebensdauer mehrere Anzeigen mit verschiedenen URLs liefen).

**GA4-Daten** sind gefiltert auf:
- `landingPage` (Pfad-only, exakte Uebereinstimmung)
- `sessionMedium = cpc` (also nur Paid-Search-Traffic)
- Phase-Zeitraum

**Limitation:** GA4-Bounce-Rate und Avg-Dauer sind Durchschnitt der Tagesbuckets, nicht echte Phase-Aggregate. Sessions/Users/Conversions/Pageviews sind Summen. 
Google-Ads-`change_event`-API ist auf 30 Tage Historie begrenzt — granulare Aenderungen vor April 2026 lassen sich nicht rekonstruieren.

---

## Kampagnen-Uebersicht

| Kampagne | Status | Channel | Spend | Impr | Klicks | CTR | Conv | CPA |
|---|---|---|---|---|---|---|---|---|
| [GSN] KI-Buchhaltung | PAUSED | SEARCH | 995,66 EUR | 5.508 | 269 | 4.88% | 5 | 199,13 EUR |
| [GSN] der-ki-check.de | PAUSED | SEARCH | 389,00 EUR | 2.989 | 96 | 3.21% | 0 | — |
| [GSN] KI-Belegerkennung Steuerkanzlei | PAUSED | SEARCH | 343,27 EUR | 275 | 23 | 8.36% | 1 | 343,27 EUR |
| [GDN] KI-Buchhaltung | PAUSED | DISPLAY | 121,70 EUR | 222.941 | 3.875 | 1.74% | 0 | — |
| [PMax] KI-Belegerfassung | PAUSED | PERFORMANCE_MAX | 79,65 EUR | 65.953 | 828 | 1.26% | 0 | — |

**Gesamt:** 1.929,28 EUR Spend, 297.666 Impressions, 5.091 Klicks, 6 Conversions

---

## Kampagne: [GSN] KI-Buchhaltung

- **Status:** PAUSED
- **Channel Type:** SEARCH
- **Aktiv (mit Impressions):** 2026-01-20 bis 2026-03-17
- **Total Spend:** 995,66 EUR
- **Impressions:** 5.508 / **Klicks:** 269 / **CTR:** 4.88% / **Avg CPC:** 3,70 EUR
- **Conversions:** 5 / **CPA:** 199,13 EUR

### Phase 1: Anzeigengruppe "KI-Buchhaltung -200126-"

- **Zeitraum:** 2026-01-20 bis 2026-03-17 (57 Tage)
- **Anzeigengruppen-Status:** ENABLED
- **Spend:** 995,66 EUR / Impr: 5.508 / Klicks: 269
- **CTR:** 4.88% / **Avg CPC:** 3,70 EUR
- **Conversions:** 5 / **CPA:** 199,13 EUR

#### Final URLs (1)

- `https://www.flowbeaver.de/early-partner`

#### Anzeigen (1)

**Ad-ID 793520949725** (RESPONSIVE_SEARCH_AD, Status: ENABLED)
- Aktiv: 2026-01-20 bis 2026-03-17
- Spend: 995,66 EUR / Impr: 5.508 / Klicks: 269 / CTR: 4.88% / Conv: 5
- **Headlines:**
  - Für vorbereitende Buchhaltung
  - {KeyWord:Eingangsrechnungen erfassen}
  - Rechnungseingang auf Autopilot
  - Belegerfassung automatisieren
  - Zeit und Ressourcen sparen
  - Flowbeaver: Early Access
  - Automatische Belegerfassung
  - Vorkontierung automatisch
  - Belegeingang automatisieren
  - Buchhaltung mit KI
  - {KeyWord:Belegerfassung per KI}
  - Early Partner werden
  - Jetzt Demo vereinbaren
  - Für Buchhaltungsdienstleister
  - Für große Belegaufkommen
- **Descriptions:**
  - Automatisieren Sie die Belegerfassung im Rechnungseingang mit künstlicher Intelligenz
  - KI-Automatisierung für Buchhaltungs-Dienstleister, die wirklich skalieren wollen
  - Ohne Prozess-Umstellung in Ihre FiBu. Leistungsfähige Datenerkennung für mehr Durchsatz
  - Mehr Umsatz ohne zusätzliche Mitarbeiter. Early Partner werden & dauerhaft profitieren
- **Ad-spezifische Final URLs:** https://www.flowbeaver.de/early-partner

#### Keywords (11)

| Keyword | Match | Status | Impr | Klicks | CTR | Avg CPC | Spend | Conv |
|---|---|---|---|---|---|---|---|---|
| buchhaltungsbüro software | PHRASE | PAUSED | 2.671 | 114 | 4,3% | 3,26 EUR | 371,45 EUR | 0 |
| rechnungseingang automatisieren | PHRASE | ENABLED | 802 | 34 | 4,2% | 4,32 EUR | 146,90 EUR | 0 |
| eingangsrechnungen automatisiert verarbeiten | PHRASE | ENABLED | 532 | 29 | 5,5% | 3,94 EUR | 114,31 EUR | 0 |
| ki belegerkennung | PHRASE | ENABLED | 461 | 31 | 6,7% | 4,18 EUR | 129,56 EUR | 4 |
| ki rechnungsprüfung | PHRASE | ENABLED | 379 | 34 | 9,0% | 3,91 EUR | 132,79 EUR | 1 |
| software für buchhaltungsservice | PHRASE | PAUSED | 359 | 10 | 2,8% | 3,27 EUR | 32,74 EUR | 0 |
| automatische kontierung | PHRASE | ENABLED | 172 | 8 | 4,7% | 3,57 EUR | 28,59 EUR | 0 |
| ki belegerfassung | PHRASE | ENABLED | 66 | 6 | 9,1% | 4,21 EUR | 25,27 EUR | 0 |
| mandantenfähige buchhaltungssoftware | PHRASE | ENABLED | 58 | 2 | 3,4% | 4,00 EUR | 8,01 EUR | 0 |
| buchhaltungsbüro software | EXACT | ENABLED | 4 | 1 | 25,0% | 6,03 EUR | 6,03 EUR | 0 |
| ki vorkontierung | PHRASE | ENABLED | 4 | 0 | 0,0% | 0,00 EUR | 0,00 EUR | 0 |

#### Top-Suchbegriffe (20 von 659)

| Suchbegriff | Impr | Klicks | CTR | Spend | Conv |
|---|---|---|---|---|---|
| nlb online | 45 | 0 | 0,0% | 0,00 EUR | 0 |
| datev unternehmen online kosten | 35 | 0 | 0,0% | 0,00 EUR | 0 |
| ki rechnungsprüfung | 34 | 4 | 11,8% | 15,61 EUR | 1 |
| lexware office | 23 | 0 | 0,0% | 0,00 EUR | 0 |
| datev kanzlei rechnungswesen | 22 | 0 | 0,0% | 0,00 EUR | 0 |
| was ist lexware | 18 | 5 | 27,8% | 12,89 EUR | 0 |
| addison programm | 17 | 0 | 0,0% | 0,00 EUR | 0 |
| addison buchhaltungsprogramm | 16 | 0 | 0,0% | 0,00 EUR | 0 |
| datev rechnungswesen | 14 | 0 | 0,0% | 0,00 EUR | 0 |
| pennylane datev | 14 | 0 | 0,0% | 0,00 EUR | 0 |
| buchhaltungssoftware | 12 | 0 | 0,0% | 0,00 EUR | 0 |
| ki buchhaltungssoftware | 11 | 0 | 0,0% | 0,00 EUR | 0 |
| primanota datev | 11 | 0 | 0,0% | 0,00 EUR | 0 |
| vereinsbuchhaltung software | 11 | 0 | 0,0% | 0,00 EUR | 0 |
| workflow rechnungseingang | 11 | 0 | 0,0% | 0,00 EUR | 0 |
| agenda digitales belegbuchen | 10 | 0 | 0,0% | 0,00 EUR | 0 |
| amondis software | 10 | 0 | 0,0% | 0,00 EUR | 0 |
| automatische rechnungsprüfung | 10 | 2 | 20,0% | 9,86 EUR | 0 |
| lexware belege erfassen | 10 | 3 | 30,0% | 7,98 EUR | 0 |
| kanzlei rechnungswesen datev | 9 | 0 | 0,0% | 0,00 EUR | 0 |

#### GA4 je Final-URL (Paid Search, Phase-Zeitraum)

| URL-Pfad | Sessions | Users | Bounce | Avg Dauer | Conversions | Pageviews |
|---|---|---|---|---|---|---|
| `/early-partner` | 360 | 338 | 73,3% | 14:09 | 7 | 442 |

#### Landingpage-Snippets (aktueller Stand)

**https://www.flowbeaver.de/early-partner**
- **Title:** Flowbeaver – Rechnungseingang auf Autopilot – Early Access
- **H1:** Early Partner Programm
- **Meta Description:** Automatisieren Sie die Belegerfassung im Rechnungseingang: Eingangsrechnungen automatisch erfassen und als buchbare Datensätze in Ihre Buchhaltung übergeben.
- **Preview:** Flowbeaver Flowbeaver Über uns Kontakt Redirect to URL: / KI-Automatisierung für Buchhaltungs-Dienstleister, die wirklich skalieren wollen ❌ Kein zeitraubendes Abtippen mehr ✅ 10x mehr Durchsatz ohne neue Mitarbeiter Flowbeaver automatisiert bis zu 90 % der Belegerfassung und Vorkontierung – in Ihrer FiBu Sehen Sie, wie 10 Minuten Arbeit in 10 Sekunden verschwinden Keine OCR-Fehler mehr. Keine man

---

## Kampagne: [GSN] der-ki-check.de

- **Status:** PAUSED
- **Channel Type:** SEARCH
- **Aktiv (mit Impressions):** 2025-10-02 bis 2025-10-21
- **Total Spend:** 389,00 EUR
- **Impressions:** 2.989 / **Klicks:** 96 / **CTR:** 3.21% / **Avg CPC:** 4,05 EUR
- **Conversions:** 0 / **CPA:** —

### Phase 1: Anzeigengruppe "KI-Check -031025-"

- **Zeitraum:** 2025-10-02 bis 2025-10-21 (20 Tage)
- **Anzeigengruppen-Status:** ENABLED
- **Spend:** 389,00 EUR / Impr: 2.989 / Klicks: 96
- **CTR:** 3.21% / **Avg CPC:** 4,05 EUR
- **Conversions:** 0 / **CPA:** —

#### Final URLs (1)

- `https://www.der-ki-check.de`

#### Anzeigen (2)

**Ad-ID 776964378382** (RESPONSIVE_SEARCH_AD, Status: ENABLED)
- Aktiv: 2025-10-02 bis 2025-10-21
- Spend: 138,74 EUR / Impr: 1.834 / Klicks: 33 / CTR: 1.80% / Conv: 0
- **Headlines:**
  - KI erfolgreich einführen
  - KI-Check für Unternehmen
  - Gratisanalyse, Ergebnis sofort
  - Check hier starten
  - Jetzt Potential prüfen
  - Nicht den Anschluss verlieren
  - Status, Chancen & Empfehlungen
  - KI-Readiness-Check für Firmen
  - Ergebnis in 5 Minuten
- **Descriptions:**
  - Der kostenlose KI-Check zeigt Ihre Chancen, Risiken und schlägt nächste Schritte vor
  - KI in Ihr Unternehmen einführen. Hier in 5 Minuten aktuellen Stand & KI-Chancen bewerten
  - Kostenloser KI-Readiness-Check. Keine Unternehmensdaten erforderlich. Ergebnis sofort
  - Analyse für Mitarbeiter-Befähigung, Vorzeigeprojekte, interne Effizienz, Marktchancen.
- **Ad-spezifische Final URLs:** https://www.der-ki-check.de

**Ad-ID 777066611471** (RESPONSIVE_SEARCH_AD, Status: ENABLED)
- Aktiv: 2025-10-02 bis 2025-10-21
- Spend: 250,26 EUR / Impr: 1.155 / Klicks: 63 / CTR: 5.45% / Conv: 0
- **Headlines:**
  - Gratis KI-Check für Firmen
  - KI-Potenziale entdecken
  - In 5 Minuten zum Report
  - Ihr KI-Potenzial sofort
  - Künstliche Intelligenz nutzen
  - Wettbewerbsvorteil durch KI
  - Digital fit in die Zukunft
  - KI für Unternehmen
  - KI-Einsatz prüfen
  - Jetzt KI-Strategie starten
- **Descriptions:**
  - Machen Sie den kostenlosen KI-Check und erhalten Sie Ihren individuellen Report
  - Entdecken Sie sofort das KI-Potenzial Ihres Unternehmens – schnell, einfach, kostenlos
  - Nur 5 Minuten: Antworten geben, Report erhalten, Vorteile sichern
  - KI-Check für klare Handlungsempfehlungen für Effizienz, Projekte und Marktchancen
- **Ad-spezifische Final URLs:** https://www.der-ki-check.de

#### Keywords (12)

| Keyword | Match | Status | Impr | Klicks | CTR | Avg CPC | Spend | Conv |
|---|---|---|---|---|---|---|---|---|
| ki beratung | PHRASE | ENABLED | 1.855 | 37 | 2,0% | 4,32 EUR | 159,67 EUR | 0 |
| ki beratung für unternehmen | PHRASE | ENABLED | 413 | 4 | 1,0% | 4,41 EUR | 17,65 EUR | 0 |
| ki check kostenlos | EXACT | ENABLED | 314 | 44 | 14,0% | 3,82 EUR | 168,06 EUR | 0 |
| ki readiness check | EXACT | ENABLED | 172 | 3 | 1,7% | 4,38 EUR | 13,15 EUR | 0 |
| ki beratung | EXACT | ENABLED | 163 | 6 | 3,7% | 4,14 EUR | 24,82 EUR | 0 |
| ki beratung kmu | EXACT | ENABLED | 29 | 0 | 0,0% | 0,00 EUR | 0,00 EUR | 0 |
| KI assessment | EXACT | PAUSED | 23 | 1 | 4,3% | 2,03 EUR | 2,03 EUR | 0 |
| künstliche intelligenz beratung | EXACT | ENABLED | 8 | 1 | 12,5% | 3,62 EUR | 3,62 EUR | 0 |
| ki beratung mittelstand | EXACT | ENABLED | 4 | 0 | 0,0% | 0,00 EUR | 0,00 EUR | 0 |
| ki beratung berlin | EXACT | ENABLED | 4 | 0 | 0,0% | 0,00 EUR | 0,00 EUR | 0 |
| ki beratungsunternehmen | EXACT | ENABLED | 2 | 0 | 0,0% | 0,00 EUR | 0,00 EUR | 0 |
| ki check unternehmen | EXACT | ENABLED | 2 | 0 | 0,0% | 0,00 EUR | 0,00 EUR | 0 |

#### Top-Suchbegriffe (20 von 155)

| Suchbegriff | Impr | Klicks | CTR | Spend | Conv |
|---|---|---|---|---|---|
| ki beratung | 82 | 3 | 3,7% | 11,88 EUR | 0 |
| ki check | 58 | 4 | 6,9% | 16,55 EUR | 0 |
| ki readiness | 45 | 0 | 0,0% | 0,00 EUR | 0 |
| ki readiness check | 41 | 2 | 4,9% | 8,50 EUR | 0 |
| ki berater | 30 | 0 | 0,0% | 0,00 EUR | 0 |
| ai consultant | 25 | 1 | 4,0% | 4,51 EUR | 0 |
| ki beratung hamburg | 20 | 1 | 5,0% | 4,78 EUR | 0 |
| ki beratung münchen | 18 | 0 | 0,0% | 0,00 EUR | 0 |
| ki automatisierung agentur | 16 | 0 | 0,0% | 0,00 EUR | 0 |
| ki für kmu | 16 | 0 | 0,0% | 0,00 EUR | 0 |
| ki agentur münchen | 15 | 0 | 0,0% | 0,00 EUR | 0 |
| ki consulting | 15 | 2 | 13,3% | 8,03 EUR | 0 |
| ki tester | 15 | 3 | 20,0% | 12,79 EUR | 0 |
| ki prüfung kostenlos | 13 | 1 | 7,7% | 4,92 EUR | 0 |
| ki test kostenlos | 13 | 0 | 0,0% | 0,00 EUR | 0 |
| ki test | 11 | 1 | 9,1% | 2,03 EUR | 0 |
| ki beratung stuttgart | 10 | 0 | 0,0% | 0,00 EUR | 0 |
| ki check kostenlos | 10 | 2 | 20,0% | 6,31 EUR | 0 |
| ki erkennung kostenlos | 10 | 1 | 10,0% | 3,90 EUR | 0 |
| ki beratung deutschland | 8 | 0 | 0,0% | 0,00 EUR | 0 |

#### GA4 je Final-URL (Paid Search, Phase-Zeitraum)

| URL-Pfad | Sessions | Users | Bounce | Avg Dauer | Conversions | Pageviews |
|---|---|---|---|---|---|---|
| `/` | 0 | 0 | 0,0% | 0:00 | 0 | 0 |

#### Landingpage-Snippets (aktueller Stand)

**https://www.der-ki-check.de**
- Status: HTTPSConnectionPool(host='www.der-ki-check.de', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLError(1, '[SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] ssl/tls alert handshake failure (_ssl.c:1016)')))

---

## Kampagne: [GSN] KI-Belegerkennung Steuerkanzlei

- **Status:** PAUSED
- **Channel Type:** SEARCH
- **Aktiv (mit Impressions):** 2026-03-17 bis 2026-04-20
- **Total Spend:** 343,27 EUR
- **Impressions:** 275 / **Klicks:** 23 / **CTR:** 8.36% / **Avg CPC:** 14,92 EUR
- **Conversions:** 1 / **CPA:** 343,27 EUR

### Phase 1: Anzeigengruppe "KI-Kern (höchste Priorität)"

- **Zeitraum:** 2026-03-17 bis 2026-04-20 (35 Tage)
- **Anzeigengruppen-Status:** ENABLED
- **Spend:** 294,86 EUR / Impr: 265 / Klicks: 20
- **CTR:** 7.55% / **Avg CPC:** 14,74 EUR
- **Conversions:** 0 / **CPA:** —

#### Final URLs (1)

- `https://www.flowbeaver.de/ki-belegerkennung`

#### Anzeigen (1)

**Ad-ID 800615890280** (RESPONSIVE_SEARCH_AD, Status: ENABLED)
- Aktiv: 2026-03-17 bis 2026-04-20
- Spend: 294,86 EUR / Impr: 265 / Klicks: 20 / CTR: 7.55% / Conv: 0
- **Headlines:**
  - {KeyWord:KI-Belegerkennung}
  - Speziell für Steuerkanzleien
  - Kostenlose Demo anfragen
  - DATEV-kompatib. Buchungsstapel
  - Automatische Vorkontierung
  - Mandanten-Belege per KI prüfen
  - Automatische Belegerfassung
  - Geld-zurück-Garantie
  - Belege mit KI erfassen
  - Buchungsvorschläge mit KI
  - Für Buchhaltungsdienstleister
  - KI für Steuerkanzleien
  - Belegerfassung automatisieren
  - Rechnungsprüfung automatisch
  - Flatrate. Monatlich kündbar.
- **Descriptions:**
  - Automatische Belegerfassung für Kanzleien. KI-basierte Kontierung & DATEV-Export
  - KI-gestützte Lösung für Steuerkanzleien, die die Belegerfassung automatisieren wollen
  - Spart Steuerkanzleien Zeit und Ressourcen. Kein Risiko, dank Geld-zurück-Garantie
  - DATEV-kompatibler Buchungsstapel per KI. Mandantenbelege automatisch vorkontieren
- **Ad-spezifische Final URLs:** https://www.flowbeaver.de/ki-belegerkennung

#### Keywords (4)

| Keyword | Match | Status | Impr | Klicks | CTR | Avg CPC | Spend | Conv |
|---|---|---|---|---|---|---|---|---|
| ki rechnungsprüfung | EXACT | ENABLED | 187 | 14 | 7,5% | 16,27 EUR | 227,72 EUR | 0 |
| ki belegerfassung | EXACT | ENABLED | 41 | 3 | 7,3% | 13,33 EUR | 40,00 EUR | 0 |
| ki belegerkennung | EXACT | ENABLED | 35 | 2 | 5,7% | 10,48 EUR | 20,97 EUR | 0 |
| ki vorkontierung | EXACT | ENABLED | 2 | 1 | 50,0% | 6,17 EUR | 6,17 EUR | 0 |

#### Top-Suchbegriffe (5 von 5)

| Suchbegriff | Impr | Klicks | CTR | Spend | Conv |
|---|---|---|---|---|---|
| ki rechnungsprüfung | 32 | 3 | 9,4% | 36,52 EUR | 0 |
| rechnungsprüfung mit ki | 17 | 0 | 0,0% | 0,00 EUR | 0 |
| ki belegerkennung | 7 | 1 | 14,3% | 9,67 EUR | 0 |
| ki rechnungserfassung | 2 | 0 | 0,0% | 0,00 EUR | 0 |
| belegerkennung | 1 | 0 | 0,0% | 0,00 EUR | 0 |

#### GA4 je Final-URL (Paid Search, Phase-Zeitraum)

| URL-Pfad | Sessions | Users | Bounce | Avg Dauer | Conversions | Pageviews |
|---|---|---|---|---|---|---|
| `/ki-belegerkennung` | 15 | 13 | 26,7% | 26:26 | 2 | 52 |

#### Landingpage-Snippets (aktueller Stand)

**https://www.flowbeaver.de/ki-belegerkennung**
- **Title:** KI-Belegerkennung für Steuerkanzleien | Flowbeaver
- **H1:** KI-Belegerkennung für Steuerkanzleien
- **Meta Description:** Mandantenbelege automatisch erfassen mit KI. Belegerfassung, Kontierung, DATEV-Export — für Steuerkanzleien. Nur 10 Plätze in der ersten Runde.
- **Preview:** Flowbeaver Flowbeaver Über uns Kontakt KI-Belegerkennung für Steuerkanzleien ✅ Belegerfassung automatisieren ✅ Automatische Kontierung ✅ DATEV-kompatibler Buchungsstapel Flowbeaver erkennt Belege, leitet die Geschäftsvorfälle ab und liefert fertige Buchungsvorschläge. Ihr Team prüft und importiert. Das ist alles. -- 15-Minuten-Demo mit dem Gründer. Persönlich, nicht automatisiert. -- Kostenlose De

### Phase 2: Anzeigengruppe "Wettbewerber-Vergleich"

- **Zeitraum:** 2026-03-22 bis 2026-04-17 (27 Tage)
- **Anzeigengruppen-Status:** ENABLED
- **Spend:** 48,41 EUR / Impr: 10 / Klicks: 3
- **CTR:** 30.00% / **Avg CPC:** 16,14 EUR
- **Conversions:** 1 / **CPA:** 48,41 EUR

#### Final URLs (1)

- `https://www.flowbeaver.de/ki-belegerkennung`

#### Anzeigen (1)

**Ad-ID 800541722085** (RESPONSIVE_SEARCH_AD, Status: ENABLED)
- Aktiv: 2026-03-22 bis 2026-04-17
- Spend: 48,41 EUR / Impr: 10 / Klicks: 3 / CTR: 30.00% / Conv: 1
- **Headlines:**
  - {KeyWord:KI-Belegerkennung}
  - Speziell für Steuerkanzleien
  - Jetzt Demo anfragen
  - DATEV-kompatib. Buchungsstapel
  - Automatische Vorkontierung
  - Mandanten-Belege per KI prüfen
  - Automatische Belegerfassung
  - Effizienz steigern
  - Belege mit KI erfassen
  - Buchungsvorschläge mit KI
  - Für Buchhaltungsdienstleister
  - KI für Steuerkanzleien
  - Belegerfassung automatisieren
  - Rechnungsprüfung automatisch
  - Flatrate. Monatlich kündbar
- **Descriptions:**
  - Automatische Belegerfassung für Kanzleien. KI-basierte Kontierung & DATEV-Export
  - KI-gestützte Lösung für Steuerkanzleien, die die Belegerfassung automatisieren wollen
  - Spart Steuerkanzleien Zeit und Ressourcen. Kein Risiko, dank Geld-zurück-Garantie
  - DATEV-kompatibler Buchungsstapel per KI. Mandantenbelege automatisch vorkontieren
- **Ad-spezifische Final URLs:** https://www.flowbeaver.de/ki-belegerkennung

#### Keywords (1)

| Keyword | Match | Status | Impr | Klicks | CTR | Avg CPC | Spend | Conv |
|---|---|---|---|---|---|---|---|---|
| finmatics alternative | EXACT | ENABLED | 10 | 3 | 30,0% | 16,14 EUR | 48,41 EUR | 1 |

#### GA4 je Final-URL (Paid Search, Phase-Zeitraum)

| URL-Pfad | Sessions | Users | Bounce | Avg Dauer | Conversions | Pageviews |
|---|---|---|---|---|---|---|
| `/ki-belegerkennung` | 9 | 9 | 22,2% | 0:40 | 1 | 12 |

#### Landingpage-Snippets (aktueller Stand)

**https://www.flowbeaver.de/ki-belegerkennung**
- **Title:** KI-Belegerkennung für Steuerkanzleien | Flowbeaver
- **H1:** KI-Belegerkennung für Steuerkanzleien
- **Meta Description:** Mandantenbelege automatisch erfassen mit KI. Belegerfassung, Kontierung, DATEV-Export — für Steuerkanzleien. Nur 10 Plätze in der ersten Runde.
- **Preview:** Flowbeaver Flowbeaver Über uns Kontakt KI-Belegerkennung für Steuerkanzleien ✅ Belegerfassung automatisieren ✅ Automatische Kontierung ✅ DATEV-kompatibler Buchungsstapel Flowbeaver erkennt Belege, leitet die Geschäftsvorfälle ab und liefert fertige Buchungsvorschläge. Ihr Team prüft und importiert. Das ist alles. -- 15-Minuten-Demo mit dem Gründer. Persönlich, nicht automatisiert. -- Kostenlose De

---

## Kampagne: [GDN] KI-Buchhaltung

- **Status:** PAUSED
- **Channel Type:** DISPLAY
- **Aktiv (mit Impressions):** 2026-01-20 bis 2026-02-25
- **Total Spend:** 121,70 EUR
- **Impressions:** 222.941 / **Klicks:** 3.875 / **CTR:** 1.74% / **Avg CPC:** 0,03 EUR
- **Conversions:** 0 / **CPA:** —

### Phase 1: Anzeigengruppe "KI-Buchhaltung [Placement-Nutzer] -200116-"

- **Zeitraum:** 2026-01-20 bis 2026-02-25 (37 Tage)
- **Anzeigengruppen-Status:** ENABLED
- **Spend:** 121,70 EUR / Impr: 222.941 / Klicks: 3.875
- **CTR:** 1.74% / **Avg CPC:** 0,03 EUR
- **Conversions:** 0 / **CPA:** —

#### Final URLs (1)

- `https://www.flowbeaver.de/early-partner`

#### Anzeigen (1)

**Ad-ID 792720758304** (RESPONSIVE_DISPLAY_AD, Status: ENABLED)
- Aktiv: 2026-01-20 bis 2026-02-25
- Spend: 121,70 EUR / Impr: 222.941 / Klicks: 3.875 / CTR: 1.74% / Conv: 0
- **Ad-spezifische Final URLs:** https://www.flowbeaver.de/early-partner

#### GA4 je Final-URL (Paid Search, Phase-Zeitraum)

| URL-Pfad | Sessions | Users | Bounce | Avg Dauer | Conversions | Pageviews |
|---|---|---|---|---|---|---|
| `/early-partner` | 299 | 280 | 76,9% | 14:22 | 1 | 366 |

#### Landingpage-Snippets (aktueller Stand)

**https://www.flowbeaver.de/early-partner**
- **Title:** Flowbeaver – Rechnungseingang auf Autopilot – Early Access
- **H1:** Early Partner Programm
- **Meta Description:** Automatisieren Sie die Belegerfassung im Rechnungseingang: Eingangsrechnungen automatisch erfassen und als buchbare Datensätze in Ihre Buchhaltung übergeben.
- **Preview:** Flowbeaver Flowbeaver Über uns Kontakt Redirect to URL: / KI-Automatisierung für Buchhaltungs-Dienstleister, die wirklich skalieren wollen ❌ Kein zeitraubendes Abtippen mehr ✅ 10x mehr Durchsatz ohne neue Mitarbeiter Flowbeaver automatisiert bis zu 90 % der Belegerfassung und Vorkontierung – in Ihrer FiBu Sehen Sie, wie 10 Minuten Arbeit in 10 Sekunden verschwinden Keine OCR-Fehler mehr. Keine man

---

## Kampagne: [PMax] KI-Belegerfassung

- **Status:** PAUSED
- **Channel Type:** PERFORMANCE_MAX
- **Aktiv (mit Impressions):** 2026-02-25 bis 2026-03-18
- **Total Spend:** 79,65 EUR
- **Impressions:** 65.953 / **Klicks:** 828 / **CTR:** 1.26% / **Avg CPC:** 0,10 EUR
- **Conversions:** 0 / **CPA:** —

_Keine Anzeigen-Aktivitaet in dieser Kampagne._

---
