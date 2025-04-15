import os
from dotenv import load_dotenv
import boto3

# 确保加载.env文件
load_dotenv()

# 打印环境变量（注意不要打印完整的secret key）
aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_REGION")
bucket_name = os.getenv("S3_BUCKET_NAME")

print("\n=== Environment Variables ===")
print("🔑 Access Key:", aws_access_key)
print("🔒 Secret Key:", "•" * len(aws_secret_key) if aws_secret_key else "Not found")
print("🌎 Region:", aws_region)
print("📦 Bucket:", bucket_name)

# 验证环境变量是否完整
if not all([aws_access_key, aws_secret_key, aws_region, bucket_name]):
    print("\n❌ Missing environment variables!")
    if not aws_access_key:
        print("- AWS_ACCESS_KEY_ID is missing")
    if not aws_secret_key:
        print("- AWS_SECRET_ACCESS_KEY is missing")
    if not aws_region:
        print("- AWS_REGION is missing")
    if not bucket_name:
        print("- S3_BUCKET_NAME is missing")
else:
    print("\n✅ All required environment variables are present")

print("\n=== Testing S3 Connection ===")
try:
    # 初始化S3客户端
    s3 = boto3.client(
        "s3",
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=aws_region
    )
    
    # 测试列出bucket中的对象
    print("📋 Trying to list objects in bucket...")
    response = s3.list_objects_v2(
        Bucket=bucket_name,
        MaxKeys=1
    )
    print("✅ Successfully connected to S3!")
    
    # 尝试上传测试文件
    print("\n📤 Trying to upload test file...")
    s3.put_object(
        Bucket=bucket_name,
        Key='uploads/test.txt',
        Body=b'This is a test file'
    )
    print("✅ Test file upload succeeded!")
    
except Exception as e:
    print(f"\n❌ Error occurred: {str(e)}")
    print("\n🔍 Debug Information:")
    print(f"Access Key ID: {aws_access_key}")
    print(f"Secret Key Length: {len(aws_secret_key) if aws_secret_key else 0}")
    print(f"Region: {aws_region}")
    print(f"Bucket: {bucket_name}")
