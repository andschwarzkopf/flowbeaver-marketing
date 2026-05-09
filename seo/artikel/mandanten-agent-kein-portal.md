# Das Mandantenportal, das kein Portal ist: Wie ein KI-Agent Belegerfassung übernimmt

**Awareness-Stufe:** 4 (Product aware) | **Länge:** ~1.200 Wörter | **CTA:** Vision-LP / Partnerkanzlei-Bewerbung
**Sprint:** Vision-Launch Säule B, Mai 2026 | **Master-Referenz:** strategie/Vision-Mandanten-Agent.md

---

Mandantenportale haben in den letzten zehn Jahren ihre große Verbreitung in der Steuerkanzleibranche gefunden. DATEV Unternehmen Online dominiert die Landschaft, daneben gibt es eine Hand voll Wettbewerbs-Lösungen für spezielle Segmente. Alle teilen sich denselben Grundgedanken: Der Mandant bekommt einen eigenen Zugang zu einer zentralen Plattform, dort lädt er Belege hoch, dort kommuniziert die Kanzlei mit ihm, dort sieht er Auswertungen.

Das funktioniert in einem Teil der Mandantenbasis hervorragend. Es funktioniert nicht überall — und genau in der Lücke entsteht die Vision, an der wir bei Flowbeaver gerade arbeiten: ein Werkzeug für die Mandantenseite, das **kein Portal** ist.

## Warum die Portal-Logik bei vielen Mandanten nicht aufgeht

Ein Portal ist eine eigenständige Plattform. Der Mandant muss sich anmelden, einen Login pflegen, sich orientieren, Belege in der richtigen Struktur ablegen. Das ist für eine professionelle Buchhaltungsabteilung ein normaler Vorgang — und für einen Handwerksbetrieb, eine Tierarztpraxis, einen Restaurant-Inhaber oder einen Solopreneur eine Hürde, die regelmäßig nicht überwunden wird.

Die Realität bei diesen Mandanten sieht anders aus: Sie fotografieren Belege spontan auf dem Handy. Sie leiten E-Mail-Rechnungen direkt weiter. Sie ziehen PDFs in eine Web-Oberfläche, wenn die einen Klick erfordert. Sie nutzen ihren Lieferanten-Login bei der Telekom, der Stromversorgung oder bei Cloud-Tools, ohne dass diese Rechnungen jemand abholt.

Das ist die Werkzeug-Welt, in der diese Mandanten ohnehin täglich arbeiten. Genau hier setzen wir mit dem Mandanten-Agenten an.

## Die vier Eingangskanäle

Der Mandanten-Agent läuft über die Werkzeuge, die der Mandant bereits beherrscht — und zusätzlich über automatische Abholung dort, wo der Mandant gar nichts tun muss.

**Kanal 1: WhatsApp.** Der Mandant fotografiert einen Beleg und schickt ihn kommentarlos an die Kanzlei-Nummer. Die Quittung von der Tankstelle, die Rechnung über die OP-Lampe, die Lieferung von OBI — egal. Zehn Sekunden Aufwand, und der Beleg ist da, wo er hingehört.

**Kanal 2: E-Mail.** Lieferanten verschicken Rechnungen heute fast immer per E-Mail. Der Mandant leitet sie an eine dedizierte Kanzlei-Adresse weiter. Auch das ist ein Vorgang von wenigen Sekunden — und kann vollständig in seiner gewohnten E-Mail-App passieren.

**Kanal 3: Drag-and-Drop.** Wenn der Mandant lieber eine Datei aus dem Download-Ordner ziehen will, gibt es eine Mini-Oberfläche, die genau das tut: Datei reinziehen, fertig. Keine Formulare, keine Pflichtfelder, keine Konfigurationsmenüs. Sechs Sekunden, kein Login.

**Kanal 4: Automatische Abholung aus Lieferantenportalen.** Telekom, Strom, Versicherung, Cloud-Tools, Software-Abos — die Rechnungen liegen in Portalen, in die der Mandant einmalig seine Zugangsdaten eingibt. Danach holt der Mandanten-Agent die Rechnungen automatisch ab. Der Mandant macht nichts mehr.

Alle vier Kanäle laufen parallel. Der Mandant nutzt, was sein Alltag hergibt — und der Agent sortiert.

## Was der Agent dann tut

Sobald ein Beleg eintrifft, läuft im Hintergrund Folgendes:

Das LLM liest den Beleg, ordnet ihn dem richtigen Mandanten zu, identifiziert den Geschäftsvorfall und füllt die Vorkontierung. In den allermeisten Fällen — unsere Hypothese liegt bei rund neun von zehn Belegen — ist alles klar. Der Beleg fließt direkt in die Vorkontierung, der Mandant bekommt nichts mehr zu sehen.

In den verbleibenden Fällen fragt der Agent gezielt nach. Im selben Kanal, in dem der Beleg kam.

