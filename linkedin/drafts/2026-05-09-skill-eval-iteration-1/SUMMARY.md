# Iteration 1 — Review

**Stand:** 2026-05-09
**Skill:** `~/.claude/skills/flowbeaver-marketing/linkedin-post-creator/`
**Workspace:** `~/.claude/skills/flowbeaver-marketing/linkedin-post-creator-workspace/iteration-1/`

Drei Test-Cases, jeweils mit-Skill und ohne-Skill (Baseline). Subagents hatten keine Schreibrechte auf den Workspace-Pfad — ich habe die Outputs aus den Inline-Returns selbst abgelegt. Ergebnisse sind valid, der Skill wurde tatsächlich vom With-Skill-Agent gelesen und befolgt (siehe Diagnose-Blöcke im Output).

## Tokens und Zeit

| Test | mit Skill | ohne Skill | Delta |
|------|-----------|------------|-------|
| 1 — Pivot/Coming-Out | 108k tok / 350s | 35k tok / 140s | 3.1× tokens, 2.5× Zeit |
| 2 — DATEV REW93030 | 99k tok / 301s | 26k tok / 62s | 3.8× tokens, 4.9× Zeit |
| 3 — Ambig Mandanten | 95k tok / 234s | 25k tok / 52s | 3.8× tokens, 4.5× Zeit |

Der Skill kostet ~3-4× mehr Tokens und ~3-5× mehr Zeit. Hauptgrund: paralleles Lesen aller Strategie-Dokumente plus Hook-Frameworks plus Humanizer-Referenzen vor dem Schreiben. Frage für Iteration 2: ist das Verhältnis von Aufwand zu Output-Qualität gerechtfertigt? (Meine vorläufige Antwort: ja, aber der Skill könnte schlanker werden.)

---

## Test 1 — Pivot / Coming-Out aus Diktat

**Dateien:**
- mit Skill → [test-1-pivot-diktat/MIT-SKILL.md](test-1-pivot-diktat/MIT-SKILL.md)
- ohne Skill → [test-1-pivot-diktat/OHNE-SKILL.md](test-1-pivot-diktat/OHNE-SKILL.md)

### Meine Bewertung

**Mit Skill — Stärken:**
- Drei wirklich verschiedene Hooks aus drei Hebeln (News, Anekdote, Reframe). Keine Paraphrasen
- Diagnose-Block macht den Awareness-Move explizit (4 → 5 mit Bridge nach 1/2)
- Säulen-Disziplin sauber: "Säule A läuft heute mit den ersten Beta-Kanzleien", "Säule B wird gerade mit Partnerkanzleien gebaut" — Tempus stimmt
- Vier-Schichten-Gründer-Position eingehalten: Unternehmer zuerst, dann Mandant, dann KI als Werkzeug
- Andreas-Voice-Schlusszeile ist scharf: "Wer in der Buchhaltung 2026 noch glaubt, der nächste Schritt sei schnellere OCR, liest den Markt nicht"
- **Wichtig:** Skill hat aktiv das Risiko geflaggt, dass dieser Pivot-Post mit dem bereits geplanten Mai-Sprint-Post #2 doppelt — das ist ein echter strategischer Hinweis, kein Lippenbekenntnis

**Mit Skill — Schwächen:**
- Länge: ~3500 Zeichen, also weit über LinkedIn-Sweetspot. Skill erlaubt das beim Vision-Sondercase, aber: ehrlich gesagt liest sich ein 3500-Zeichen-Post auf LinkedIn nicht durch, egal wie gut. Sollte der Skill **immer** auch eine Kurzfassung mitliefern?
- Hook B und Hook C funktionieren nicht eins-zu-eins mit dem Body, der mit Hook A öffnet. Skill müsste pro Hook einen passenden Body-Einstieg liefern, oder explizit drei Mini-Bodies anbieten

**Ohne Skill — Stärken:**
- Direkter Einstieg "Seit 33 Jahren bin ich Unternehmer"
- Strukturiert mit nummerierten Punkten (RL / eigene Erfahrung / OCR-Welle)
- Auch hier: gute Schlusszeile "Reibungslos. Schnell. Ein System, das Spaß macht. Auf Wachstum eingestellt."

