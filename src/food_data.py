# Food data dictionary shared between s3_uploader.py and lambda_function.py
FOOD_DATA = {
    # Asian Foods
    "sushi":       {"food_name": "Sushi",       "calories": 350,  "protein": 9,   "carbs": 41,  "fat": 18},
    "ramen":       {"food_name": "Ramen",       "calories": 380,  "protein": 10,  "carbs": 60,  "fat": 12},
    "dimsum":      {"food_name": "Dim Sum",     "calories": 250,  "protein": 8,   "carbs": 35,  "fat": 10},
    "dumpling":    {"food_name": "Dumpling",    "calories": 280,  "protein": 12,  "carbs": 38,  "fat": 8},
    "bibimbap":    {"food_name": "Bibimbap",    "calories": 490,  "protein": 12,  "carbs": 80,  "fat": 14},
    "padthai":     {"food_name": "Pad Thai",    "calories": 430,  "protein": 14,  "carbs": 70,  "fat": 13},
    "pho":         {"food_name": "Pho",         "calories": 350,  "protein": 15,  "carbs": 60,  "fat": 6},
    "teriyaki":    {"food_name": "Teriyaki",    "calories": 320,  "protein": 20,  "carbs": 40,  "fat": 8},
    "springroll":  {"food_name": "Spring Roll", "calories": 120,  "protein": 3,   "carbs": 18,  "fat": 4},
    "sashimi":     {"food_name": "Sashimi",     "calories": 200,  "protein": 22,  "carbs": 0,   "fat": 12},
    "tempura":     {"food_name": "Tempura",     "calories": 300,  "protein": 5,   "carbs": 35,  "fat": 15},
    "udon":        {"food_name": "Udon",        "calories": 210,  "protein": 7,   "carbs": 40,  "fat": 2},
    
    # Fruits
    "apple":       {"food_name": "Apple",       "calories": 95,   "protein": 0.5, "carbs": 25,  "fat": 0.3},
    "banana":      {"food_name": "Banana",      "calories": 105,  "protein": 1.3, "carbs": 27,  "fat": 0.3},
    "orange":      {"food_name": "Orange",      "calories": 62,   "protein": 1.2, "carbs": 15.4,"fat": 0.2},
    "strawberry":  {"food_name": "Strawberry",  "calories": 32,   "protein": 0.7, "carbs": 7.7, "fat": 0.3},
    "blueberry":   {"food_name": "Blueberry",   "calories": 57,   "protein": 0.7, "carbs": 14.5,"fat": 0.3},
    "mango":       {"food_name": "Mango",       "calories": 99,   "protein": 1.4, "carbs": 24.7,"fat": 0.6},
    "grapes":      {"food_name": "Grapes",      "calories": 62,   "protein": 0.6, "carbs": 16,  "fat": 0.3},
    "watermelon":  {"food_name": "Watermelon",  "calories": 30,   "protein": 0.6, "carbs": 7.6, "fat": 0.2},
    "pineapple":   {"food_name": "Pineapple",   "calories": 50,   "protein": 0.5, "carbs": 13,  "fat": 0.1},
    "kiwi":        {"food_name": "Kiwi",        "calories": 42,   "protein": 0.8, "carbs": 10,  "fat": 0.4},
    "pear":        {"food_name": "Pear",        "calories": 101,  "protein": 0.6, "carbs": 27,  "fat": 0.2},
    "peach":       {"food_name": "Peach",       "calories": 59,   "protein": 1.4, "carbs": 14,  "fat": 0.4},
    "plum":        {"food_name": "Plum",        "calories": 30,   "protein": 0.5, "carbs": 7.5, "fat": 0.2},
    "cherry":      {"food_name": "Cherry",      "calories": 50,   "protein": 1,   "carbs": 12,  "fat": 0.3},
    "grapefruit":  {"food_name": "Grapefruit",  "calories": 52,   "protein": 0.9, "carbs": 13,  "fat": 0.2},
    "papaya":      {"food_name": "Papaya",      "calories": 59,   "protein": 0.9, "carbs": 15,  "fat": 0.4},
    "fig":         {"food_name": "Fig",         "calories": 74,   "protein": 0.8, "carbs": 19,  "fat": 0.3},
    "pomegranate": {"food_name": "Pomegranate", "calories": 83,   "protein": 1.7, "carbs": 19,  "fat": 1.2},
    "guava":       {"food_name": "Guava",       "calories": 68,   "protein": 2.6, "carbs": 14,  "fat": 1},
    "lychee":      {"food_name": "Lychee",      "calories": 66,   "protein": 0.8, "carbs": 17,  "fat": 0.4},
    "passionfruit":{"food_name": "Passion Fruit","calories": 97,  "protein": 2.2, "carbs": 23,  "fat": 0.4},
    "jackfruit":   {"food_name": "Jackfruit",   "calories": 95,   "protein": 1.7, "carbs": 24,  "fat": 0.6},
    "durian":      {"food_name": "Durian",      "calories": 147,  "protein": 1.5, "carbs": 27,  "fat": 5},
    "dragonfruit": {"food_name": "Dragon Fruit","calories": 60,   "protein": 1.2, "carbs": 13,  "fat": 0.4},
    "blackberry":  {"food_name": "Blackberry",  "calories": 43,   "protein": 1.4, "carbs": 10,  "fat": 0.5},
    "raspberry":   {"food_name": "Raspberry",   "calories": 52,   "protein": 1.5, "carbs": 12,  "fat": 0.7},
    "cantaloupe":  {"food_name": "Cantaloupe",  "calories": 34,   "protein": 0.8, "carbs": 8,   "fat": 0.2},
    
    # Vegetables
    "carrot":      {"food_name": "Carrot",      "calories": 41,   "protein": 0.9, "carbs": 10,  "fat": 0.2},
    "broccoli":    {"food_name": "Broccoli",    "calories": 55,   "protein": 3.7, "carbs": 11,  "fat": 0.6},
    "cucumber":    {"food_name": "Cucumber",    "calories": 16,   "protein": 0.7, "carbs": 4,   "fat": 0.1},
    "lettuce":     {"food_name": "Lettuce",     "calories": 15,   "protein": 1.4, "carbs": 2.9, "fat": 0.2},
    "spinach":     {"food_name": "Spinach",     "calories": 23,   "protein": 2.9, "carbs": 3.6, "fat": 0.4},
    "tomato":      {"food_name": "Tomato",      "calories": 22,   "protein": 1.1, "carbs": 4.8, "fat": 0.2},
    "potato":      {"food_name": "Potato",      "calories": 130,  "protein": 3,   "carbs": 30,  "fat": 0},
    "sweetpotato": {"food_name": "Sweet Potato", "calories": 103, "protein": 2,   "carbs": 24,  "fat": 0.2},
    "onion":       {"food_name": "Onion",       "calories": 40,   "protein": 1.1, "carbs": 9,   "fat": 0.1},
    "pepper":      {"food_name": "Pepper",      "calories": 31,   "protein": 1,   "carbs": 6,   "fat": 0.3},
    "corn":        {"food_name": "Corn",        "calories": 86,   "protein": 3.2, "carbs": 19,  "fat": 1.2},
    "eggplant":    {"food_name": "Eggplant",    "calories": 25,   "protein": 1,   "carbs": 6,   "fat": 0.2},
    "zucchini":    {"food_name": "Zucchini",    "calories": 17,   "protein": 1.2, "carbs": 3.1, "fat": 0.3},
    "kale":        {"food_name": "Kale",        "calories": 49,   "protein": 4.3, "carbs": 9,   "fat": 0.9},
    "asparagus":   {"food_name": "Asparagus",   "calories": 20,   "protein": 2.2, "carbs": 3.7, "fat": 0.2},
    
    # Proteins
    "chicken":     {"food_name": "Chicken",     "calories": 239,  "protein": 27,  "carbs": 0,   "fat": 14},
    "beef":        {"food_name": "Beef",        "calories": 250,  "protein": 26,  "carbs": 0,   "fat": 17},
    "pork":        {"food_name": "Pork",        "calories": 242,  "protein": 26,  "carbs": 0,   "fat": 16},
    "salmon":      {"food_name": "Salmon",      "calories": 208,  "protein": 20,  "carbs": 0,   "fat": 13},
    "tuna":        {"food_name": "Tuna",        "calories": 184,  "protein": 30,  "carbs": 0,   "fat": 6},
    "egg":         {"food_name": "Egg",         "calories": 78,   "protein": 6,   "carbs": 0.6, "fat": 5},
    "tofu":        {"food_name": "Tofu",        "calories": 76,   "protein": 8,   "carbs": 1.9, "fat": 4.8},
    "shrimp":      {"food_name": "Shrimp",      "calories": 99,   "protein": 24,  "carbs": 0.2, "fat": 0.3},
    "duck":        {"food_name": "Duck",        "calories": 337,  "protein": 27,  "carbs": 0,   "fat": 28},
    "lamb":        {"food_name": "Lamb",        "calories": 294,  "protein": 25,  "carbs": 0,   "fat": 21},
    "crab":        {"food_name": "Crab",        "calories": 97,   "protein": 19,  "carbs": 0,   "fat": 1.5},
    "lobster":     {"food_name": "Lobster",     "calories": 89,   "protein": 19,  "carbs": 0,   "fat": 1},
    "turkey":      {"food_name": "Turkey",      "calories": 135,  "protein": 30,  "carbs": 0,   "fat": 1},
    "bacon":       {"food_name": "Bacon",       "calories": 42,   "protein": 3,   "carbs": 0.1, "fat": 3.3},
    "venison":     {"food_name": "Venison",     "calories": 158,  "protein": 30,  "carbs": 0,   "fat": 3},
    
    # Grains & Staples
    "rice":        {"food_name": "Rice",        "calories": 200,  "protein": 4,   "carbs": 45,  "fat": 1},
    "bread":       {"food_name": "Bread",       "calories": 80,   "protein": 3,   "carbs": 15,  "fat": 1},
    "noodle":      {"food_name": "Noodle",      "calories": 220,  "protein": 7,   "carbs": 43,  "fat": 2},
    "oatmeal":     {"food_name": "Oatmeal",     "calories": 150,  "protein": 5,   "carbs": 27,  "fat": 3},
    "quinoa":      {"food_name": "Quinoa",      "calories": 120,  "protein": 4.4, "carbs": 21,  "fat": 1.9},
    "pasta":       {"food_name": "Pasta",       "calories": 131,  "protein": 5,   "carbs": 25,  "fat": 1.1},
    "tortilla":    {"food_name": "Tortilla",    "calories": 140,  "protein": 4,   "carbs": 24,  "fat": 3},
    "bagel":       {"food_name": "Bagel",       "calories": 245,  "protein": 9,   "carbs": 47,  "fat": 1.5},
    "croissant":   {"food_name": "Croissant",   "calories": 231,  "protein": 5,   "carbs": 26,  "fat": 12},
    "barley":      {"food_name": "Barley",      "calories": 354,  "protein": 12,  "carbs": 73,  "fat": 2.3},
    "couscous":    {"food_name": "Couscous",    "calories": 112,  "protein": 3.8, "carbs": 23,  "fat": 0.2},
    "millet":      {"food_name": "Millet",      "calories": 119,  "protein": 3.5, "carbs": 23,  "fat": 1},
    
    # Fast Food & Snacks
    "burger":      {"food_name": "Burger",      "calories": 350,  "protein": 20,  "carbs": 33,  "fat": 18},
    "pizza":       {"food_name": "Pizza",       "calories": 285,  "protein": 12,  "carbs": 36,  "fat": 10},
    "fries":       {"food_name": "Fries",       "calories": 312,  "protein": 3.4, "carbs": 41,  "fat": 15},
    "sandwich":    {"food_name": "Sandwich",    "calories": 250,  "protein": 12,  "carbs": 30,  "fat": 10},
    "hotdog":      {"food_name": "Hot Dog",     "calories": 290,  "protein": 10,  "carbs": 23,  "fat": 17},
    "chips":       {"food_name": "Chips",       "calories": 160,  "protein": 2,   "carbs": 15,  "fat": 10},
    "popcorn":     {"food_name": "Popcorn",     "calories": 106,  "protein": 3,   "carbs": 22,  "fat": 1.2},
    "pretzel":     {"food_name": "Pretzel",     "calories": 108,  "protein": 2.8, "carbs": 22,  "fat": 0.8},
    "nachos":      {"food_name": "Nachos",      "calories": 346,  "protein": 6,   "carbs": 36,  "fat": 21},
    "taco":        {"food_name": "Taco",        "calories": 226,  "protein": 12,  "carbs": 20,  "fat": 12},
    "springroll":  {"food_name": "Spring Roll", "calories": 120,  "protein": 3,   "carbs": 18,  "fat": 4},
    "samosa":      {"food_name": "Samosa",      "calories": 262,  "protein": 6,   "carbs": 32,  "fat": 13},
    
    # Dairy & Alternatives
    "milk":        {"food_name": "Milk",        "calories": 103,  "protein": 8,   "carbs": 12,  "fat": 2.4},
    "yogurt":      {"food_name": "Yogurt",      "calories": 59,   "protein": 10,  "carbs": 3.6, "fat": 0.4},
    "cheese":      {"food_name": "Cheese",      "calories": 113,  "protein": 7,   "carbs": 1,   "fat": 9},
    "icecream":    {"food_name": "Ice Cream",   "calories": 137,  "protein": 2.3, "carbs": 16,  "fat": 7},
    "soymilk":     {"food_name": "Soy Milk",    "calories": 80,   "protein": 7,   "carbs": 4,   "fat": 4},
    "butter":      {"food_name": "Butter",      "calories": 102,  "protein": 0.1, "carbs": 0,   "fat": 12},
    "cream":       {"food_name": "Cream",       "calories": 52,   "protein": 0.3, "carbs": 0.4, "fat": 5.5},
    "ricotta":     {"food_name": "Ricotta",     "calories": 174,  "protein": 14,  "carbs": 3.8, "fat": 13},
    "feta":        {"food_name": "Feta",        "calories": 264,  "protein": 14,  "carbs": 4,   "fat": 21},
    "ghee":        {"food_name": "Ghee",        "calories": 112,  "protein": 0,   "carbs": 0,   "fat": 12.7},
    
    # Desserts
    "cake":        {"food_name": "Cake",        "calories": 280,  "protein": 4,   "carbs": 40,  "fat": 12},
    "cookie":      {"food_name": "Cookie",      "calories": 160,  "protein": 2,   "carbs": 25,  "fat": 7},
    "chocolate":   {"food_name": "Chocolate",   "calories": 210,  "protein": 2.5, "carbs": 24,  "fat": 13},
    "muffin":      {"food_name": "Muffin",      "calories": 230,  "protein": 3,   "carbs": 32,  "fat": 9},
    "brownie":     {"food_name": "Brownie",     "calories": 243,  "protein": 2.8, "carbs": 36,  "fat": 12},
    "donut":       {"food_name": "Donut",       "calories": 195,  "protein": 2.1, "carbs": 22,  "fat": 11},
    "pudding":     {"food_name": "Pudding",     "calories": 130,  "protein": 2,   "carbs": 22,  "fat": 4},
    "gelato":      {"food_name": "Gelato",      "calories": 216,  "protein": 4,   "carbs": 28,  "fat": 9},
    "tiramisu":    {"food_name": "Tiramisu",    "calories": 240,  "protein": 6,   "carbs": 37,  "fat": 12},
    "macaron":     {"food_name": "Macaron",     "calories": 70,   "protein": 1,   "carbs": 11,  "fat": 3},
    
    # Breakfast
    "cereal":      {"food_name": "Cereal",      "calories": 110,  "protein": 2,   "carbs": 24,  "fat": 1},
    "pancake":     {"food_name": "Pancake",     "calories": 175,  "protein": 4,   "carbs": 28,  "fat": 5},
    "waffle":      {"food_name": "Waffle",      "calories": 190,  "protein": 5,   "carbs": 25,  "fat": 7},
    "omelette":    {"food_name": "Omelette",    "calories": 154,  "protein": 11,  "carbs": 1.3, "fat": 11},
    "hashbrown":   {"food_name": "Hash Brown",  "calories": 143,  "protein": 1.5, "carbs": 15,  "fat": 8.5},
    "granola":     {"food_name": "Granola",     "calories": 471,  "protein": 10,  "carbs": 64,  "fat": 20},
    "smoothie":    {"food_name": "Smoothie",    "calories": 200,  "protein": 5,   "carbs": 45,  "fat": 1},
    
    # Healthy Fats
    "avocado":     {"food_name": "Avocado",     "calories": 160,  "protein": 2,   "carbs": 9,   "fat": 15},
    "nuts":        {"food_name": "Nuts",        "calories": 170,  "protein": 6,   "carbs": 6,   "fat": 15},
    "oliveoil":    {"food_name": "Olive Oil",   "calories": 120,  "protein": 0,   "carbs": 0,   "fat": 14},
    "peanutbutter":{"food_name": "Peanut Butter","calories": 188, "protein": 8,   "carbs": 6,   "fat": 16},
    "almond":      {"food_name": "Almond",      "calories": 164,  "protein": 6,   "carbs": 6,   "fat": 14},
    "walnut":      {"food_name": "Walnut",      "calories": 185,  "protein": 4.3, "carbs": 3.9, "fat": 18},
    "chia":        {"food_name": "Chia Seeds",  "calories": 486,  "protein": 16,  "carbs": 42,  "fat": 31},
    "flaxseed":    {"food_name": "Flaxseed",    "calories": 534,  "protein": 18,  "carbs": 29,  "fat": 42},
    "coconut":     {"food_name": "Coconut",     "calories": 354,  "protein": 3,   "carbs": 15,  "fat": 33},
} 