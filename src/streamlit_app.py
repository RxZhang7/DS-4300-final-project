import streamlit as st
import pymysql
import pandas as pd
from s3_uploader import upload_image_to_s3
import os
from dotenv import load_dotenv

load_dotenv()

RDS_HOST = os.getenv("RDS_HOST")
RDS_USER = os.getenv("RDS_USER")
RDS_PASSWORD = os.getenv("RDS_PASSWORD")
RDS_DB = os.getenv("RDS_DB")

st.title("🍽️ HealthSnap - Upload Your Meal Photo")

# Upload UI
uploaded_file = st.file_uploader("Choose a meal image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Preview", use_column_width=True)

    if st.button("Upload to S3"):
        success = upload_image_to_s3(uploaded_file, uploaded_file.name)
        if success:
            st.success("✅ Image successfully uploaded to S3!")
            st.info("⏳ Please wait a few seconds while data is inserted into RDS...")
        else:
            st.error("❌ Upload failed. Check console for details.")

# Divider
st.markdown("---")
st.subheader("📊 Recently Uploaded Meals")

# Function to fetch rows
def fetch_latest_rows(limit=10):
    try:
        conn = pymysql.connect(
            host=RDS_HOST,
            user=RDS_USER,
            password=RDS_PASSWORD,
            database=RDS_DB,
            connect_timeout=5
        )
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, image_name, food_name, calories, fat, protein, carbs, upload_time "
                "FROM food_info ORDER BY upload_time DESC LIMIT %s", (limit,)
            )
            rows = cur.fetchall()
            return rows
    except Exception as e:
        st.error(f"❌ Failed to fetch from RDS: {e}")
        return []
    finally:
        if 'conn' in locals():
            conn.close()

# Function to delete by id
def delete_rows_by_ids(ids_to_delete):
    try:
        conn = pymysql.connect(
            host=RDS_HOST,
            user=RDS_USER,
            password=RDS_PASSWORD,
            database=RDS_DB,
            connect_timeout=5
        )
        with conn.cursor() as cur:
            format_ids = ','.join(['%s'] * len(ids_to_delete))
            sql = f"DELETE FROM food_info WHERE id IN ({format_ids})"
            cur.execute(sql, ids_to_delete)
            conn.commit()
    except Exception as e:
        st.error(f"❌ Failed to delete rows: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

# Load data
data = fetch_latest_rows()
if data:
    columns = ["ID", "Image Name", "Food Name", "Calories (kcal)", "Fat (g)", "Protein (g)", "Carbs (g)", "Upload Time"]
    df = pd.DataFrame(data, columns=columns)

    for col in ["Calories (kcal)", "Fat (g)", "Protein (g)", "Carbs (g)"]:
        df[col] = df[col].apply(lambda x: int(x) if x == int(x) else round(x, 1))


    # Editable table
    st.dataframe(df.drop(columns=["ID"]), use_container_width=True)

    if "edit_mode" not in st.session_state:
        st.session_state.edit_mode = False

    if st.button("📝 Edit"):
        st.session_state.edit_mode = True

    if st.session_state.edit_mode:
        st.markdown("### ✅ Select rows to delete")

        selected_ids = []
        for i, row in df.iterrows():
            if st.checkbox(f"Delete row with image: {row['Image Name']}, time: {row['Upload Time']}", key=f"row_{i}"):
                selected_ids.append(int(row["ID"]))

        if st.button("💾 Save Changes"):
            if selected_ids:
                delete_rows_by_ids(selected_ids)
                st.success("✅ Selected rows deleted!")
                st.rerun()
            else:
                st.warning("⚠️ No rows selected.")

else:
    st.info("No records yet. Upload an image to get started.")





