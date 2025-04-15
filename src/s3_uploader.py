import boto3
import os
from dotenv import load_dotenv
import pymysql
from datetime import datetime

load_dotenv()

# AWS credentials
aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_REGION")
bucket_name = os.getenv("S3_BUCKET_NAME")

# RDS credentials
RDS_HOST = os.getenv("RDS_HOST")
RDS_USER = os.getenv("RDS_USER")
RDS_PASSWORD = os.getenv("RDS_PASSWORD")
RDS_DB = os.getenv("RDS_DB")

# Food data dictionary
FOOD_DATA = {
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

# Initialize S3 client with credentials
s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)

def get_food_info(filename):
    """Get food information from filename"""
    # Remove file extension and convert to lowercase
    name = filename.lower()
    # Remove numbers and special characters
    name = ''.join(c for c in name if c.isalpha() or c.isspace())
    
    # Try to find the longest matching food name
    best_match = None
    max_length = 0
    
    for keyword, data in FOOD_DATA.items():
        # If the keyword is found in the cleaned filename
        if keyword in name:
            # Keep track of the longest matching keyword
            if len(keyword) > max_length:
                max_length = len(keyword)
                best_match = data
    
    if best_match:
        print(f"✅ Found food match: {best_match['food_name']}")
        return best_match
        
    print("❌ No food match found")
    return {"food_name": "Unknown", "calories": 0, "protein": 0, "carbs": 0, "fat": 0}

def insert_to_rds(image_name, food_info):
    """Insert food information into RDS"""
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
                INSERT INTO food_info 
                (image_name, food_name, calories, fat, protein, carbs, upload_time)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cur.execute(sql, (
                image_name,
                food_info["food_name"],
                food_info["calories"],
                food_info["fat"],
                food_info["protein"],
                food_info["carbs"],
                datetime.now()
            ))
            conn.commit()
            print("✅ Successfully inserted into RDS")
            return True
    except Exception as e:
        print(f"❌ Failed to insert into RDS: {e}")
        return False
    finally:
        if 'conn' in locals():
            conn.close()

def upload_image_to_s3(file_obj, filename):
    """Upload image to S3 and save info to RDS"""
    try:
        # Upload to S3
        s3.upload_fileobj(file_obj, bucket_name, f"uploads/{filename}")
        print("✅ Successfully uploaded to S3")
        
        # Get food info and save to RDS
        food_info = get_food_info(filename)
        if insert_to_rds(filename, food_info):
            return True
        return False
    except Exception as e:
        print(f"❌ Upload failed: {e}")
        return False