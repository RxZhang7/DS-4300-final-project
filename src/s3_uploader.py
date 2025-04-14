import boto3
import os
from dotenv import load_dotenv

load_dotenv()

aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_REGION")
bucket_name = os.getenv("S3_BUCKET_NAME")

# Initialize S3 client with credentials
s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)

def upload_image_to_s3(file_obj, filename):
    try:
        s3.upload_fileobj(file_obj, bucket_name, f"uploads/{filename}")
        return True
    except Exception as e:
        print("❌ Upload failed:", e)
        return False
