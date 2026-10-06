"""
Recipe Finder - Main Application
================================
A Flask web application that helps users find recipes based on
the ingredients they already have.

Python concepts demonstrated:
- Variables and data types
- Lists and dictionaries
- Functions with parameters and return values
- for loops and if/elif/else conditions
- String manipulation (lower, strip, split)
- Searching and filtering
- Exception handling (try/except)
- Flask routing and request handling
- Jinja2 template rendering
- Random module
"""

# ---- Import statements ----
from flask import Flask, render_template, request, redirect, url_for, abort
import random
import sys
import os

# Add the data folder to the path so we can import recipes
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "data"))

# Import the recipe dataset (a list of dictionaries)
from data.recipes import recipes, common_ingredients, categories

# ---- Create the Flask application ----
app = Flask(__name__)


# ============================================================
# PYTHON HELPER FUNCTIONS
# ============================================================

def normalize_ingredients(ingredient_list):
    """
    Normalize a list of ingredients.
    - Converts each ingredient to lowercase
    - Removes extra spaces
    - Removes empty strings

    Parameters:
        ingredient_list (list): A list of ingredient strings

    Returns:
        list: A cleaned list of ingredient strings
    """
    cleaned = []
    for ingredient in ingredient_list:
        # String manipulation: strip spaces and convert to lowercase
        clean_ingredient = ingredient.strip().lower()
        # Only add non-empty strings
        if clean_ingredient:
            cleaned.append(clean_ingredient)
    return cleaned


def calculate_match_percentage(user_ingredients, recipe_ingredients):
    """
    Calculate what percentage of a recipe's ingredients
    the user already has.

    Parameters:
        user_ingredients (list): Ingredients the user has
        recipe_ingredients (list): Ingredients the recipe needs

    Returns:
        int: Match percentage (0 to 100)
    """
    if len(recipe_ingredients) == 0:
        return 0

    # Count how many recipe ingredients the user has
    match_count = 0
    for ingredient in recipe_ingredients:
        if ingredient in user_ingredients:
            match_count = match_count + 1

    # Basic calculation: percentage = (matches / total) * 100
    percentage = (match_count / len(recipe_ingredients)) * 100
    return round(percentage)


def search_recipes(user_ingredients):
    """
    Search for recipes that match the user's ingredients.

    This function:
    1. Normalizes the user's ingredients
    2. Loops through all recipes
    3. Finds matching and missing ingredients
    4. Calculates match percentage
    5. Sorts recipes by best match

    Parameters:
        user_ingredients (list): Ingredients the user has

    Returns:
        list: Recipes with match information, sorted by best match
    """
    # Step 1: Normalize user input
    normalized_user = normalize_ingredients(user_ingredients)

    # Step 2: Create an empty list to store results
    results = []

    # Step 3: Loop through each recipe in the database
    for recipe in recipes:
        # Normalize the recipe ingredients
        recipe_ingredients = normalize_ingredients(recipe["ingredients"])

        # Find matching ingredients (ingredients in both lists)
        matching = []
        for ingredient in recipe_ingredients:
            if ingredient in normalized_user:
                matching.append(ingredient)

        # Find missing ingredients (in recipe but not with user)
        missing = []
        for ingredient in recipe_ingredients:
            if ingredient not in normalized_user:
                missing.append(ingredient)

        # Calculate the match percentage
        match_percentage = calculate_match_percentage(normalized_user, recipe_ingredients)

        # Only include recipes that have at least one matching ingredient
        if len(matching) > 0:
            # Create a copy of the recipe and add match information
            recipe_with_match = dict(recipe)
            recipe_with_match["matching"] = matching
            recipe_with_match["missing"] = missing
            recipe_with_match["match_percentage"] = match_percentage
            results.append(recipe_with_match)

    # Step 4: Sort results by match percentage (highest first)
    # Using a simple bubble sort to demonstrate Python loops
    for i in range(len(results)):
        for j in range(0, len(results) - i - 1):
            if results[j]["match_percentage"] < results[j + 1]["match_percentage"]:
                # Swap the two recipes
                temp = results[j]
                results[j] = results[j + 1]
                results[j + 1] = temp

    return results


def get_recipe_by_id(recipe_id):
    """
    Find a single recipe by its ID number.

    Parameters:
        recipe_id (int): The ID of the recipe to find

    Returns:
        dict or None: The recipe dictionary, or None if not found
    """
    for recipe in recipes:
        if recipe["id"] == recipe_id:
            return recipe
    return None


def get_recipes_by_category(category_name):
    """
    Get all recipes that belong to a specific category.

    Parameters:
        category_name (str): The category to filter by

    Returns:
        list: Recipes in that category
    """
    filtered_recipes = []
    for recipe in recipes:
        if recipe["category"] == category_name:
            filtered_recipes.append(recipe)
    return filtered_recipes


