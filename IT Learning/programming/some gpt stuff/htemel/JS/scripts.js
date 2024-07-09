async function fetchRecipes() {
    try {
        const response = await fetch('recipes');
        const data = await response.json();
        let recipesContainer = document.getElementById('recipes');
        data.forEach(recipe => {
            let recipeCard = `
            <div class="col-md-4">
              <div class="card mb-4">
                <img class="card-img-top" src="${recipe.image}" alt="${recipe.name}">
                <div class="card-body">
                  <h5 class="card-title">${recipe.name}</h5>
                  <p class="card-text">${recipe.description}</p>
                  <a href="recipe.html?id=${recipe.id}" class="btn btn-primary">Zobacz więcej</a>
                </div>
              </div>
            </div>`;
            recipesContainer.insertAdjacentHTML('beforeend', recipeCard);
        });
    } catch (error) {
        console.error('Error:', error);
    }
}

document.getElementById('recipe-form').addEventListener('submit', function(event) {
    event.preventDefault();

    let recipe = {
        name: document.getElementById('name').value,
        ingredients: document.getElementById('ingredients').value,
        instructions: document.getElementById('instructions').value,
        category: document.getElementById('category').value,
        image: document.getElementById('image').value,
    };

    let recipes = JSON.parse(localStorage.getItem('recipes')) || [];
    recipes.push(recipe);
    localStorage.setItem('recipes', JSON.stringify(recipes));

    alert('Przepis dodany!');
    document.getElementById('recipe-form').reset();
});

document.getElementById('recipes').addEventListener('DOMContentLoaded', fetchRecipes);