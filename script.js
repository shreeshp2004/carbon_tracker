function calculateCarbon() {
    let carKm = document.getElementById("car").value;
    let acHours = document.getElementById("ac").value;
    let electricityKWh = document.getElementById("electricity").value;
    let meatKg = document.getElementById("meat").value;

    // CO2 emissions factors (kg CO2 per unit)
    let carEmission = carKm * 0.2;  // 0.2 kg CO2 per km
    let acEmission = acHours * 1.5;  // 1.5 kg CO2 per hour
    let electricityEmission = electricityKWh * 0.5; // 0.5 kg CO2 per kWh
    let meatEmission = meatKg * 27;  // 27 kg CO2 per kg of meat

    let totalEmissions = carEmission + acEmission + electricityEmission + meatEmission;

    let resultBox = document.getElementById("result");

    resultBox.innerHTML = `
        🔥 Your estimated daily carbon footprint is: 
        <span style="color:#ff5555; font-size: 24px;">${totalEmissions.toFixed(2)} kg CO₂</span>
    `;

    // Color indicator based on emission levels
    if (totalEmissions < 10) {
        resultBox.style.backgroundColor = "rgba(0, 255, 136, 0.3)";
    } else if (totalEmissions < 30) {
        resultBox.style.backgroundColor = "rgba(255, 165, 0, 0.3)";
    } else {
        resultBox.style.backgroundColor = "rgba(255, 69, 0, 0.3)";
    }

    resultBox.style.padding = "15px";
    resultBox.style.borderRadius = "12px";
}
