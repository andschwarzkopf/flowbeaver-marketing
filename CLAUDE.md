# Flowbeaver Marketing — Projektkontext

## Was ist Flowbeaver?
KI-Vorsystem für die vorbereitende Buchhaltung in Steuerkanzleien. Kombiniert LLM + KI-OCR + deterministische Regeln ("Dreiklang") für Belegextraktion, Zuordnung und Vorkontierung. Ergebnis: DATEV-kompatibler Buchungsstapel.

## Wichtigste Regeln
- Flowbeaver ist eine DATEV-**Ergänzung**, niemals eine DATEV-Alternative
- ICP: Wachstumsorientierte Steuerkanzleien mit ≥4 Mitarbeitern
- Sprache: Deutsch, "Sie"-Anrede, sachlich-selbstbewusst, keine Emojis
- Solo-Founder (Andreas Schwarzkopf) = Vorteil, nicht Schwäche — direkter Zugang, schnelle Iteration
- Kein Startup-Jargon: "Pioneer-Kohorte" → "erste Runde", "Disruption" → nicht verwenden

## Branchendaten (STAX 2024 — BStBK/Allensbach)
- Einzelkanzlei: Ø **4,5 Beschäftigte**, Umsatz 305.000 €, Gewinn 125.000 €
- Berufsausübungsgesellschaft (BÄG): Ø **24 Beschäftigte**, Umsatz 1.265.000 €
- **Personalkosten: 43,8 % vom Umsatz** (2018: 37 %) — massiver Anstieg
- **59,1 % offene Stellen in Einzelkanzleien nicht besetzt**, nur 23,2 % konnten alle Stellen besetzen
- Buchführung = 21–25 % des Kanzleiumsatzes — Kerngeschäft
- Digitale Buchführung nach Belegen: 54,8 % (Einzelkanzleien), KI-Chatbots: 12,2 %
- **Größte Digitalisierungshürden: organisatorischer Aufwand, innere Widerstände, mangelnde Zeit** (nicht Technik/Kosten)
- Trend zu Pauschalvergütungen (32,4 %, 2018: 13,5 %) → Effizienz = Margenhebel
- ICP-Einordnung: Flowbeaver-ICP (≥4 MA) = durchschnittliche bis große Einzelkanzleien + gesamtes BÄG-Segment

## Validierte Kunden-Insights
- **Rückfragen sind der größte Zeitkiller** — nicht das Abtippen. Teams verbringen Stunden mit Mandanten-Kommunikation wegen unklarer Geschäftsvorfälle und fremdsprachiger Belege.
- **Flowbeaver-Differenzierung:** LLM versteht jede Sprache und leitet aus exotischen Rechnungen klare Geschäftsvorfälle ab → weniger Rückfragen

---

## Ordnerstruktur

```
flowbeaver-marketing/
├── CLAUDE.md                          # Dieses Dokument
├── strategie/                         # Fundament — ändert sich selten
│   ├── GTM-Strategie.md
│   ├── Positionierung.md
│   ├── Kanalstrategie.md
│   ├── Preiskalkulation.md
│   └── Aktionsplan.md
├── paid-ads/                          # Google Ads — ändert sich wöchentlich
│   ├── inbox/                         # Neue Datenexporte hier ablegen
│   ├── archiv/YYYY-MM/               # Verarbeitete Exporte
│   ├── anzeigentexte/                 # Anzeigentext-Entwürfe
│   ├── MANIFEST.md                    # Log: was verarbeitet wurde
│   └── Keyword-Strategie.md           # Lebendes Dokument, datengetrieben
├── seo/                               # SEO Content-Produktion
│   ├── inbox/                         # GSC-Exporte, Ranking-Daten
│   ├── archiv/YYYY-MM/               # Verarbeitete Exporte
│   ├── artikel/                       # Blog-Artikel (Entwurf & fertig)
│   ├── MANIFEST.md                    # Log: was verarbeitet wurde
│   └── content-plan.md               # Artikel-Backlog mit Status
├── landingpages/                      # Alle Landingpage-Versionen
│   ├── landingpage-waitlist-v1.html
│   ├── landingpage-waitlist-v2.html
│   └── Landingpage-diskussion.md
├── webinare/                          # Webinar-Skripte und Materialien
├── linkedin/                          # LinkedIn-Post-Entwürfe
├── email/                             # E-Mail-Sequenzen (Welcome, Webinar-Einladung, Follow-up)
└── assets/                            # Bild-Prompts, visuelle Assets
    └── hero-trichter-prompt.md
```

---

## Daten-Workflow (Paid Ads & SEO)

### So funktioniert der Inbox/Manifest-Workflow:

1. **Daten ablegen:** CSV-Exporte aus Google Ads, GA4 oder Google Search Console in den jeweiligen `inbox/`-Ordner legen
2. **Analyse anstoßen:** z.B. "analysiere die neuen Ads-Daten" oder "neue SEO-Daten auswerten"
3. **Verarbeitung:** Claude liest `inbox/`, gleicht mit `MANIFEST.md` ab, analysiert neue Dateien
4. **Ergebnis:** Keyword-Strategie.md bzw. content-plan.md wird aktualisiert, Empfehlungen werden gegeben
5. **Archivierung:** Verarbeitete Dateien → `archiv/YYYY-MM/`, MANIFEST.md wird aktualisiert

### Wichtig:
- `MANIFEST.md` ist die Single Source of Truth dafür, was bereits verarbeitet wurde
- `paid-ads/Keyword-Strategie.md` ist das zentrale, lebende Strategie-Dokument für Keywords, Kampagnenstruktur und Empfehlungen
- `seo/content-plan.md` ist das Backlog für SEO-Artikel mit Status-Tracking

---

## Skills (in ~/.claude/skills/flowbeaver-marketing/)

### flowbeaver-marketing (Content-Erstellung)
- LinkedIn-Posts → `linkedin/`
- E-Mail-Sequenzen → `email/`
- Webinar-Skripte → `webinare/`
- Landingpage-Copy → `landingpages/`
- Referenzen: `references/linkedin.md`, `references/emails.md`, `references/landingpage.md`, `references/webinar.md`, `references/customer-insights.md`

### google-ads (Kampagnen-Analyse & Optimierung)
- Analysiert Datenexporte aus `paid-ads/inbox/`
- Aktualisiert `paid-ads/Keyword-Strategie.md`
- Erstellt Anzeigentexte, Negative-Keyword-Listen, Agentur-Briefings

### seo-content (SEO-Artikel)
- Schreibt Blog-Artikel gemäß `seo/content-plan.md`
- Folgt der Keyword-Strategie aus `paid-ads/Keyword-Strategie.md`
- Referenz: `references/seo.md`
