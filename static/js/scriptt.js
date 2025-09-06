let extraCost = 50;
let luggagecost = 315;
let carcost = 420;
let petcost = 840;
let refundcost = 271;

// Calculate total amount when checkboxes are clicked
function calculateTotal() {
    let total = baseAmount; // Start with the base amount
    let extras = document.querySelectorAll('input[name="extras"]:checked'); 
    let luggage = document.querySelectorAll('input[name="luggage"]:checked');
    let carmodel = document.querySelectorAll('input[name="carmodel"]:checked');// Get selected extras
    let pet = document.querySelectorAll('input[name="pet"]:checked');
    let refund = document.querySelectorAll('input[name="refund"]:checked');
    
    
    // For each selected checkbox, add the extra cost
    extras.forEach(function () {
        total += extraCost;
    });

    luggage.forEach(function () {
        total += luggagecost;
    });

    carmodel.forEach(function () {
        total += carcost;
    });

    pet.forEach(function () {
        total += petcost;
    });

    refund.forEach(function () {
        total += refundcost;
    });


    // Update the total amount on the page
    document.getElementById('totalAmount').textContent = total;
}


    