def get_quick_recipes(max_time=15):
    """
    Get recipes that can be made quickly.

    Parameters:
        max_time (int): Maximum total time in minutes

    Returns:
        list: Quick recipes
    """
    quick = []
    for recipe in recipes:
        if recipe["total_time"] <= max_time:
            quick.append(recipe)
    return quick


def get_vegetarian_recipes():
    """
    Get all vegetarian recipes.

    Returns:
        list: Vegetarian recipes
    """
    veg_recipes = []
    for recipe in recipes:
        if "vegetarian" in recipe["tags"] or "vegan" in recipe["tags"]:
            veg_recipes.append(recipe)
    return veg_recipes


def get_random_recipe():
    """
    Select a random recipe from the database.
    Uses Python's random module.

    Returns:
        dict: A randomly selected recipe
    """
    return random.choice(recipes)


def get_popular_recipes(count=6):
    """
    Get a selection of popular recipes.
    For this app, we select recipes with high match potential.

    Parameters:
        count (int): Number of recipes to return

    Returns:
        list: Popular recipes
    """
    # Select recipes with shorter cooking times as "popular"
    popular = []
    for recipe in recipes:
        if recipe["total_time"] <= 30:
            popular.append(recipe)
    # Return only the requested number
    return popular[:count]


def get_recently_added(count=4):
    """
    Get recently added recipes (highest IDs).

    Parameters:
        count (int): Number of recipes to return

    Returns:
        list: Recently added recipes
    """
    # Sort by ID in descending order (newest first)
    sorted_recipes = sorted(recipes, key=lambda r: r["id"], reverse=True)
    return sorted_recipes[:count]


def filter_recipes(recipes_list, category=None, meal_type=None,
                   difficulty=None, max_time=None, vegetarian=False):
    """
    Filter a list of recipes by multiple criteria.

    Parameters:
        recipes_list (list): The list of recipes to filter
        category (str): Filter by category
        meal_type (str): Filter by meal type
        difficulty (str): Filter by difficulty
        max_time (int): Filter by maximum cooking time
        vegetarian (bool): Filter for vegetarian only

    Returns:
        list: Filtered recipes
    """
    filtered = []

    for recipe in recipes_list:
        # Check each filter condition
        if category and recipe["category"] != category:
            continue
        if meal_type and recipe["meal_type"] != meal_type:
            continue
        if difficulty and recipe["difficulty"] != difficulty:
            continue
        if max_time and recipe["total_time"] > max_time:
            continue
        if vegetarian and "vegetarian" not in recipe["tags"] and "vegan" not in recipe["tags"]:
            continue

        # If all conditions passed, add to results
        filtered.append(recipe)

    return filtered


# ============================================================
# FLASK ROUTES
# ============================================================

@app.route("/")
def home():
    """Home page with ingredient search."""
    return render_template("index.html",
                           recipes=recipes,
                           common_ingredients=common_ingredients,
                           categories=categories,
                           total_recipes=len(recipes))


@app.route("/discover")
def discover():
    """Discover page with various recipe collections."""
    popular = get_popular_recipes(6)
    quick = get_quick_recipes(15)[:6]
    vegetarian = get_vegetarian_recipes()[:6]
    recent = get_recently_added(6)

    return render_template("discover.html",
                           popular=popular,
                           quick=quick,
                           vegetarian=vegetarian,
                           recent=recent,
                           categories=categories)


