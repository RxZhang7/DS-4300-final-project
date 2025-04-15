import json
import urllib.parse
import boto3
import pymysql
import os
from dotenv import load_dotenv
from food_data import FOOD_DATA

load_dotenv()

RDS_HOST = os.getenv("RDS_HOST")
RDS_USER = os.getenv("RDS_USER")
RDS_PASSWORD = os.getenv("RDS_PASSWORD")
RDS_DB = os.getenv("RDS_DB")

s3 = boto3.client('s3')

def classify_image_by_filename(filename):
    name = filename.lower()

    for keyword, data in FOOD_DATA.items():
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





