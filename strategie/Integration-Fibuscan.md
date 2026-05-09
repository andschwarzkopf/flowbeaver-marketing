# Integration: Flowbeaver → FIBUscan

**Stand:** 2026-05-06
**Status:** Recherche, noch nicht mit FIBUdata abgestimmt

## Use Case

Eine bestimmte Gruppe von Steuerkanzleien nutzt **FIBUscan als zentrales Buchhaltungssystem** und exportiert nicht weiter nach DATEV. Für diese Kanzleien ist FIBUscan die Endstation der Finanzbuchhaltung — DATEV-Formate spielen nur als Transport-Standard eine Rolle, nicht als Zielsystem.

Für Flowbeaver heißt das: Wir liefern Belege und Vorkontierung in einem Format, das FIBUscan importieren kann. Der Steuerberater bucht in FIBUscan zu Ende.

## Was FIBUscan importseitig akzeptiert

FIBUscan hat in der Steuerberater-Version ein **Berater-Portal** explizit für Drittsystem-Daten. Originalzitat aus der Doku: *"Unternehmen, deren Buchhaltung/Steuerberatung nicht mit FIBUscan arbeiten, wird hiermit ermöglicht, die erfassten und digitalisierten Belege vollständig und per Datenübertragung dem Beraterbüro zur Verfügung zu stellen."*

Drei Aufnahme-Modi sind möglich:
1. Nur Belegbilder
2. Nur Buchungsinformationen (kontiert oder unkontiert)
3. Beides kombiniert ← der für Flowbeaver relevante Fall

### Akzeptierte Formate

| Format | Belegbild dabei? | Eignung für Flowbeaver |
|---|---|---|
| DATEV KNE Vorlauf (ASCII) | Nur via "KNE mit PDF-Import" | Hoch — wenn wir KNE generieren |
| DATEV pro Vorlauf (XML/CSV) | Separat zu verlinken | Hoch — Flowbeaver-Standard-Output |
| Excel/CSV (frei mappbar) | Nein | Mittel — verliert Belegbild |
| ZUGFeRD / X-Rechnung | Ja (im Container) | Hoch für Eingangsrechnungen |
| PDF mit Importschablone | Ja, ist *das* Belegbild | Mittel — eher manuell |

**Wichtig:** Der reine CSV-Pfad transportiert keine Belegbilder. Wer Belegbilder mitschicken will, muss zwingend KNE-mit-PDF, ZUGFeRD oder den nativen PDF-Import nutzen.

## Lieferpfade für Flowbeaver

### Variante 1 — DATEV pro Vorlauf + separate PDFs
1. Flowbeaver erzeugt einen DATEV-pro-konformen Buchungsstapel (CSV, EXTF-Format).
2. Parallel werden die zugehörigen PDFs in einen Ordner mit der Belegnummer im Dateinamen exportiert.
3. Steuerberater importiert in FIBUscan über *Datei-Import → DATEV pro Vorlauf* die Buchungen und über *PDF-Import* die Belege. FIBUscan verknüpft per Belegnummer.

Vorteil: Flowbeaver-Standard-Output reicht aus.
Nachteil: Zwei Schritte beim Berater.

### Variante 2 — DATEV KNE + PDFs in einem Bundle
1. Flowbeaver erzeugt KNE-Vorlauf + PDFs in einem ZIP.
2. Steuerberater nutzt *DATEV KNE mit PDF-Import* — Buchung und Beleg landen in einem Schritt verknüpft.

Vorteil: Ein Klick beim Berater.
Nachteil: Wir müssen das alte KNE-ASCII-Format zusätzlich erzeugen; Mapping-Konvention für PDFs ist öffentlich nicht vollständig dokumentiert.

### Variante 3 — ZUGFeRD / X-Rechnung
1. Flowbeaver liefert eingehende E-Rechnungen direkt als ZUGFeRD- oder X-Rechnung-XML weiter.
2. FIBUscan importiert nativ — Belegbild und strukturierte Daten in einem Container, kein DATEV-Umweg.

