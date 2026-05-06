// Flowbeaver Sparrechner — scoped IIFE, vermeidet globale Namenskonflikte
//
// Konstanten:
//   FLATRATE     — monatliche Flowbeaver-Kosten in Euro
//   SAVINGS_RATE — angenommene Zeitersparnis (0.7 = 70%)
//
// Hinweis: Wenn SAVINGS_RATE geaendert wird, auch das Label
// "bei 70 % Zeitersparnis" im HTML anpassen.
//
// Erwartete DOM-Struktur (siehe Sparrechner-HTML im Block 6):
//   Eingabe-Slider:  fbTimeSlider, fbInvoicesSlider, fbWageSlider
//   Slider-Werte:    fbTimeValue, fbInvoicesValue, fbWageValue
//   Ergebnis-Slider: fbTimeSlider2, fbInvoicesSlider2, fbWageSlider2
//   Ergebnis-Werte:  fbTimeValue2, fbInvoicesValue2, fbWageValue2
//   Ergebnis-Output: fbCurrentHours, fbFlowbeaverHours, fbSavedHours,
//                    fbSavedCosts, fbNetSavings
//   Sektionen:       fbSliderSection, fbResultsSection
//   Button:          .fb-calculate-btn (onclick="fbCalculateSavings()")

(function() {
    const FLATRATE = 299;
    const SAVINGS_RATE = 0.7;

    // Eingabe-Slider live mit Anzeige verbinden
    document.getElementById('fbTimeSlider').oninput = function() {
        document.getElementById('fbTimeValue').textContent = this.value;
    };
    document.getElementById('fbInvoicesSlider').oninput = function() {
        document.getElementById('fbInvoicesValue').textContent = this.value;
    };
    document.getElementById('fbWageSlider').oninput = function() {
        document.getElementById('fbWageValue').textContent = this.value;
    };

    // Ergebnis-Slider live mit Anzeige verbinden
    document.getElementById('fbTimeSlider2').oninput = function() {
        document.getElementById('fbTimeValue2').textContent = this.value;
    };
    document.getElementById('fbInvoicesSlider2').oninput = function() {
        document.getElementById('fbInvoicesValue2').textContent = this.value;
    };
    document.getElementById('fbWageSlider2').oninput = function() {
        document.getElementById('fbWageValue2').textContent = this.value;
    };

    // Globale Handler fuer onclick / onchange im HTML
    window.fbCalculateSavings = function() {
        const time = parseInt(document.getElementById('fbTimeSlider').value);
        const invoices = parseInt(document.getElementById('fbInvoicesSlider').value);
        const wage = parseInt(document.getElementById('fbWageSlider').value);

        document.getElementById('fbTimeSlider2').value = time;
        document.getElementById('fbTimeValue2').textContent = time;
        document.getElementById('fbInvoicesSlider2').value = invoices;
        document.getElementById('fbInvoicesValue2').textContent = invoices;
        document.getElementById('fbWageSlider2').value = wage;
        document.getElementById('fbWageValue2').textContent = wage;

        fbUpdateCalculation();

        document.getElementById('fbSliderSection').style.display = 'none';
        document.getElementById('fbResultsSection').classList.add('active');
    };

    window.fbUpdateCalculation = function() {
        const time = parseInt(document.getElementById('fbTimeSlider2').value);
        const invoices = parseInt(document.getElementById('fbInvoicesSlider2').value);
        const wage = parseInt(document.getElementById('fbWageSlider2').value);

        const currentHours = Math.round((invoices * time) / 60);
        const flowbeaverHours = Math.round((invoices * time * (1 - SAVINGS_RATE)) / 60);
        const savedHours = currentHours - flowbeaverHours;
        const savedCosts = Math.round(savedHours * wage);
        const netSavings = savedCosts - FLATRATE;

        document.getElementById('fbCurrentHours').textContent = currentHours.toLocaleString('de-DE') + ' Stunden';
        document.getElementById('fbFlowbeaverHours').textContent = flowbeaverHours.toLocaleString('de-DE') + ' Stunden';
        document.getElementById('fbSavedHours').textContent = savedHours.toLocaleString('de-DE') + ' Stunden';
        document.getElementById('fbSavedCosts').textContent = savedCosts.toLocaleString('de-DE') + ' Euro';
        document.getElementById('fbNetSavings').textContent = netSavings.toLocaleString('de-DE') + ' Euro / Monat';
    };
})();