**Beispiel A — fehlender Beleg.** Eine Bankbuchung über 87,40 Euro bei OBI ist auf dem Konto, aber kein Beleg liegt vor. Der Agent schickt eine WhatsApp-Nachricht: *"Zu Ihrer Kartenzahlung am 14. Mai über 87,40 Euro bei OBI haben wir noch keinen Beleg. Können Sie ihn fotografieren und antworten?"* Der Mandant antwortet mit dem Foto, fertig.

**Beispiel B — schlechter Scan.** Eine fotografierte Quittung ist unscharf oder schief. Der Agent: *"Der Beleg von gestern lässt sich nicht lesen. Bitte erneut fotografieren, möglichst gerade von oben."* Mandant macht ein neues Foto.

**Beispiel C — mehrdeutiger Geschäftsvorfall.** Eine OBI-Bestellung über 450 Euro für Holz und Schrauben kann betrieblicher Bürobedarf, Reparatur am Geschäftsobjekt, oder Lagerware für Weiterverkauf sein. Der Agent: *"Ist die OBI-Bestellung vom 14. Mai für Ihren eigenen Bürobedarf, für eine Reparatur, oder als Ware für Weiterverkauf?"*

**Beispiel D — formal fehlerhafter Beleg.** Eine Saturn-Quittung über 1.450 Euro erfüllt nicht die Anforderungen für den Vorsteuerabzug, weil sie keine Rechnung mit Firmen-Adresse ist. Der Agent: *"Diese Saturn-Quittung über 1.450 Euro reicht für den Vorsteuerabzug nicht aus. Bitte fordern Sie bei Saturn eine Rechnung auf Ihre Firmenadresse an."*

In jedem Fall geschieht die Klärung dort, wo sie schnell ist: direkt mit dem Mandanten, ohne Umweg über die Kanzlei. Niemand aus dem Kanzleiteam wird eingebunden — solange es nicht ein echter Sonderfall ist, der Steuerfachwissen erfordert.

## Was die Kanzlei am Ende sieht

Sobald die Klärung abgeschlossen ist, fließen die Daten über die DATEV-Schnittstellen in den Buchungsstapel. Je nach Setup über DUO, Rechnungsdatenservice oder Buchungsdatenservice. Die Kanzlei sieht im DATEV-Workflow:

- einen vollständigen, vorkontierten Buchungsstapel
- ergänzt um die Klärinformationen, die der Agent mit dem Mandanten erarbeitet hat (zum Beispiel die Klassifikation einer mehrdeutigen OBI-Bestellung)
- plus eine deutlich kleinere Liste echter Restklärfälle, die Steuerfachwissen brauchen

Die Klärfälle, die heute Stunden pro Woche an Mandantenkommunikation kosten, sind weg. Die Mitarbeiter der Kanzlei sehen einen sauberen Stapel und prüfen ihn. Die fachliche Steuer-Tiefe — Sonderkonten, Splittbuchungen, Vorsteuer-Optimierung, komplexe Sachverhalte — bleibt bei den Profis. Die Logistik geht weg.

## Was das von DATEV ASR oder DUO unterscheidet

DATEV ASR ist eine OCR-basierte KI-Komponente innerhalb des DATEV-Workflows. Sie liest Belege, die in DUO oder über andere Wege eingegangen sind, und schlägt Buchungen vor. ASR adressiert die Vorkontierung — also Block 3 in der Logistik-Aufteilung, die wir an anderer Stelle beschrieben haben.

DUO ist ein Mandantenportal — also der Eingangskanal Nummer Eins für Belege bei einem Teil der Mandanten. DUO adressiert die strukturierten Mandanten, die mit einem Portal arbeiten können.

Der Mandanten-Agent adressiert weder die Vorkontierung noch das Portal. Er adressiert Block 2 — die Klärung mit dem Mandanten — und gleichzeitig den Eingangskanal für die Mandanten, die DUO nicht zuverlässig nutzen. Er ist ergänzend, nicht ersetzend. Daten fließen am Ende denselben DATEV-Pfad entlang, der heute schon in jeder DATEV-Kanzlei läuft.

## Roadmap und Partnerkanzlei-Programm

Der Mandanten-Agent ist Säule B von Flowbeaver und befindet sich in der Entwicklungs-Vorbereitung. Damit das Werkzeug von Anfang an in echten Kanzleiprozessen funktioniert, suchen wir drei bis fünf Partnerkanzleien für die gemeinsame Entwicklung — wachstumsorientierte Kanzleien mit mindestens 4 Mitarbeitern, DATEV als Hauptsystem, und der Bereitschaft, Workflows offen zu legen.

Decision-Gate ist Mitte Juni 2026: Bei drei oder mehr Partnerkanzlei-Bewerbungen mit ICP-Fit startet die Entwicklung sofort. Andernfalls wird die Vision weiter geprüft, aber nicht gebaut — wir bauen nur, was wirklich gebraucht wird.

Mehr zur Bewerbung und zum Aufbau-Prozess auf der Vision-Seite. Link im Profil.

---

*Dieser Artikel ist Teil der Vision-Launch-Serie Mai 2026. Weiterführend: "Warum die Digitalisierung der Mandanten an einer Mauer scheitert" und "Kapazität statt Personal."*
