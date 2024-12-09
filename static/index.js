function filterFlavors() {
    const filter = document.querySelector('input[name="filter"]:checked').value;
    const flavorCards = document.querySelectorAll('.flavor-card');
    const header = document.querySelector('header h1');

  
    if (filter === "all") {
        header.innerText = "All Ice Cream Flavors";
    } else if (filter === "seasonal") {
        header.innerText = "Seasonal Ice Cream Flavors";
    } else if (filter === "non-seasonal") {
        header.innerText = "Non-Seasonal Ice Cream Flavors";
    }

    
    flavorCards.forEach(card => {
        const isSeasonal = card.dataset.isSeasonal === "1";
        if (filter === "all" ||
            (filter === "seasonal" && isSeasonal) ||
            (filter === "non-seasonal" && !isSeasonal)) {
            card.style.display = "block";
        } else {
            card.style.display = "none";
        }
    });
}


function filterByAllergen() {
    const selectedAllergens = [];
    document.querySelectorAll('.allergen-checkbox:checked').forEach((checkbox) => {
        selectedAllergens.push(checkbox.value.trim().toLowerCase()); 
    });
    console.log("Selected allergens: ", selectedAllergens); 

    const flavorCards = document.querySelectorAll('.flavor-card');
    flavorCards.forEach(card => {
        const allergens = card.dataset.allergens.split(",").map(allergen => allergen.trim().toLowerCase());
        console.log("Flavor allergens: ", allergens);  

        
        const hasMatchingAllergen = selectedAllergens.some(allergen => allergens.includes(allergen));

        if (hasMatchingAllergen) {
            card.style.display = 'none';  
        } else {
            card.style.display = 'block'; 
        }
    });
}

function searchFlavors() {
const query = document.getElementById('search').value.toLowerCase();  
const flavorCards = document.querySelectorAll('.flavor-card');
const header = document.querySelector('header h1');


if (query) {
    header.innerText = "Search Results for: " + query;
} else {
    header.innerText = "All Ice Cream Flavors";
}


flavorCards.forEach(card => {
    const flavorName = card.querySelector('h3').innerText.toLowerCase(); 
    if (flavorName.includes(query)) {
        card.style.display = 'block';  
    } else {
        card.style.display = 'none'; 
    }
});
}