**Ohne Skill — Schwächen:**
- Hashtags im Body (`#Buchhaltung #KI #Steuerberater #Pivot #Flowbeaver`) — Brand-Verstoß
- Italicized startup name (`*Providerly*`) — LinkedIn rendert das als Plain-Text, sieht komisch aus
- "Wenn Sie das interessiert — ob als Steuerberater, als Unternehmer, oder weil Sie selbst an dieser Schnittstelle arbeiten — sprechen Sie mich an" — generischer CTA, nahe an Engagement-Bait
- Kein Awareness-Move, keine Säulen-Disziplin, keine Hook-Varianten
- "Anfang der 90er angefangen" konfligiert mit "33 Jahren" (1992/1993 = 33 Jahre wäre 2025/2026, das stimmt — aber "Anfang der 90er" liest sich wie 1990-1992, leichter Bruch)
- Italische Zwischenfett-Konstruktionen (`**1. Reinforcement Learning hat alles verändert.**`) sind ein KI-Tell

**Mein Verdikt:** Mit-Skill ist klar besser positioniert (Vision/Stratege statt Tool-Anbieter), aber der Skill produziert hier zuviel Text. Iteration 2 sollte: pro Hook-Variante einen passenden Mini-Einstieg, plus optional eine Kurz-Variante für Vision-Posts.

---

## Test 2 — DATEV REW93030 (Solution-aware)

**Dateien:**
- mit Skill → [test-2-datev-rew93030/MIT-SKILL.md](test-2-datev-rew93030/MIT-SKILL.md)
- ohne Skill → [test-2-datev-rew93030/OHNE-SKILL.md](test-2-datev-rew93030/OHNE-SKILL.md)

### Meine Bewertung

**Mit Skill — Stärken:**
- Hook A "REW93030. Wer DATEV intensiv nutzt, kennt den Code. Meistens taucht er Freitagnachmittag auf, wenn der Buchungsstapel der Woche endlich gespeichert werden soll." — sehr konkret, sehr gut
- Reframe-Logik im Body: "Plattform-Geschichte" statt "DATEV-Versagen" — schlauer Move, hält die DATEV-Ergänzungs-Disziplin
- Schlusszeile "DATEV ist und bleibt das Buchhaltungssystem. Flowbeaver liegt davor und filtert. Nicht gegen DATEV. Davor." — Andreas-Voice mit Parallel-Konstruktion, brand-safe
- Säulen-Disziplin sauber (Säule A only, keine Roadmap-Andeutungen)
- Origin-Story bewusst weggelassen mit Begründung
- Brand-Risiko-Check ("Klingt das wie ein Diagnostiker oder wie ein Angreifer?") in den Anmerkungen — gute Selbstprüfung

**Mit Skill — Schwächen:**
- Drei Hooks öffnen unterschiedlich, aber der Body ist nur für Hook A geschrieben. Skill weist darauf hin und sagt "bei B oder C den ersten Absatz streichen", aber das ist Friktion für den Nutzer
- Hook B könnte härter: "Wenn ein Buchungsstapel an REW93030 hängenbleibt..." ist okay, aber beginnt mit Konditionalsatz — die ersten Worte vor "mehr anzeigen" sind nicht der Punch

**Ohne Skill — Stärken:**
- Einstieg "Heute beim Stöbern in der DATEV-Community ist mir wieder etwas aufgefallen" ist okay, aber bait-y
- Erkennt korrekt, dass DATEV nicht angegriffen werden soll
- Soft-CTA am Ende mit Signatur

**Ohne Skill — Schwächen:**
- `**Fehler REW93030**` und `**CSV-Import mit 4-stelligem Datumsformat (TTMM)**` — Bold-Begriff-mit-Erklärung-Liste, klassisches KI-Tell
- "Die eigentliche Arbeit in der Buchhaltung passiert oft an den Rändern des Systems." — schöner Satz, aber dann "Genau dort gehen Stunden verloren" — generischer Filler
- Schluss "Wer von Ihnen kennt diese Threads? Welcher Fehler-Code beschäftigt Ihr Team aktuell am meisten?" — Engagement-Bait, exakt das was die Brand-Regel verbietet
- Hashtags fehlen, dafür `*Andreas Schwarzkopf, Flowbeaver — KI-Vorsystem...*` als Footer — okay, aber italics
- Nur ein Hook, keine Varianten

**Mein Verdikt:** Mit-Skill klar besser, vor allem wegen der "Plattform-Geschichte"-Reframe-Logik und dem brand-konformen Schluss. Schwäche bleibt: Body ist Hook-A-spezifisch.

---

## Test 3 — Ambiguer Mandanten-Input

**Dateien:**
- mit Skill → [test-3-ambiguer-mandanten/MIT-SKILL.md](test-3-ambiguer-mandanten/MIT-SKILL.md)
- ohne Skill → [test-3-ambiguer-mandanten/OHNE-SKILL.md](test-3-ambiguer-mandanten/OHNE-SKILL.md)

### Meine Bewertung

**Hier zeigt der Skill seinen größten Wert.**

