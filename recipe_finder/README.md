# Recipe Finder

A modern, Python-powered web application that helps you discover delicious recipes based on the ingredients you already have at home.

## Features

- **Smart Ingredient Search** - Enter ingredients you have and find matching recipes
- **Match Percentage** - Python calculates exactly how well each recipe matches your ingredients
- **Recipe Categories** - Browse by Breakfast, Lunch, Dinner, Snacks, Desserts, Vegetarian, Poultry & Meat, Quick Meals
- **Favorites** - Save your favorite recipes (stored in browser)
- **Surprise Me** - Python randomly picks a recipe for you
- **Pantry Management** - Keep track of ingredients at home
- **Meal Planner** - Plan meals for the week
- **Dark Mode** - Toggle between light and dark themes
- **Responsive Design** - Works on desktop, tablet, and mobile

## Technology Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Core programming language |
| Flask | Web framework for routes and request handling |
| Jinja2 | Template engine for rendering HTML |
| HTML5 | Semantic markup |
| CSS3 | Modern styling with custom properties |
| JavaScript | Frontend interactions (favorites, pantry, theme) |

## Python Concepts Used

- **Variables & Data Types** - Strings, integers, lists, dictionaries
- **Lists & Dictionaries** - Recipe data stored as a list of dictionaries
- **Functions** - Modular functions with parameters and return values
- **for Loops** - Iterating through recipes and ingredients
- **if/elif/else** - Conditional logic for filtering and sorting
- **String Manipulation** - `lower()`, `strip()`, `split()` for input normalization
- **Searching & Filtering** - Custom search algorithms
- **Random Module** - `random.choice()` for Surprise Me feature
- **Exception Handling** - `try/except` blocks for error safety
- **Flask Routing** - URL routes and HTTP GET/POST handling
- **Jinja2 Templates** - Dynamic HTML rendering

## Project Structure

```
recipe_finder/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── data/
│   └── recipes.py        # Recipe dataset (list of dictionaries)
├── templates/
│   ├── base.html         # Base layout template
│   ├── index.html        # Home page
│   ├── discover.html     # Discover page
│   ├── find-recipes.html # Find Recipes page
│   ├── results.html      # Search results page
│   ├── recipe.html       # Recipe detail page
│   ├── categories.html   # Categories page
│   ├── category.html     # Single category page
│   ├── favorites.html    # Favorites page
│   ├── surprise.html     # Surprise Me page
│   ├── pantry.html       # Pantry page
│   ├── meal_planner.html # Meal Planner page
│   ├── about.html        # About page
│   └── 404.html          # Error page
└── static/
    ├── css/
    │   └── style.css     # Main stylesheet
    └── js/
        └── script.js     # Frontend JavaScript
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone or download the project**

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Open your browser** and go to:
   ```
   http://127.0.0.1:5000
   ```

## How the Matching Algorithm Works

1. **Normalize**: Convert all ingredients to lowercase and remove extra spaces
2. **Compare**: Check each recipe's ingredients against the user's ingredients
3. **Count Matches**: Count how many ingredients match
4. **Calculate Percentage**: `Match % = (matching ingredients / total recipe ingredients) x 100`
5. **Sort Results**: Recipes are sorted by highest match percentage first

### Example

**User has:** egg, tomato, bread

**Recipe needs:** egg, bread, cheese, tomato

**Matching:** egg, bread, tomato (3 out of 4)

**Missing:** cheese

**Match Percentage:** 75%

## Example Ingredient Search

1. Go to the home page or Find Recipes page
2. Type ingredients like `egg`, `tomato`, `bread`
3. Press Enter after each ingredient
4. Click "Find Recipes"
5. Python searches the database and shows matching recipes sorted by match percentage

## Routes

| Route | Description |
|-------|-------------|
| `/` | Home page with ingredient search |
| `/discover` | Discover page with recipe collections |
| `/find-recipes` | Find Recipes page with filters |
| `/search` | Search results (POST/GET) |
| `/categories` | All categories |
| `/category/<name>` | Recipes in a category |
| `/recipe/<id>` | Recipe detail page |
| `/favorites` | Saved favorite recipes |
| `/surprise` | Random recipe selection |
| `/pantry` | Pantry management |
| `/meal-planner` | Weekly meal planner |
| `/about` | About the project |
| `/api/recipes` | JSON API for all recipes |

## Built With Python & Flask

This project was built as a CA-2 college project to demonstrate Python programming concepts in a real-world web application. Python handles:

- Recipe data storage and management
- Ingredient processing and normalization
- Search and matching algorithms
- Filtering by category, difficulty, and time
- Random recipe selection
- Backend routing and request handling
- Template rendering with Jinja2
