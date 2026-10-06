"""
Recipe Dataset for Recipe Finder
================================
This file stores all recipes as a LIST OF DICTIONARIES.
Each dictionary contains the details of one recipe.

Python concepts demonstrated here:
- Variables
- Lists
- Dictionaries
- List of dictionaries
- Strings
"""

# List of dictionaries - each dictionary is one recipe
recipes = [
    {
        "id": 1,
        "name": "Classic Omelette",
        "description": "A fluffy and delicious omelette loaded with vegetables and cheese. Perfect for a quick breakfast.",
        "category": "Breakfast",
        "meal_type": "Breakfast",
        "ingredients": ["egg", "cheese", "onion", "tomato", "butter", "salt", "pepper"],
        "instructions": [
            "Crack the eggs into a bowl and beat them well with salt and pepper.",
            "Heat butter in a non-stick pan over medium heat.",
            "Add chopped onion and tomato, saute for 2 minutes.",
            "Pour the beaten eggs into the pan.",
            "Sprinkle cheese on top and cook until the eggs are set.",
            "Fold the omelette and serve hot."
        ],
        "prep_time": 5,
        "cook_time": 10,
        "total_time": 15,
        "difficulty": "Easy",
        "servings": 1,
        "image": "https://images.unsplash.com/photo-1525351484163-7529414344d8?w=800&q=80",
        "tags": ["vegetarian", "quick", "high-protein"]
    },
    {
        "id": 2,
        "name": "Egg Sandwich",
        "description": "A hearty sandwich with fried egg, fresh tomato and melted cheese between toasted bread slices.",
        "category": "Breakfast",
        "meal_type": "Breakfast",
        "ingredients": ["egg", "bread", "cheese", "tomato", "butter", "lettuce"],
        "instructions": [
            "Toast the bread slices until golden brown.",
            "Fry the egg in a pan with a little butter.",
            "Layer lettuce, tomato slice, fried egg and cheese on one bread slice.",
            "Cover with the second bread slice.",
            "Cut in half and serve immediately."
        ],
        "prep_time": 5,
        "cook_time": 5,
        "total_time": 10,
        "difficulty": "Easy",
        "servings": 1,
        "image": "https://images.unsplash.com/photo-1482049016688-2d3e1b311543?w=800&q=80",
        "tags": ["quick", "vegetarian"]
    },
    {
        "id": 3,
        "name": "Fluffy Pancakes",
        "description": "Soft and fluffy pancakes served with maple syrup and fresh berries. A weekend breakfast favorite.",
        "category": "Breakfast",
        "meal_type": "Breakfast",
        "ingredients": ["flour", "egg", "milk", "sugar", "butter", "baking powder", "maple syrup"],
        "instructions": [
            "Mix flour, sugar and baking powder in a large bowl.",
            "In another bowl, whisk egg and milk together.",
            "Combine wet and dry ingredients, stir until just mixed.",
            "Melt butter in a pan over medium heat.",
            "Pour batter to form circles and cook until bubbles appear.",
            "Flip and cook the other side until golden.",
            "Serve with maple syrup and fresh berries."
        ],
        "prep_time": 10,
        "cook_time": 15,
        "total_time": 25,
        "difficulty": "Easy",
        "servings": 4,
        "image": "https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=800&q=80",
        "tags": ["vegetarian", "sweet", "kid-friendly"]
    },
    {
        "id": 4,
        "name": "Avocado Toast",
        "description": "Creamy avocado spread on crispy toast topped with a poached egg and chili flakes.",
        "category": "Breakfast",
        "meal_type": "Breakfast",
        "ingredients": ["bread", "avocado", "egg", "lemon", "chili flakes", "salt", "olive oil"],
        "instructions": [
            "Toast the bread slices until crispy.",
            "Mash the avocado with lemon juice and salt.",
            "Poach the egg in simmering water for 3 minutes.",
            "Spread mashed avocado on the toast.",
            "Top with the poached egg and sprinkle chili flakes.",
            "Drizzle olive oil and serve."
        ],
        "prep_time": 5,
        "cook_time": 5,
        "total_time": 10,
        "difficulty": "Easy",
        "servings": 2,
        "image": "https://images.unsplash.com/photo-1541519227354-08fa5d50c44d?w=800&q=80",
        "tags": ["vegetarian", "quick", "healthy"]
    },
    {
        "id": 5,
        "name": "French Toast",
        "description": "Golden brown French toast soaked in a sweet egg mixture, served with honey and fruits.",
        "category": "Breakfast",
        "meal_type": "Breakfast",
        "ingredients": ["bread", "egg", "milk", "sugar", "cinnamon", "butter", "honey"],
        "instructions": [
            "Whisk egg, milk, sugar and cinnamon in a shallow dish.",
            "Dip each bread slice into the mixture.",
            "Heat butter in a pan over medium heat.",
            "Cook the dipped bread until golden on both sides.",
            "Serve warm with honey and fresh fruits."
        ],
        "prep_time": 5,
        "cook_time": 10,
        "total_time": 15,
        "difficulty": "Easy",
        "servings": 2,
        "image": "https://images.unsplash.com/photo-1484723091739-30a097e8f929?w=800&q=80",
        "tags": ["vegetarian", "sweet", "quick"]
    },
    {
        "id": 6,
        "name": "Vegetable Salad",
        "description": "A fresh and crunchy salad with mixed vegetables, olive oil and lemon dressing.",
        "category": "Lunch",
        "meal_type": "Lunch",
        "ingredients": ["lettuce", "tomato", "cucumber", "onion", "olive oil", "lemon", "salt"],
        "instructions": [
            "Wash and chop all the vegetables.",
            "Combine lettuce, tomato, cucumber and onion in a large bowl.",
            "Whisk olive oil, lemon juice and salt to make the dressing.",
            "Pour the dressing over the salad.",
            "Toss gently and serve fresh."
        ],
        "prep_time": 10,
        "cook_time": 0,
        "total_time": 10,
        "difficulty": "Easy",
        "servings": 2,
        "image": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=800&q=80",
        "tags": ["vegetarian", "vegan", "healthy", "quick"]
    },
    {
        "id": 7,
        "name": "Grilled Cheese Sandwich",
        "description": "Crispy golden sandwich with gooey melted cheese inside. A comfort food classic.",
        "category": "Lunch",
        "meal_type": "Lunch",
        "ingredients": ["bread", "cheese", "butter", "tomato"],
        "instructions": [
            "Butter the outer sides of the bread slices.",
            "Place cheese and tomato slices between the bread.",
            "Heat a pan over medium heat.",
            "Grill the sandwich until golden and cheese melts.",
            "Flip and cook the other side.",
            "Serve hot and crispy."
        ],
        "prep_time": 5,
        "cook_time": 5,
        "total_time": 10,
        "difficulty": "Easy",
        "servings": 1,
        "image": "https://images.unsplash.com/photo-1528735602780-2552fd46c7af?w=800&q=80",
        "tags": ["vegetarian", "quick", "comfort-food"]
    },
    {
        "id": 8,
        "name": "Chicken Caesar Salad",
        "description": "Crisp romaine lettuce with grilled chicken, parmesan and creamy Caesar dressing.",
        "category": "Lunch",
        "meal_type": "Lunch",
        "ingredients": ["chicken", "lettuce", "cheese", "bread", "garlic", "lemon", "olive oil"],
        "instructions": [
            "Season chicken with salt, pepper and olive oil.",
            "Grill the chicken until fully cooked, then slice.",
            "Cut bread into cubes and toast as croutons.",
            "Tear lettuce into bite-sized pieces.",
            "Whisk garlic, lemon juice and olive oil for dressing.",
            "Toss lettuce, chicken, croutons and cheese with dressing.",
            "Serve immediately."
        ],
        "prep_time": 15,
        "cook_time": 15,
        "total_time": 30,
        "difficulty": "Medium",
        "servings": 2,
        "image": "https://images.unsplash.com/photo-1546793665-c74683f339c1?w=800&q=80",
        "tags": ["high-protein", "healthy"]
    },
    {
        "id": 9,
        "name": "Tomato Soup",
        "description": "A warm and comforting tomato soup with a hint of basil and cream.",
        "category": "Lunch",
        "meal_type": "Lunch",
        "ingredients": ["tomato", "onion", "garlic", "butter", "cream", "basil", "salt"],
        "instructions": [
            "Chop tomatoes, onion and garlic.",
            "Melt butter in a pot and saute onion and garlic.",
            "Add chopped tomatoes and cook for 10 minutes.",
            "Blend the mixture until smooth.",
            "Add cream, salt and basil, simmer for 5 minutes.",
            "Serve hot with bread."
        ],
        "prep_time": 10,
        "cook_time": 20,
        "total_time": 30,
        "difficulty": "Easy",
        "servings": 4,
        "image": "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=800&q=80",
        "tags": ["vegetarian", "comfort-food", "soup"]
    },
    {
        "id": 10,
        "name": "Veggie Wrap",
        "description": "A healthy wrap filled with hummus, crunchy vegetables and fresh herbs.",
        "category": "Lunch",
        "meal_type": "Lunch",
        "ingredients": ["tortilla", "hummus", "lettuce", "tomato", "cucumber", "onion", "cheese"],
        "instructions": [
            "Lay the tortilla flat on a clean surface.",
            "Spread hummus evenly over the tortilla.",
            "Layer lettuce, tomato, cucumber, onion and cheese.",
            "Roll the tortilla tightly into a wrap.",
            "Cut in half and serve."
        ],
        "prep_time": 10,
        "cook_time": 0,
        "total_time": 10,
        "difficulty": "Easy",
        "servings": 1,
        "image": "https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=800&q=80",
        "tags": ["vegetarian", "quick", "healthy"]
    },
    {
        "id": 11,
        "name": "Spaghetti Aglio e Olio",
        "description": "Classic Italian pasta with garlic, olive oil and chili flakes. Simple yet flavorful.",
        "category": "Dinner",
        "meal_type": "Dinner",
        "ingredients": ["spaghetti", "garlic", "olive oil", "chili flakes", "parsley", "salt"],
        "instructions": [
            "Cook spaghetti in salted boiling water until al dente.",
            "Heat olive oil in a pan and saute sliced garlic until golden.",
            "Add chili flakes to the garlic oil.",
            "Toss the cooked spaghetti in the garlic oil.",
            "Garnish with fresh parsley and serve hot."
        ],
        "prep_time": 5,
        "cook_time": 15,
        "total_time": 20,
        "difficulty": "Easy",
        "servings": 2,
        "image": "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=800&q=80",
        "tags": ["vegetarian", "quick", "italian"]
    },
    {
        "id": 12,
        "name": "Chicken Stir Fry",
        "description": "A quick and colorful stir fry with tender chicken and crisp vegetables.",
        "category": "Dinner",
        "meal_type": "Dinner",
        "ingredients": ["chicken", "bell pepper", "onion", "garlic", "soy sauce", "ginger", "rice"],
        "instructions": [
            "Cut chicken into thin strips.",
            "Heat oil in a wok over high heat.",
            "Stir fry chicken until golden, then remove.",
            "Add garlic, ginger, onion and bell pepper, stir fry for 2 minutes.",
            "Return chicken to the wok, add soy sauce.",
            "Serve hot over steamed rice."
        ],
        "prep_time": 10,
        "cook_time": 15,
        "total_time": 25,
        "difficulty": "Medium",
        "servings": 2,
        "image": "https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=800&q=80",
        "tags": ["high-protein", "quick", "asian"]
    },
    {
        "id": 13,
        "name": "Margherita Pizza",
        "description": "A classic pizza with fresh tomato sauce, mozzarella and basil on a crispy crust.",
        "category": "Dinner",
        "meal_type": "Dinner",
        "ingredients": ["pizza dough", "tomato", "cheese", "basil", "olive oil", "garlic"],
        "instructions": [
            "Preheat the oven to the highest setting.",
            "Roll out the pizza dough into a round shape.",
            "Spread crushed tomato sauce over the dough.",
            "Top with slices of mozzarella cheese.",
            "Drizzle olive oil and add garlic.",
            "Bake for 10-12 minutes until the crust is golden.",
            "Garnish with fresh basil and serve."
        ],
        "prep_time": 20,
        "cook_time": 12,
        "total_time": 32,
        "difficulty": "Medium",
        "servings": 2,
        "image": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=800&q=80",
        "tags": ["vegetarian", "italian", "comfort-food"]
    },
    {
        "id": 14,
        "name": "Beef Tacos",
        "description": "Seasoned ground beef in crispy taco shells with fresh toppings and salsa.",
        "category": "Dinner",
        "meal_type": "Dinner",
        "ingredients": ["beef", "taco shells", "lettuce", "tomato", "cheese", "onion", "sour cream"],
        "instructions": [
            "Cook ground beef in a pan until browned.",
            "Add taco seasoning and a little water, simmer.",
            "Warm the taco shells in the oven.",
            "Fill each shell with the beef mixture.",
            "Top with lettuce, tomato, cheese and onion.",
            "Add a dollop of sour cream and serve."
        ],
        "prep_time": 10,
        "cook_time": 15,
        "total_time": 25,
        "difficulty": "Easy",
        "servings": 4,
        "image": "https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?w=800&q=80",
        "tags": ["mexican", "comfort-food"]
    },
    {
        "id": 15,
        "name": "Creamy Mushroom Pasta",
        "description": "Rich and creamy pasta with sauteed mushrooms and parmesan cheese.",
        "category": "Dinner",
        "meal_type": "Dinner",
        "ingredients": ["pasta", "mushroom", "cream", "garlic", "cheese", "butter", "parsley"],
        "instructions": [
            "Cook pasta in salted boiling water until al dente.",
            "Saute sliced mushrooms in butter until golden.",
            "Add garlic and cook for 1 minute.",
            "Pour in the cream and simmer until slightly thickened.",
            "Toss the pasta in the creamy mushroom sauce.",
            "Top with grated cheese and parsley, serve hot."
        ],
        "prep_time": 10,
        "cook_time": 20,
        "total_time": 30,
        "difficulty": "Medium",
        "servings": 2,
        "image": "https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?w=800&q=80",
        "tags": ["vegetarian", "comfort-food", "italian"]
    },
    {
        "id": 16,
        "name": "Baked Salmon",
        "description": "Tender salmon fillet baked with lemon, garlic and herbs. A healthy and elegant dinner.",
        "category": "Dinner",
        "meal_type": "Dinner",
        "ingredients": ["salmon", "lemon", "garlic", "olive oil", "dill", "salt", "pepper"],
        "instructions": [
            "Preheat the oven to 200 degrees C.",
            "Place salmon on a baking sheet.",
            "Drizzle with olive oil and lemon juice.",
            "Season with garlic, dill, salt and pepper.",
            "Bake for 15-18 minutes until the fish flakes easily.",
            "Serve with steamed vegetables."
        ],
        "prep_time": 10,
        "cook_time": 18,
        "total_time": 28,
        "difficulty": "Medium",
        "servings": 2,
        "image": "https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=800&q=80",
        "tags": ["healthy", "high-protein", "seafood"]
    },
    {
        "id": 17,
        "name": "Potato Wedges",
        "description": "Crispy on the outside and fluffy on the inside, these potato wedges are the perfect snack.",
        "category": "Snacks",
        "meal_type": "Snacks",
        "ingredients": ["potato", "olive oil", "paprika", "garlic powder", "salt", "pepper"],
        "instructions": [
            "Preheat the oven to 220 degrees C.",
            "Cut potatoes into wedge shapes.",
            "Toss wedges with olive oil, paprika, garlic powder, salt and pepper.",
            "Spread on a baking sheet in a single layer.",
            "Bake for 25-30 minutes, flipping halfway.",
            "Serve hot with your favorite dip."
        ],
        "prep_time": 10,
        "cook_time": 30,
        "total_time": 40,
        "difficulty": "Easy",
        "servings": 4,
        "image": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=800&q=80",
        "tags": ["vegetarian", "vegan", "comfort-food"]
    },
    {
        "id": 18,
        "name": "Cheese Nachos",
        "description": "Crispy tortilla chips loaded with melted cheese, jalapenos and fresh salsa.",
        "category": "Snacks",
        "meal_type": "Snacks",
        "ingredients": ["tortilla chips", "cheese", "tomato", "onion", "jalapeno", "sour cream"],
        "instructions": [
            "Preheat the oven to 180 degrees C.",
            "Spread tortilla chips on a baking sheet.",
            "Top with grated cheese and sliced jalapenos.",
            "Bake for 5-7 minutes until cheese melts.",
            "Top with fresh tomato salsa and sour cream.",
            "Serve immediately."
        ],
        "prep_time": 5,
        "cook_time": 7,
        "total_time": 12,
        "difficulty": "Easy",
        "servings": 2,
        "image": "https://images.unsplash.com/photo-1513456852971-30c0b8199d4d?w=800&q=80",
        "tags": ["vegetarian", "quick", "mexican"]
    },
    {
        "id": 19,
        "name": "Hummus with Veggies",
        "description": "Creamy homemade hummus served with fresh carrot, cucumber and bell pepper sticks.",
        "category": "Snacks",
        "meal_type": "Snacks",
        "ingredients": ["chickpeas", "tahini", "lemon", "garlic", "olive oil", "carrot", "cucumber"],
        "instructions": [
            "Blend chickpeas, tahini, lemon juice and garlic in a food processor.",
            "Add olive oil and blend until smooth and creamy.",
            "Season with salt to taste.",
            "Cut carrot and cucumber into sticks.",
            "Serve hummus in a bowl surrounded by vegetable sticks."
        ],
        "prep_time": 10,
        "cook_time": 0,
        "total_time": 10,
        "difficulty": "Easy",
        "servings": 4,
        "image": "https://images.unsplash.com/photo-1577805947697-89e18249d767?w=800&q=80",
        "tags": ["vegan", "healthy", "quick"]
    },
    {
        "id": 20,
        "name": "Garlic Bread",
        "description": "Warm and buttery bread with garlic and herbs, baked until golden and crispy.",
        "category": "Snacks",
        "meal_type": "Snacks",
        "ingredients": ["bread", "butter", "garlic", "parsley", "cheese", "salt"],
        "instructions": [
            "Preheat the oven to 180 degrees C.",
            "Mix softened butter with minced garlic, parsley and salt.",
            "Slice the bread and spread the garlic butter on each slice.",
            "Sprinkle cheese on top.",
            "Bake for 8-10 minutes until golden and crispy.",
            "Serve warm."
        ],
        "prep_time": 5,
        "cook_time": 10,
        "total_time": 15,
        "difficulty": "Easy",
        "servings": 4,
        "image": "https://images.unsplash.com/photo-1556008531-57e6eefc7be4?w=800&q=80",
        "tags": ["vegetarian", "quick", "comfort-food"]
    },
    {
        "id": 21,
        "name": "Chocolate Cake",
        "description": "A rich and moist chocolate cake with creamy chocolate frosting. Perfect for celebrations.",
        "category": "Desserts",
        "meal_type": "Desserts",
        "ingredients": ["flour", "cocoa powder", "sugar", "egg", "butter", "milk", "baking powder"],
        "instructions": [
            "Preheat the oven to 180 degrees C.",
            "Mix flour, cocoa powder and baking powder in a bowl.",
            "Cream butter and sugar until fluffy, then add eggs one by one.",
            "Combine dry and wet ingredients, add milk.",
            "Pour batter into a greased cake tin.",
            "Bake for 30-35 minutes until a toothpick comes out clean.",
            "Cool, frost with chocolate icing and serve."
        ],
        "prep_time": 15,
        "cook_time": 35,
        "total_time": 50,
        "difficulty": "Medium",
        "servings": 8,
        "image": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=800&q=80",
        "tags": ["vegetarian", "sweet", "baking"]
    },
    {
        "id": 22,
        "name": "Fruit Smoothie",
        "description": "A refreshing blend of banana, berries and yogurt. A healthy and energizing drink.",
        "category": "Desserts",
        "meal_type": "Desserts",
        "ingredients": ["banana", "strawberry", "yogurt", "honey", "milk", "ice"],
        "instructions": [
            "Peel and slice the banana.",
            "Add banana, strawberries, yogurt, honey and milk to a blender.",
            "Blend until smooth and creamy.",
            "Add ice cubes and blend again.",
            "Pour into glasses and serve immediately."
        ],
        "prep_time": 5,
        "cook_time": 0,
        "total_time": 5,
        "difficulty": "Easy",
        "servings": 2,
        "image": "https://images.unsplash.com/photo-1511690743698-d9d85f2fbf38?w=800&q=80",
        "tags": ["vegetarian", "healthy", "quick", "drink"]
    },
    {
        "id": 23,
        "name": "Chocolate Chip Cookies",
        "description": "Chewy and golden cookies loaded with chocolate chips. A classic treat for all ages.",
        "category": "Desserts",
        "meal_type": "Desserts",
        "ingredients": ["flour", "butter", "sugar", "egg", "chocolate chips", "vanilla", "baking soda"],
        "instructions": [
            "Preheat the oven to 180 degrees C.",
            "Cream butter and sugar until light and fluffy.",
            "Add egg and vanilla, mix well.",
            "Fold in flour and baking soda, then add chocolate chips.",
            "Drop spoonfuls of dough on a baking sheet.",
            "Bake for 10-12 minutes until edges are golden.",
            "Cool on a wire rack and enjoy."
        ],
        "prep_time": 15,
        "cook_time": 12,
        "total_time": 27,
        "difficulty": "Easy",
        "servings": 24,
        "image": "https://images.unsplash.com/photo-1499636136210-6f4ee915583e?w=800&q=80",
        "tags": ["vegetarian", "sweet", "baking", "kid-friendly"]
    },
    {
        "id": 24,
        "name": "Ice Cream Sundae",
        "description": "Vanilla ice cream topped with chocolate sauce, nuts and a cherry. A delightful dessert.",
        "category": "Desserts",
        "meal_type": "Desserts",
        "ingredients": ["ice cream", "chocolate sauce", "nuts", "cherry", "whipped cream"],
        "instructions": [
            "Scoop vanilla ice cream into a serving bowl.",
            "Drizzle chocolate sauce generously over the ice cream.",
            "Sprinkle crushed nuts on top.",
            "Add a swirl of whipped cream.",
            "Top with a cherry and serve immediately."
        ],
        "prep_time": 5,
        "cook_time": 0,
        "total_time": 5,
        "difficulty": "Easy",
        "servings": 1,
        "image": "https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=800&q=80",
        "tags": ["vegetarian", "sweet", "quick", "kid-friendly"]
    },
    {
        "id": 25,
        "name": "Paneer Butter Masala",
        "description": "Cottage cheese cubes in a rich and creamy tomato butter sauce. A North Indian favorite.",
        "category": "Vegetarian",
        "meal_type": "Dinner",
        "ingredients": ["paneer", "tomato", "onion", "butter", "cream", "ginger", "garlic", "spices"],
        "instructions": [
            "Cut paneer into cubes and lightly fry them.",
            "Make a puree of tomato, onion, ginger and garlic.",
            "Heat butter in a pan and cook the puree until thick.",
            "Add spices and simmer for 5 minutes.",
            "Add cream and paneer cubes, cook for 3 minutes.",
            "Serve hot with rice or naan."
        ],
        "prep_time": 15,
        "cook_time": 25,
        "total_time": 40,
        "difficulty": "Medium",
        "servings": 4,
        "image": "https://images.unsplash.com/photo-1631452180519-c014fe946bc7?w=800&q=80",
        "tags": ["vegetarian", "indian", "comfort-food"]
    },
    {
        "id": 26,
        "name": "Vegetable Fried Rice",
        "description": "A quick and flavorful rice dish with mixed vegetables and soy sauce.",
        "category": "Vegetarian",
        "meal_type": "Dinner",
        "ingredients": ["rice", "carrot", "peas", "onion", "garlic", "soy sauce", "spring onion"],
        "instructions": [
            "Cook rice and let it cool completely.",
            "Heat oil in a wok over high heat.",
            "Add garlic, onion and diced carrot, stir fry for 2 minutes.",
            "Add peas and cook for another minute.",
            "Add the cold rice and soy sauce, toss well.",
            "Garnish with spring onion and serve hot."
        ],
        "prep_time": 10,
        "cook_time": 15,
        "total_time": 25,
        "difficulty": "Easy",
        "servings": 2,
        "image": "https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=800&q=80",
        "tags": ["vegetarian", "vegan", "quick", "asian"]
    },
    {
        "id": 27,
        "name": "Caprese Salad",
        "description": "A simple Italian salad with fresh mozzarella, tomatoes and basil, drizzled with olive oil.",
        "category": "Vegetarian",
        "meal_type": "Lunch",
        "ingredients": ["tomato", "mozzarella", "basil", "olive oil", "salt", "pepper", "balsamic vinegar"],
        "instructions": [
            "Slice tomatoes and mozzarella into rounds.",
            "Arrange alternating slices on a plate.",
            "Tuck fresh basil leaves between the slices.",
            "Drizzle with olive oil and balsamic vinegar.",
            "Season with salt and pepper, serve fresh."
        ],
        "prep_time": 10,
        "cook_time": 0,
        "total_time": 10,
        "difficulty": "Easy",
        "servings": 2,
        "image": "https://images.unsplash.com/photo-1592417817098-8fd3d9eb14a5?w=800&q=80",
        "tags": ["vegetarian", "italian", "healthy", "quick"]
    },
    {
        "id": 28,
        "name": "Mushroom Risotto",
        "description": "Creamy Italian rice dish with sauteed mushrooms and parmesan cheese.",
        "category": "Vegetarian",
        "meal_type": "Dinner",
        "ingredients": ["rice", "mushroom", "onion", "garlic", "white wine", "cheese", "butter", "vegetable stock"],
        "instructions": [
            "Saute onion and garlic in butter until soft.",
            "Add sliced mushrooms and cook until golden.",
            "Add rice and stir for 1 minute.",
            "Pour in white wine and let it absorb.",
            "Add warm stock one ladle at a time, stirring constantly.",
            "When rice is creamy and cooked, stir in cheese and butter.",
            "Serve immediately."
        ],
        "prep_time": 10,
        "cook_time": 30,
        "total_time": 40,
        "difficulty": "Hard",
        "servings": 4,
        "image": "https://images.unsplash.com/photo-1476124369491-e7addf5db371?w=800&q=80",
        "tags": ["vegetarian", "italian", "comfort-food"]
    },
    {
        "id": 29,
        "name": "Chicken Biryani",
        "description": "A fragrant and flavorful rice dish layered with spiced chicken and saffron.",
        "category": "Poultry & Meat",
        "meal_type": "Dinner",
        "ingredients": ["chicken", "rice", "yogurt", "onion", "ginger", "garlic", "spices", "saffron"],
        "instructions": [
            "Marinate chicken in yogurt and spices for 30 minutes.",
            "Cook rice until 70 percent done, then drain.",
            "Fry sliced onions until golden and crispy.",
            "Cook the marinated chicken until tender.",
            "Layer rice and chicken in a heavy pot.",
            "Add saffron milk and fried onions on top.",
            "Cover and cook on low heat for 20 minutes.",
            "Mix gently and serve hot."
        ],
        "prep_time": 30,
        "cook_time": 40,
        "total_time": 70,
        "difficulty": "Hard",
        "servings": 4,
        "image": "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=800&q=80",
        "tags": ["indian", "high-protein", "comfort-food"]
    },
    {
        "id": 30,
        "name": "Grilled Chicken Breast",
        "description": "Juicy and tender grilled chicken breast marinated in herbs and lemon.",
        "category": "Poultry & Meat",
        "meal_type": "Dinner",
        "ingredients": ["chicken", "lemon", "garlic", "olive oil", "rosemary", "salt", "pepper"],
        "instructions": [
            "Mix lemon juice, olive oil, garlic, rosemary, salt and pepper.",
            "Marinate the chicken breast for at least 30 minutes.",
            "Preheat the grill to medium-high heat.",
            "Grill chicken for 6-7 minutes per side.",
            "Let it rest for 5 minutes before slicing.",
            "Serve with a side salad or vegetables."
        ],
        "prep_time": 35,
        "cook_time": 15,
        "total_time": 50,
        "difficulty": "Medium",
        "servings": 2,
        "image": "https://images.unsplash.com/photo-1532550907401-a500c9a57435?w=800&q=80",
        "tags": ["high-protein", "healthy", "grilled"]
    },
    {
        "id": 31,
        "name": "Beef Burger",
        "description": "A juicy homemade beef burger with cheese, lettuce and special sauce.",
        "category": "Poultry & Meat",
        "meal_type": "Lunch",
        "ingredients": ["beef", "burger bun", "cheese", "lettuce", "tomato", "onion", "pickle"],
        "instructions": [
            "Season ground beef with salt and pepper.",
            "Shape into patties slightly larger than the buns.",
            "Grill or pan-fry patties for 4 minutes per side.",
            "Add cheese on top in the last minute.",
            "Toast the burger buns.",
            "Assemble with lettuce, tomato, onion, pickle and sauce.",
            "Serve immediately."
        ],
        "prep_time": 10,
        "cook_time": 10,
        "total_time": 20,
        "difficulty": "Easy",
        "servings": 2,
        "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=800&q=80",
        "tags": ["comfort-food", "quick", "american"]
    },
    {
        "id": 32,
        "name": "Chicken Curry",
        "description": "A warm and aromatic chicken curry with coconut milk and spices.",
        "category": "Poultry & Meat",
        "meal_type": "Dinner",
        "ingredients": ["chicken", "coconut milk", "onion", "tomato", "ginger", "garlic", "curry powder"],
        "instructions": [
            "Saute onion, ginger and garlic until soft.",
            "Add curry powder and cook for 1 minute.",
            "Add chopped tomatoes and cook until they break down.",
            "Add chicken pieces and cook until browned.",
            "Pour in coconut milk and simmer for 20 minutes.",
            "Season and serve hot with rice."
        ],
        "prep_time": 10,
        "cook_time": 30,
        "total_time": 40,
        "difficulty": "Medium",
        "servings": 4,
        "image": "https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=800&q=80",
        "tags": ["indian", "high-protein", "comfort-food"]
    },
    {
        "id": 33,
        "name": "15-Minute Fried Rice",
        "description": "The quickest fried rice you will ever make, ready in just 15 minutes.",
        "category": "Quick Meals",
        "meal_type": "Dinner",
        "ingredients": ["rice", "egg", "soy sauce", "spring onion", "garlic", "peas", "carrot"],
        "instructions": [
            "Use leftover or pre-cooked cold rice.",
            "Heat oil in a wok over high heat.",
            "Scramble the egg and set aside.",
            "Stir fry garlic, peas and carrot for 2 minutes.",
            "Add rice and soy sauce, toss everything together.",
            "Add the scrambled egg and spring onion.",
            "Serve hot immediately."
        ],
        "prep_time": 5,
        "cook_time": 10,
        "total_time": 15,
        "difficulty": "Easy",
        "servings": 2,
        "image": "https://images.unsplash.com/photo-1512058564366-18510be2db19?w=800&q=80",
        "tags": ["quick", "vegetarian", "asian"]
    },
    {
        "id": 34,
        "name": "Microwave Mug Cake",
        "description": "A single-serving chocolate cake made in a mug in just 2 minutes.",
        "category": "Quick Meals",
        "meal_type": "Desserts",
        "ingredients": ["flour", "cocoa powder", "sugar", "milk", "oil", "baking powder", "chocolate chips"],
        "instructions": [
            "Mix flour, cocoa powder, sugar and baking powder in a mug.",
            "Add milk and oil, stir until smooth.",
            "Fold in chocolate chips.",
            "Microwave on high for 90 seconds.",
            "Let it cool for a minute and enjoy."
        ],
        "prep_time": 3,
        "cook_time": 2,
        "total_time": 5,
        "difficulty": "Easy",
        "servings": 1,
        "image": "https://images.unsplash.com/photo-1551024506-0bccd828d307?w=800&q=80",
        "tags": ["quick", "vegetarian", "sweet", "kid-friendly"]
    },
    {
        "id": 35,
        "name": "Quesadilla",
        "description": "A crispy tortilla filled with melted cheese and chicken, ready in minutes.",
        "category": "Quick Meals",
        "meal_type": "Lunch",
        "ingredients": ["tortilla", "cheese", "chicken", "bell pepper", "onion", "sour cream"],
        "instructions": [
            "Cook and shred the chicken.",
            "Place a tortilla in a hot pan.",
            "Sprinkle cheese, chicken, bell pepper and onion on one half.",
            "Fold the tortilla in half.",
            "Cook until golden and crispy on both sides.",
            "Cut into wedges and serve with sour cream."
        ],
        "prep_time": 5,
        "cook_time": 10,
        "total_time": 15,
        "difficulty": "Easy",
        "servings": 1,
        "image": "https://images.unsplash.com/photo-1618040996337-56904b7850b9?w=800&q=80",
        "tags": ["quick", "mexican", "comfort-food"]
    },
    {
        "id": 36,
        "name": "Overnight Oats",
        "description": "No-cook oats soaked overnight with milk, fruits and nuts. A healthy grab-and-go breakfast.",
        "category": "Quick Meals",
        "meal_type": "Breakfast",
        "ingredients": ["oats", "milk", "yogurt", "honey", "banana", "nuts", "chia seeds"],
        "instructions": [
            "Add oats, milk and yogurt to a jar.",
            "Stir in chia seeds and honey.",
            "Mix well and refrigerate overnight.",
            "In the morning, top with sliced banana and nuts.",
            "Serve cold or microwave for 1 minute."
        ],
        "prep_time": 5,
        "cook_time": 0,
        "total_time": 5,
        "difficulty": "Easy",
        "servings": 1,
        "image": "https://images.unsplash.com/photo-1517673400267-0251440c45dc?w=800&q=80",
        "tags": ["quick", "vegetarian", "healthy", "no-cook"]
    }
]


# List of common ingredients for quick-add buttons
common_ingredients = [
    "egg", "tomato", "onion", "potato", "cheese",
    "chicken", "rice", "bread", "butter", "milk",
    "garlic", "lemon", "pasta", "flour", "sugar"
]


# List of all categories
categories = [
    "Breakfast",
    "Lunch",
    "Dinner",
    "Snacks",
    "Desserts",
    "Vegetarian",
    "Poultry & Meat",
    "Quick Meals"
]