@app.route("/find-recipes")
def find_recipes():
    """Find Recipes page with ingredient input and filters."""
    return render_template("find-recipes.html",
                           common_ingredients=common_ingredients,
                           categories=categories)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Search results page.
    Handles both GET and POST requests for ingredient search.
    """
    user_ingredients = []

    try:
        if request.method == "POST":
            # Get ingredients from form (comma-separated or multiple values)
            ingredients_text = request.form.get("ingredients", "")
            if ingredients_text:
                # String manipulation: split by comma
                user_ingredients = ingredients_text.split(",")
            # Also check for individual ingredient fields
            for key in request.form:
                if key.startswith("ing_"):
                    val = request.form.get(key, "").strip()
                    if val:
                        user_ingredients.append(val)
        else:
            # GET request: get ingredients from URL parameter
            ingredients_text = request.args.get("ingredients", "")
            if ingredients_text:
                user_ingredients = ingredients_text.split(",")

        # Normalize the ingredients
        user_ingredients = normalize_ingredients(user_ingredients)

        # Error handling: check if user entered any ingredients
        if len(user_ingredients) == 0:
            return render_template("results.html",
                                   error="Please add at least one ingredient.",
                                   user_ingredients=[],
                                   results=[],
                                   categories=categories)

        # Search for matching recipes
        results = search_recipes(user_ingredients)

        # Get filter parameters from URL
        sort_by = request.args.get("sort", "best Match")

        # Sort results based on user preference
        if sort_by == "Quickest":
            results = sorted(results, key=lambda r: r["total_time"])
        elif sort_by == "Easiest":
            difficulty_order = {"Easy": 1, "Medium": 2, "Hard": 3}
            results = sorted(results, key=lambda r: difficulty_order.get(r["difficulty"], 4))
        # "Best Match" is already sorted by match_percentage

        return render_template("results.html",
                               user_ingredients=user_ingredients,
                               results=results,
                               result_count=len(results),
                               sort_by=sort_by,
                               categories=categories)

    except Exception as e:
        # Exception handling: show a friendly error message
        return render_template("results.html",
                               error="Something went wrong. Please try again.",
                               user_ingredients=[],
                               results=[],
                               categories=categories)


@app.route("/recipe/<int:recipe_id>")
def recipe_detail(recipe_id):
    """Recipe detail page showing full recipe information."""
    recipe = get_recipe_by_id(recipe_id)

    # Error handling: recipe not found
    if recipe is None:
        abort(404)

    # Get user ingredients from URL to show match info
    user_ingredients_text = request.args.get("ingredients", "")
    user_ingredients = normalize_ingredients(user_ingredients_text.split(",")) if user_ingredients_text else []

    matching = []
    missing = []
    match_percentage = 0

    if user_ingredients:
        recipe_ingredients = normalize_ingredients(recipe["ingredients"])
        for ingredient in recipe_ingredients:
            if ingredient in user_ingredients:
                matching.append(ingredient)
            else:
                missing.append(ingredient)
        match_percentage = calculate_match_percentage(user_ingredients, recipe_ingredients)

    return render_template("recipe.html",
                           recipe=recipe,
                           matching=matching,
                           missing=missing,
                           match_percentage=match_percentage,
                           user_ingredients=user_ingredients,
                           categories=categories)


@app.route("/categories")
def categories_page():
    """Categories page showing all recipe categories."""
    # Count recipes in each category using a dictionary
    category_counts = {}
    for recipe in recipes:
        cat = recipe["category"]
        if cat in category_counts:
            category_counts[cat] = category_counts[cat] + 1
        else:
            category_counts[cat] = 1

    return render_template("categories.html",
                           categories=categories,
                           category_counts=category_counts,
                           total_recipes=len(recipes))


@app.route("/category/<category_name>")
def category_detail(category_name):
    """Show recipes in a specific category."""
    # Error handling: check if category exists
    if category_name not in categories:
        abort(404)

    # Get recipes for this category using Python filtering
    category_recipes = get_recipes_by_category(category_name)

    return render_template("category.html",
                           category_name=category_name,
                           recipes=category_recipes,
                           categories=categories)


@app.route("/favorites")
def favorites():
    """Favorites page - shows favorited recipe IDs from frontend."""
    return render_template("favorites.html", categories=categories)


@app.route("/surprise")
def surprise():
    """Surprise Me page - Python selects a random recipe."""
    random_recipe = get_random_recipe()
    return render_template("surprise.html",
                           recipe=random_recipe,
                           categories=categories)


@app.route("/pantry")
def pantry():
    """Pantry page for managing ingredients."""
    return render_template("pantry.html",
                           common_ingredients=common_ingredients,
                           categories=categories)


@app.route("/meal-planner")
def meal_planner():
    """Meal Planner page."""
    return render_template("meal_planner.html", categories=categories)


@app.route("/about")
def about():
    """About page explaining the application."""
    return render_template("about.html", categories=categories)


@app.route("/api/recipes")
def api_recipes():
    """
    API endpoint that returns all recipes as JSON.
    Used by the JavaScript frontend for favorites and meal planner.
    """
    return {"recipes": recipes}


# ============================================================
# ERROR HANDLERS
# ============================================================

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 error page."""
    return render_template("404.html", categories=categories), 404


@app.errorhandler(500)
def internal_error(error):
    """Custom 500 error page."""
    return render_template("404.html",
                           error_message="Something went wrong on our end.",
                           categories=categories), 500


# ============================================================
# RUN THE APPLICATION
# ============================================================

if __name__ == "__main__":
    print("=" * 50)
    print("  Recipe Finder - Python & Flask")
    print("=" * 50)
    print(f"  Total recipes loaded: {len(recipes)}")
    print(f"  Categories: {len(categories)}")
    print("=" * 50)
    print("  Open your browser and go to:")
    print("  http://127.0.0.1:5000")
    print("=" * 50)
    app.run(debug=True, host="127.0.0.1", port=5000)
