# Demo-Anfrage Bestätigung — Automatische E-Mail

Wird automatisch versendet, wenn jemand das Demo-Popup-Formular auf flowbeaver.de absendet.

Versand: Brevo-Automation (Trigger = Form-Submit aus Tilda-Popup).
Variablen: {{ contact.FIRSTNAME }} {{ contact.LASTNAME }} aus dem Form.
Booking-Link: produktive MS-Bookings-Public-URL.
Foto in der Signatur: assets/andreas-schwarzkopf.jpg
   In Brevo als Signatur-Bild ueber den Namen einbinden (rund, ~80×80 px).

---

**Subject:** Ihre Flowbeaver-Demo — wann passt es bei Ihnen?

**Preheader:** 15 Minuten, die sich wirklich lohnen.

---

Guten Tag {{ contact.FIRSTNAME }} {{ contact.LASTNAME }},

vielen Dank für Ihr Interesse an Flowbeaver.

In den 15 Minuten zeige ich Ihnen an echten Beispielbelegen, wie Flowbeaver auch komplexe oder fremdsprachige Rechnungen liest, kontiert und an DATEV übergibt.

Am einfachsten ist es, wenn Sie sich direkt einen Termin in meinem Kalender aussuchen:
https://outlook.office.com/book/Flowbeaver@k-d-a.de/?ismsaljsauthenabled

Bestätigung und Microsoft-Teams-Link kommen automatisch per E-Mail. Sollte keiner der vorgeschlagenen Termine passen, antworten Sie gerne auf diese Mail mit zwei oder drei eigenen Vorschlägen.

Sie müssen nichts vorbereiten.

Beste Grüße

![Andreas Schwarzkopf](../assets/andreas-schwarzkopf.jpg)
**Andreas Schwarzkopf**
Geschäftsführer, Flowbeaver GmbH
Tel: +49 30 20169735
www.flowbeaver.de
