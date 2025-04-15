import boto3
import os
from dotenv import load_dotenv
import pymysql
from datetime import datetime
import requests
import json
from food_data import FOOD_DATA

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

# USDA API credentials
USDA_API_KEY = os.getenv("USDA_API_KEY", "DEMO_KEY")  # Use DEMO_KEY if not set
USDA_API_URL = "https://api.nal.usda.gov/fdc/v1"

# Initialize AWS clients
s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)

rekognition = boto3.client(
    "rekognition",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)

def detect_food_in_image(bucket, key):
    """Detect food items in the image using AWS Rekognition"""
    try:
        # Check if we have Rekognition permissions first
        try:
            response = rekognition.detect_labels(
                Image={
                    'S3Object': {
                        'Bucket': bucket,
                        'Name': key
                    }
                },
                MaxLabels=10,
                MinConfidence=70
            )
        except Exception as e:
            if "AccessDeniedException" in str(e):
                print("⚠️ Rekognition access not available, falling back to filename matching")
                return []
            raise e

        # Extract food-related labels
        food_labels = []
        for label in response['Labels']:
            if label['Confidence'] > 70:  # Only consider labels with high confidence
                name = label['Name'].lower()
                # Check if the label matches any food in our database
                for food_key in FOOD_DATA.keys():
                    if food_key in name or name in food_key:
                        food_labels.append(food_key)
                        break
        
        print(f"🔍 Detected labels: {food_labels}")
        return food_labels
    except Exception as e:
        print(f"❌ Error detecting labels: {e}")
        return []

def get_food_info(filename, detected_labels=None):
    """Get food information from filename or image recognition only (no USDA API)"""
    # Clean filename
    name = filename.lower()
    name = ''.join(c for c in name if c.isalpha() or c.isspace())
    
    # 1. first try to find matches from filename
    filename_matches = []
    for keyword, data in FOOD_DATA.items():
        if keyword in name:
            filename_matches.append((keyword, len(keyword), data))
    
    # if found filename matches, use the longest one
    if filename_matches:
        filename_matches.sort(key=lambda x: x[1], reverse=True)
        best_match = filename_matches[0][2]
        print(f"✅ Found food match from filename: {best_match['food_name']}")
        return best_match
    
    # 2. if no filename matches, try image recognition results
    if detected_labels:
        for label in detected_labels:
            if label in FOOD_DATA:
                data = FOOD_DATA[label]
                print(f"✅ Found food match from image recognition: {data['food_name']}")
                return data
    
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
    """Upload image to S3, perform recognition, and save info to RDS"""
    try:
        # Upload to S3
        s3_key = f"uploads/{filename}"
        s3.upload_fileobj(file_obj, bucket_name, s3_key)
        print("✅ Successfully uploaded to S3")
        
        try:
            # Attempt image recognition
            detected_labels = detect_food_in_image(bucket_name, s3_key)
        except Exception as e:
            print(f"⚠️ Image recognition failed, falling back to filename matching: {e}")
            detected_labels = []
        
        # Get food info using both filename and detected labels
        food_info = get_food_info(filename, detected_labels)
        
        # Save to RDS
        if insert_to_rds(filename, food_info):
            return True
        return False
    except Exception as e:
        print(f"❌ Upload failed: {e}")
        return False