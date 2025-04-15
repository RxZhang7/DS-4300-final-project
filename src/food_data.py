# Food data dictionary shared between s3_uploader.py and lambda_function.py
FOOD_DATA = {
    # Asian Foods
    "sushi":       {"food_name": "Sushi",       "calories": 350,  "protein": 9,   "carbs": 41,  "fat": 18},
    "ramen":       {"food_name": "Ramen",       "calories": 380,  "protein": 10,  "carbs": 60,  "fat": 12},
    "dimsum":      {"food_name": "Dim Sum",     "calories": 250,  "protein": 8,   "carbs": 35,  "fat": 10},
    "dumpling":    {"food_name": "Dumpling",    "calories": 280,  "protein": 12,  "carbs": 38,  "fat": 8},
    
    # Fruits
    "apple":       {"food_name": "Apple",       "calories": 95,   "protein": 0.5, "carbs": 25,  "fat": 0.3},
    "banana":      {"food_name": "Banana",      "calories": 105,  "protein": 1.3, "carbs": 27,  "fat": 0.3},
    "orange":      {"food_name": "Orange",      "calories": 62,   "protein": 1.2, "carbs": 15.4,"fat": 0.2},
    "strawberry":  {"food_name": "Strawberry",  "calories": 32,   "protein": 0.7, "carbs": 7.7, "fat": 0.3},
    "blueberry":   {"food_name": "Blueberry",   "calories": 57,   "protein": 0.7, "carbs": 14.5,"fat": 0.3},
    "mango":       {"food_name": "Mango",       "calories": 99,   "protein": 1.4, "carbs": 24.7,"fat": 0.6},
    "grapes":      {"food_name": "Grapes",      "calories": 62,   "protein": 0.6, "carbs": 16,  "fat": 0.3},
    "watermelon":  {"food_name": "Watermelon",  "calories": 30,   "protein": 0.6, "carbs": 7.6, "fat": 0.2},
    
    # Vegetables
    "carrot":      {"food_name": "Carrot",      "calories": 41,   "protein": 0.9, "carbs": 10,  "fat": 0.2},
    "broccoli":    {"food_name": "Broccoli",    "calories": 55,   "protein": 3.7, "carbs": 11,  "fat": 0.6},
    "cucumber":    {"food_name": "Cucumber",    "calories": 16,   "protein": 0.7, "carbs": 4,   "fat": 0.1},
    "lettuce":     {"food_name": "Lettuce",     "calories": 15,   "protein": 1.4, "carbs": 2.9, "fat": 0.2},
    "spinach":     {"food_name": "Spinach",     "calories": 23,   "protein": 2.9, "carbs": 3.6, "fat": 0.4},
    "tomato":      {"food_name": "Tomato",      "calories": 22,   "protein": 1.1, "carbs": 4.8, "fat": 0.2},
    "potato":      {"food_name": "Potato",      "calories": 130,  "protein": 3,   "carbs": 30,  "fat": 0},
    "sweetpotato": {"food_name": "Sweet Potato", "calories": 103, "protein": 2,   "carbs": 24,  "fat": 0.2},
    
    # Proteins
    "chicken":     {"food_name": "Chicken",     "calories": 239,  "protein": 27,  "carbs": 0,   "fat": 14},
    "beef":        {"food_name": "Beef",        "calories": 250,  "protein": 26,  "carbs": 0,   "fat": 17},
    "pork":        {"food_name": "Pork",        "calories": 242,  "protein": 26,  "carbs": 0,   "fat": 16},
    "salmon":      {"food_name": "Salmon",      "calories": 208,  "protein": 20,  "carbs": 0,   "fat": 13},
    "tuna":        {"food_name": "Tuna",        "calories": 184,  "protein": 30,  "carbs": 0,   "fat": 6},
    "egg":         {"food_name": "Egg",         "calories": 78,   "protein": 6,   "carbs": 0.6, "fat": 5},
    "tofu":        {"food_name": "Tofu",        "calories": 76,   "protein": 8,   "carbs": 1.9, "fat": 4.8},
    "shrimp":      {"food_name": "Shrimp",      "calories": 99,   "protein": 24,  "carbs": 0.2, "fat": 0.3},
    
    # Grains & Staples
    "rice":        {"food_name": "Rice",        "calories": 200,  "protein": 4,   "carbs": 45,  "fat": 1},
    "bread":       {"food_name": "Bread",       "calories": 80,   "protein": 3,   "carbs": 15,  "fat": 1},
    "noodle":      {"food_name": "Noodle",      "calories": 220,  "protein": 7,   "carbs": 43,  "fat": 2},
    "oatmeal":     {"food_name": "Oatmeal",     "calories": 150,  "protein": 5,   "carbs": 27,  "fat": 3},
    "quinoa":      {"food_name": "Quinoa",      "calories": 120,  "protein": 4.4, "carbs": 21,  "fat": 1.9},
    "pasta":       {"food_name": "Pasta",       "calories": 131,  "protein": 5,   "carbs": 25,  "fat": 1.1},
    
    # Fast Food & Snacks
    "burger":      {"food_name": "Burger",      "calories": 350,  "protein": 20,  "carbs": 33,  "fat": 18},
    "pizza":       {"food_name": "Pizza",       "calories": 285,  "protein": 12,  "carbs": 36,  "fat": 10},
    "fries":       {"food_name": "Fries",       "calories": 312,  "protein": 3.4, "carbs": 41,  "fat": 15},
    "sandwich":    {"food_name": "Sandwich",    "calories": 250,  "protein": 12,  "carbs": 30,  "fat": 10},
    "hotdog":      {"food_name": "Hot Dog",     "calories": 290,  "protein": 10,  "carbs": 23,  "fat": 17},
    "chips":       {"food_name": "Chips",       "calories": 160,  "protein": 2,   "carbs": 15,  "fat": 10},
    
    # Dairy & Alternatives
    "milk":        {"food_name": "Milk",        "calories": 103,  "protein": 8,   "carbs": 12,  "fat": 2.4},
    "yogurt":      {"food_name": "Yogurt",      "calories": 59,   "protein": 10,  "carbs": 3.6, "fat": 0.4},
    "cheese":      {"food_name": "Cheese",      "calories": 113,  "protein": 7,   "carbs": 1,   "fat": 9},
    "icecream":    {"food_name": "Ice Cream",   "calories": 137,  "protein": 2.3, "carbs": 16,  "fat": 7},
    "soymilk":     {"food_name": "Soy Milk",    "calories": 80,   "protein": 7,   "carbs": 4,   "fat": 4},
    
    # Desserts
    "cake":        {"food_name": "Cake",        "calories": 280,  "protein": 4,   "carbs": 40,  "fat": 12},
    "cookie":      {"food_name": "Cookie",      "calories": 160,  "protein": 2,   "carbs": 25,  "fat": 7},
    "chocolate":   {"food_name": "Chocolate",   "calories": 210,  "protein": 2.5, "carbs": 24,  "fat": 13},
    "muffin":      {"food_name": "Muffin",      "calories": 230,  "protein": 3,   "carbs": 32,  "fat": 9},
    
    # Breakfast
    "cereal":      {"food_name": "Cereal",      "calories": 110,  "protein": 2,   "carbs": 24,  "fat": 1},
    "pancake":     {"food_name": "Pancake",     "calories": 175,  "protein": 4,   "carbs": 28,  "fat": 5},
    "waffle":      {"food_name": "Waffle",      "calories": 190,  "protein": 5,   "carbs": 25,  "fat": 7},
    
    # Healthy Fats
    "avocado":     {"food_name": "Avocado",     "calories": 160,  "protein": 2,   "carbs": 9,   "fat": 15},
    "nuts":        {"food_name": "Nuts",        "calories": 170,  "protein": 6,   "carbs": 6,   "fat": 15},
    "oliveoil":    {"food_name": "Olive Oil",   "calories": 120,  "protein": 0,   "carbs": 0,   "fat": 14}
} 