**Mit Skill — Stärken:**
- Hat die Ambiguität korrekt erkannt: "Säule A (heute) oder Säule B (Roadmap)?" — und die Klärfrage explizit gestellt, **bevor** geliefert wurde
- Hat darunter eine ehrliche Annahme dokumentiert ("Säule A-Frame, ehrlichere Variante, weil A das Problem heute nicht direkt löst und ein Säule-B-Pitch hier Vendor-Sprache wäre")
- Reframe-Body: "Mandanten, die nicht liefern, scheitern selten an Bequemlichkeit. Sie scheitern an dem Werkzeug" — saubere Awareness-Stufe-2-zu-3-Bewegung
- Lingerd Ending: "Wer das einmal so liest, schaut anders auf den Posteingang." — kein Engagement-Bait, ein nachhallender Gedanke
- DUO namentlich erwähnt mit korrekter Disziplin (Beispiel-Portal, nicht Synonym für DATEV)
- Säule B bewusst nicht erwähnt — kein Pitch geschmuggelt

**Mit Skill — Schwächen:**
- Body ist wieder Hook-A-spezifisch (Datums-Szene), Hook B und C funktionieren nicht direkt davor
- "Pillar 1 mit starkem Einschlag Pillar 5" — vielleicht too cute. Eine Pillar-Entscheidung wäre besser

**Ohne Skill — Stärken:**
- Konkreter Einstieg "Es ist der 14. des Monats. Sie haben Ihrem Mandanten zum dritten Mal hinterhertelefoniert."
- Praktische Tipps (feste Fristen / Pauschalen mit Klausel / Foto per App) — handfest

**Ohne Skill — Schwächen:**
- Hat die Ambiguität nicht erkannt — hat einfach generische Beratungs-Tipps geliefert
- "Willkommen im stillen Produktivitäts-Killer" — Cliché-Phrase
- Nummerierte 1-2-3-Liste mit Bold-Punkten — KI-Tell
- Vendor-leichter Pitch in Punkt 3: "wenn die Erfassung dahinter sauber automatisiert läuft, gewinnt die Kanzlei den Großteil der Zeit zurück" — schleicht ein Tool-Versprechen rein, ohne es als solches zu markieren
- "Wie handhaben Sie das in Ihrer Kanzlei? Feste Fristen oder eher Kulanz?" — Engagement-Bait
- Hashtags `#Steuerberater #Kanzleiführung #Digitalisierung #VorbereitendeBuchhaltung`

**Mein Verdikt:** Größter Skill-Win. Der Skill hat exakt das gemacht, wofür der Test gebaut war: Ambiguität erkennen, Klärfrage stellen, transparent annehmen, Säulen-Disziplin halten.

---

## Vier Diskussionsfragen für Iteration 2

1. **Hook-zu-Body-Kopplung.** Der Skill liefert 3 Hooks, aber der Body öffnet immer mit dem Wortlaut von Hook A. Hooks B und C verlangen, dass der erste Body-Absatz gestrichen wird. Soll der Skill stattdessen 3 Mini-Einstiege liefern (einen pro Hook), die dann in einen gemeinsamen Mittelteil münden? Oder bleibt es bei 1 Body + Hook-A-Eröffnung, und Hook B/C sind explizit als Alternativen markiert?

2. **Vision-Post-Länge.** Test 1 hat ~3500 Zeichen produziert. LinkedIn rendert das als wall of text. Soll der Skill bei Vision/Pivot-Posts **immer auch** eine 1100-Zeichen-Kurzfassung mitliefern? Oder soll die Lange Version komplett raus und der Skill zwingt auf Kurzfassung?

3. **Strategie-Read-Aufwand.** Der Skill liest jedes Mal alle Strategie-Docs + Hook-Frameworks + Humanizer-Refs (~3-4× Token-Aufwand des Baselines). Akzeptabler Preis für die Qualität — oder soll der Skill smarter werden? Z.B. erst Diagnose machen, dann nur die relevanten Sektionen lesen.

4. **Pillar-Diagnose-Schärfe.** Test 3 hat "Pillar 1 mit starkem Einschlag Pillar 5" gesagt. Charmant, aber vielleicht zu weich — der Nutzer will eine Entscheidung. Soll der Skill auf eine einzelne Pillar zwingen?

---

## Wie geben Sie Feedback?

Lesen Sie die `post.md`-Dateien direkt im IDE (Pfade sind oben verlinkt). Schreiben Sie mir dann zurück, was Sie konkret zu jedem der drei Tests denken — und welche der vier Diskussionsfragen wir in Iteration 2 angreifen sollen.

Wenn Sie wollen, können Sie auch direkt sagen "Test X ist Schrott, Test Y nehme ich so wie er ist" — je konkreter, desto besser geht der Skill in Iteration 2 in die richtige Richtung.