Vorteil: Sauberster Weg für E-Rechnungen.
Nachteil: Nur für E-Rechnungen, deckt klassische PDFs/Papierbelege nicht ab.

## Bekannte Einschränkungen

- **Bank-Vorläufe** lassen sich laut FIBUscan-Doku **nicht** über die DATEV-XML-Schnittstelle importieren — dafür gibt es einen separaten DATEV-pro-Pfad.
- Beim DATEV-XML-Im/Export gelten zusätzliche Regeln zu Rechnungsnummern und Storno-Belegen, die Fehler werfen können.
- Reiner CSV-Import bringt keine Belegbilder mit.

## Offene Fragen an FIBUdata

Die öffentliche Doku ist beim PDF-Beleg-Mapping dünn. Vor einer echten Integration müssen wir bei FIBUdata abklären:

1. Genaue **Dateinamenskonvention** für die PDF-Zuordnung beim "KNE mit PDF-Import"
2. **Pflichtfelder** im DATEV-pro-Vorlauf, damit FIBUscan ihn ohne manuelles Mapping annimmt
3. Ob die **Beleglink-Schnittstelle (DATEV pro mit Beleglink über Fremdconnector)** auch eingangsseitig in der Berater-Version nutzbar ist
4. Ob es eine **API** für die Berater-Version gibt, um den Schritt "Datei in Download-Ordner ablegen + manuell importieren" zu automatisieren
5. Wie **Mehrwertsteuer-Schlüssel** beim Import behandelt werden — übernommen oder neu berechnet
6. Wie **Mandantenanlage** im Berater-Portal funktioniert, wenn Daten aus einem Drittsystem kommen

## Strategische Einordnung

Die Zielgruppe "Steuerkanzleien, die ausschließlich FIBUscan nutzen" ist klein, aber spitz. Diese Kanzleien haben sich bewusst **gegen** den DATEV-Standardpfad entschieden — typischerweise wegen Kosten, Komplexität oder Branchenspezialisierung (z. B. Agrar, kleine Online-Händler). Sie sind also nicht durch eine "DATEV-Ergänzung"-Story zu erreichen.

Für diese Kanzleien lautet das Versprechen anders:

> Flowbeaver liefert vorkontierte Belege direkt in Ihr FIBUscan-Berater-Portal. Sie buchen wie gewohnt in FIBUscan zu Ende — ohne, dass der Mandant FIBUscan einrichten oder bedienen muss.

Das ist kein Marketing-Argument für die breite Zielgruppe, sondern ein **Nischen-Vertriebsargument**: Wir können FIBUscan-Kanzleien gewinnen, die sonst keinen klaren Weg haben, Mandanten ohne FIBUscan-Lizenz sauber anzubinden.

**Marktabschätzung folgt** — FIBUscan-Nutzung ist in keiner öffentlichen Statistik separat ausgewiesen, müsste über FIBUdata-Workshops, Agrosoft-Partnerschaften und Branchen-Communitys geschätzt werden.

## Quellen

- [FIBUscan für Steuerberater](https://fibudata.net/fuer-steuerberater/) — Berater-Version, drei Aufnahme-Modi
- [Berater-Portal Doku](https://handbuch.fibuscan.de/module_8.htm) — Drittsystem-Datenübertragung
- [Modul Kunden — Import-Optionen](https://handbuch.fibuscan.de/module_4_12.htm) — Import-Wege
- [AR-Import per CSV/DATEV-Vorlauf](https://handbuch.fibuscan.de/module_4_12_3.htm) — Format-Details
- [DATEV XML-Schnittstelle](https://handbuch.fibuscan.de/module_7_8_5.htm) — Einschränkungen
- [DATEV pro mit Beleglink](https://handbuch.fibuscan.de/module_7_8_4.htm) — Fremdconnector
- [Versionshistorie FIBUscan](https://handbuch.fibuscan.de/module_7_3.htm) — aktuelle Stände
- [FIBUscan Produktseite](https://fibudata.net/fibuscan/) — Funktionsliste
