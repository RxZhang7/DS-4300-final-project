# HealthSnap - AI-Powered Food Nutrition Tracking App

## Overview
HealthSnap is an AI-powered food nutrition tracking application that uses image recognition technology to identify foods and provide detailed nutritional analysis. Users can upload food photos to track their eating habits, obtain nutritional intake data, and monitor their daily calorie consumption.

## Key Features
- 🤖 AI Image Recognition: Automatically identifies uploaded food images
- 📊 Nutrition Analysis: Provides detailed nutritional information (calories, protein, fat, carbohydrates)
- 📈 Data Visualization: Displays nutritional intake through intuitive charts
- 📝 Food Journal: Records and tracks daily diet
- 🧮 Calorie Calculator: Calculates daily calorie needs based on personal information

## Tech Stack
- Frontend: Streamlit
- Backend: Python
- Database: Amazon RDS (MySQL)
- Storage: Amazon S3
- AI Service: AWS Rekognition
- Data Processing: Pandas, NumPy
- Visualization: Plotly, Altair

## Installation Guide

### Prerequisites
- Python 3.8+
- AWS Account (for S3 and Rekognition services)
- MySQL Database

### Setup Steps
1. Clone the repository
```bash
git clone [repository-url]
cd DS-4300-final-project
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Configure environment variables
Create a `.env` file and add the following configurations:
```
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=your_region
S3_BUCKET_NAME=your_bucket_name
RDS_HOST=your_rds_host
RDS_USER=your_rds_user
RDS_PASSWORD=your_rds_password
RDS_DB=your_database_name
```

4. Initialize database
```sql
CREATE TABLE food_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    image_name VARCHAR(255),
    food_name VARCHAR(255),
    calories FLOAT,
    fat FLOAT,
    protein FLOAT,
    carbs FLOAT,
    upload_time DATETIME
);
```

## Usage Guide
1. Launch the application
```bash
streamlit run src/streamlit_app.py
```

2. Features
- Upload Food Images: Click "Choose a meal image" to upload food photos
- View Nutrition Analysis: Automatically displays nutritional information after upload
- Record Meals: Add food records in the "Daily Food Log"
- View Statistics: Use "Nutrition Analytics" to view nutritional intake statistics
- Calculate Calories: Use "Calorie Calculator" to calculate daily calorie needs

## Project Structure
```
DS-4300-final-project/
├── src/
│   ├── streamlit_app.py    # Main application
│   ├── s3_uploader.py      # S3 upload functionality
│   ├── food_data.py        # Food data dictionary
│   ├── lambda_function.py  # AWS Lambda function
├── requirements.txt        # Project dependencies
└── README.md              # Project documentation
```

## Important Notes
- Ensure AWS credentials are properly configured
- Image upload supports jpg, jpeg, and png formats
- Use clear food images for better recognition accuracy
- Filenames can serve as a backup recognition method

## Contributors
- Rongxuan Zhang
- Yanzhen Chen
- Huy Le

## License
This project is licensed under the MIT License