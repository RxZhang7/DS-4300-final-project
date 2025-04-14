import json
import urllib.parse
import boto3
import pymysql

# RDS settings
RDS_HOST = "host"
RDS_USER = "admin"
RDS_PASSWORD = "master_passward"
RDS_DB = "nutritiondb"

s3 = boto3.client('s3')

def classify_image_by_filename(filename):
    name = filename.lower()

    food_data = {
        "potato":      {"food_name": "Potato",      "calories": 130,  "protein": 3,   "carbs": 30,  "fat": 0},
        "rice":        {"food_name": "Rice",        "calories": 200,  "protein": 4,   "carbs": 45,  "fat": 1},
        "burger":      {"food_name": "Burger",      "calories": 350,  "protein": 20,  "carbs": 33,  "fat": 18},
        "apple":       {"food_name": "Apple",       "calories": 95,   "protein": 0.5, "carbs": 25,  "fat": 0.3},
        "banana":      {"food_name": "Banana",      "calories": 105,  "protein": 1.3, "carbs": 27,  "fat": 0.3},
        "orange":      {"food_name": "Orange",      "calories": 62,   "protein": 1.2, "carbs": 15.4,"fat": 0.2},
        "chicken":     {"food_name": "Chicken",     "calories": 239,  "protein": 27,  "carbs": 0,   "fat": 14},
        "beef":        {"food_name": "Beef",        "calories": 250,  "protein": 26,  "carbs": 0,   "fat": 17},
        "salmon":      {"food_name": "Salmon",      "calories": 208,  "protein": 20,  "carbs": 0,   "fat": 13},
        "egg":         {"food_name": "Egg",         "calories": 78,   "protein": 6,   "carbs": 0.6, "fat": 5},
        "bread":       {"food_name": "Bread",       "calories": 80,   "protein": 3,   "carbs": 15,  "fat": 1},
        "pizza":       {"food_name": "Pizza",       "calories": 285,  "protein": 12,  "carbs": 36,  "fat": 10},
        "cheese":      {"food_name": "Cheese",      "calories": 113,  "protein": 7,   "carbs": 1,   "fat": 9},
        "carrot":      {"food_name": "Carrot",      "calories": 41,   "protein": 0.9, "carbs": 10,  "fat": 0.2},
        "broccoli":    {"food_name": "Broccoli",    "calories": 55,   "protein": 3.7, "carbs": 11,  "fat": 0.6},
        "cucumber":    {"food_name": "Cucumber",    "calories": 16,   "protein": 0.7, "carbs": 4,   "fat": 0.1},
        "lettuce":     {"food_name": "Lettuce",     "calories": 15,   "protein": 1.4, "carbs": 2.9, "fat": 0.2},
        "avocado":     {"food_name": "Avocado",     "calories": 160,  "protein": 2,   "carbs": 9,   "fat": 15},
        "grapes":      {"food_name": "Grapes",      "calories": 62,   "protein": 0.6, "carbs": 16,  "fat": 0.3},
        "yogurt":      {"food_name": "Yogurt",      "calories": 59,   "protein": 10,  "carbs": 3.6, "fat": 0.4},
        "oatmeal":     {"food_name": "Oatmeal",     "calories": 150,  "protein": 5,   "carbs": 27,  "fat": 3},
        "pasta":       {"food_name": "Pasta",       "calories": 131,  "protein": 5,   "carbs": 25,  "fat": 1.1},
        "tofu":        {"food_name": "Tofu",        "calories": 76,   "protein": 8,   "carbs": 1.9, "fat": 4.8},
        "shrimp":      {"food_name": "Shrimp",      "calories": 99,   "protein": 24,  "carbs": 0.2, "fat": 0.3},
        "steak":       {"food_name": "Steak",       "calories": 271,  "protein": 25,  "carbs": 0,   "fat": 19},
        "milk":        {"food_name": "Milk",        "calories": 103,  "protein": 8,   "carbs": 12,  "fat": 2.4},
        "icecream":    {"food_name": "Ice Cream",   "calories": 137,  "protein": 2.3, "carbs": 16,  "fat": 7},
        "sandwich":    {"food_name": "Sandwich",    "calories": 250,  "protein": 12,  "carbs": 30,  "fat": 10},
        "cereal":      {"food_name": "Cereal",      "calories": 110,  "protein": 2,   "carbs": 24,  "fat": 1},
        "fries":       {"food_name": "Fries",       "calories": 312,  "protein": 3.4, "carbs": 41,  "fat": 15}
    }

    for keyword, data in food_data.items():
        if keyword in name:
            return data

    return {"food_name": "Unknown", "calories": 0, "protein": 0, "carbs": 0, "fat": 0}

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(record['s3']['object']['key'])
        print(f"📦 S3 upload detected: Bucket = {bucket}, Key = {key}")

        result = classify_image_by_filename(key)
        print("🍽️ Detected:", result)

        try:
            conn = pymysql.connect(
                host=RDS_HOST,
                user=RDS_USER,
                password=RDS_PASSWORD,
                database=RDS_DB,
                connect_timeout=5
            )
            with conn.cursor() as cur:
                sql = """
                    INSERT INTO food_info (image_name, food_name, calories, fat, protein, carbs)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                cur.execute(sql, (
                    key,
                    result['food_name'],
                    result['calories'],
                    result['fat'],
                    result['protein'],
                    result['carbs']
                ))
                conn.commit()
                print("✅ Inserted into RDS successfully.")
        except Exception as e:
            print("❌ Failed to insert into RDS:", e)
        finally:
            if 'conn' in locals():
                conn.close()

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda processed image using hardcoded classification.')
    }





