import os
import pymysql
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 获取数据库配置
db_config = {
    'host': os.getenv('RDS_HOST'),
    'user': os.getenv('RDS_USER'),
    'password': os.getenv('RDS_PASSWORD'),
    'database': os.getenv('RDS_DB'),
    'connect_timeout': 5
}

print("\n=== Database Configuration ===")
print(f"Host: {db_config['host']}")
print(f"User: {db_config['user']}")
print(f"Database: {db_config['database']}")
print(f"Password: {'*' * len(db_config['password']) if db_config['password'] else 'Not set'}")

# 测试连接
print("\n=== Testing Database Connection ===")
try:
    print("Attempting to connect to database...")
    conn = pymysql.connect(**db_config)
    print("✅ Successfully connected to database!")
    
    # 测试查询
    print("\n=== Testing Query ===")
    with conn.cursor() as cur:
        cur.execute("SELECT VERSION()")
        version = cur.fetchone()
        print(f"Database version: {version[0]}")
        
        print("\nTesting food_info table...")
        cur.execute("SHOW TABLES LIKE 'food_info'")
        if cur.fetchone():
            print("✅ food_info table exists")
            cur.execute("SELECT COUNT(*) FROM food_info")
            count = cur.fetchone()[0]
            print(f"Number of records: {count}")
        else:
            print("❌ food_info table does not exist")
    
except Exception as e:
    print(f"\n❌ Connection failed: {str(e)}")
    print("\n🔍 Debug Information:")
    print("1. Check if the RDS instance is running in AWS console")
    print("2. Verify the security group allows inbound traffic on port 3306")
    print("3. Confirm the database endpoint is correct")
    print("4. Make sure the database credentials are correct")
    
finally:
    if 'conn' in locals() and conn:
        conn.close()
        print("\nDatabase connection closed.") 