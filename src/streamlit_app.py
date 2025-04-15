import streamlit as st
import pymysql
import pandas as pd
import altair as alt
import plotly.graph_objects as go
from s3_uploader import upload_image_to_s3
import os
from dotenv import load_dotenv

load_dotenv()

RDS_HOST = os.getenv("RDS_HOST")
RDS_USER = os.getenv("RDS_USER")
RDS_PASSWORD = os.getenv("RDS_PASSWORD")
RDS_DB = os.getenv("RDS_DB")

st.markdown("# 🍽️ HealthSnap\n## Upload Your Meal Photo")

# Upload UI
uploaded_file = st.file_uploader("Choose a meal image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Preview", use_column_width=True)

    if st.button("Upload to S3"):
        with st.spinner("Uploading and analyzing image..."):
            try:
                # Check if filename contains a valid food name
                filename = uploaded_file.name.lower()
                valid_foods = ["apple", "banana", "orange", "chicken", "beef", "salmon", "egg", 
                             "bread", "pizza", "cheese", "carrot", "broccoli", "cucumber", 
                             "lettuce", "avocado", "grapes", "yogurt", "oatmeal", "pasta", 
                             "tofu", "shrimp", "steak", "milk", "icecream", "sandwich", 
                             "cereal", "fries", "potato", "rice", "burger"]

                st.info("""
                🔍 Image Recognition Enabled!
                The system will:
                1. Analyze your image using AI
                2. Try to identify the food in the picture
                3. Use filename as backup if needed
                
                For best results, you can:
                - Upload a clear photo of the food
                - Name your file after the food (e.g., apple.jpg)
                - Ensure the food is one of: """ + ", ".join(valid_foods))

                success = upload_image_to_s3(uploaded_file, uploaded_file.name)
                if success:
                    st.success("✅ Image uploaded and analyzed successfully!")
                    st.rerun()
                else:
                    st.error("❌ Upload failed. Check console for details.")
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")

# Divider
st.markdown("---")
st.subheader("📊 Recently Uploaded Meals")

# Function to fetch rows
def fetch_latest_rows():
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
                "FROM food_info ORDER BY upload_time DESC"
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

    # Recently Uploaded Meals edit button
    col1, col2 = st.columns([6, 1])
    with col1:
        st.write("")  # Empty space for alignment
    with col2:
        if st.button(
            "✏️ Edit" if not st.session_state.edit_mode else "Done",
            key="edit_uploaded_meals"  # Added unique key
        ):
            st.session_state.edit_mode = not st.session_state.edit_mode
            st.rerun()

    if st.session_state.edit_mode:
        st.markdown("### Edit Uploaded Meals")
        
        selected_ids = []
        for i, row in df.iterrows():
            col1, col2 = st.columns([5, 1])
            with col1:
                st.text(f"{row['Food Name']} ({row['Upload Time']})")
            with col2:
                if st.button("🗑️", key=f"delete_meal_{i}"):
                    selected_ids.append(int(row["ID"]))
        
        if selected_ids:
            delete_rows_by_ids(selected_ids)
            st.success("✅ Selected meals deleted!")
            st.rerun()

else:
    st.info("No records yet. Upload an image to get started.")

# Add some spacing
st.markdown("---")
st.subheader("📊 Nutrition Analytics")

# Bar Chart with Altair
st.markdown("#### 🔥 Calories by Food Type")

# Get the latest record for each food type
cal_df = df.sort_values("Upload Time").drop_duplicates("Food Name", keep="last")
cal_df = cal_df.sort_values(by="Calories (kcal)", ascending=True).reset_index(drop=True)  # Sort in ascending order
cal_df["Rank"] = cal_df.index + 1
cal_df["Highlight"] = cal_df["Rank"].apply(lambda x: "Top 3" if x >= len(cal_df) - 2 else "Other")  # Update highlight logic

highlight_color = "#FF5733"
default_color = "#1f77b4"

# Configure horizontal bar chart
bar_chart = alt.Chart(cal_df).mark_bar().encode(
    y=alt.Y(
        "Food Name:N", 
        sort="-x",  # Sort by calorie value
        title=None,  # Remove Y-axis title
        axis=alt.Axis(
            labelLimit=200,  # Increase label length limit
            labelFontSize=12  # Adjust font size
        )
    ),
    x=alt.X(
        "Calories (kcal):Q",
        title="Calories (kcal)"
    ),
    color=alt.condition(
        alt.datum.Highlight == "Top 3",
        alt.value(highlight_color),
        alt.value(default_color)
    ),
    tooltip=["Food Name", "Calories (kcal)"]
).properties(
    width=600,
    height=max(len(cal_df) * 30, 400)  # Dynamically adjust height based on number of foods
).configure_axis(
    labelFontSize=12,
    titleFontSize=13
).configure_view(
    strokeWidth=0  # Remove chart border
)

st.altair_chart(bar_chart, use_container_width=True)


# Pie Chart
st.markdown("### 🥜 Macronutrient Breakdown")

# Dropdown to select record
record_options = df.apply(lambda row: f"{row['Food Name']} @ {row['Upload Time']}", axis=1)
selected_label = st.selectbox("Choose an upload to inspect:", record_options)

# Get selected row
selected_row = df.loc[record_options == selected_label].iloc[0]

labels = ["Fat", "Protein", "Carbs"]
values = [selected_row["Fat (g)"], selected_row["Protein (g)"], selected_row["Carbs (g)"]]
colors = ["#1f77b4", "#aec7e8", "#ff4b4b"]

st.markdown(f"**{selected_row['Food Name']} uploaded at {selected_row['Upload Time']}**")

fig = go.Figure(
    data=[
        go.Pie(
            labels=labels,
            values=values,
            marker=dict(colors=colors),
            hoverinfo='label+percent+value',
            textinfo='none',
            showlegend=True
        )
    ]
)

fig.update_layout(
    height=400,
    width=500,
    margin=dict(t=20, b=20, l=0, r=0),
    legend=dict(
        orientation="v",
        yanchor="middle",
        y=0.5,
        xanchor="right",
        x=1.05
    )
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.subheader("🧮 Calorie Calculator")

# Personal Information Section
st.markdown("### 📏 Personal Information")
col1, col2 = st.columns(2)
with col1:
    height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170, step=1)
with col2:
    weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=60, step=1)

# Activity Level Selection
activity_level = st.selectbox(
    "Activity Level",
    ["Sedentary (little or no exercise)",
     "Lightly active (1-3 days/week)",
     "Moderately active (3-5 days/week)",
     "Very active (6-7 days/week)",
     "Extra active (very active + physical job)"]
)

# Weight Loss Goal
col1, col2 = st.columns(2)
with col1:
    weight_loss_goal = st.selectbox(
        "Weight Loss Goal",
        ["Maintain Weight", "Slow Weight Loss", "Moderate Weight Loss", "Fast Weight Loss"]
    )

# Map weight loss goals to calorie deficits
deficit_map = {
    "Maintain Weight": 0,
    "Slow Weight Loss": 250,
    "Moderate Weight Loss": 500,
    "Fast Weight Loss": 750
}
calorie_deficit = deficit_map[weight_loss_goal]

# Calculate BMR and TDEE
def calculate_bmr(height, weight):
    # Using Mifflin-St Jeor Equation
    return 10 * weight + 6.25 * height - 5

def calculate_tdee(bmr, activity_level):
    activity_multipliers = {
        "Sedentary (little or no exercise)": 1.2,
        "Lightly active (1-3 days/week)": 1.375,
        "Moderately active (3-5 days/week)": 1.55,
        "Very active (6-7 days/week)": 1.725,
        "Extra active (very active + physical job)": 1.9
    }
    return bmr * activity_multipliers[activity_level]

bmr = calculate_bmr(height, weight)
tdee = calculate_tdee(bmr, activity_level)

# Display recommended calories
st.markdown("### 💡 Recommended Daily Calorie Intake")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("BMR", f"{bmr:.0f} kcal")
with col2:
    st.metric("TDEE", f"{tdee:.0f} kcal")
with col3:
    target_calories = tdee - calorie_deficit
    st.metric(f"Weight Loss ({calorie_deficit} kcal deficit)", f"{target_calories:.0f} kcal")

# Food Selection and Calculation
st.markdown("### 🍽️ Daily Food Log")

# Initialize session state for food log if not exists
if 'food_log' not in st.session_state:
    st.session_state.food_log = []

# Food Selection Section
st.markdown("#### Add New Food")
food_names = df["Food Name"].unique().tolist() if not df.empty else []
col1, col2 = st.columns(2)
with col1:
    selected_food = st.selectbox("Select Food", food_names)
with col2:
    weight = st.number_input("Serving Size (g)", min_value=1, value=100, step=1)

# Add to log button
if st.button("➕ Add to Daily Log"):
    if selected_food:
        food_info = df[df["Food Name"] == selected_food].iloc[0]
        # Calculate nutrition for the serving
        total_calories = (food_info['Calories (kcal)'] * weight) / 100
        total_protein = (food_info['Protein (g)'] * weight) / 100
        total_fat = (food_info['Fat (g)'] * weight) / 100
        total_carbs = (food_info['Carbs (g)'] * weight) / 100
        
        # Add to food log
        st.session_state.food_log.append({
            'food': selected_food,
            'weight': weight,
            'calories': total_calories,
            'protein': total_protein,
            'fat': total_fat,
            'carbs': total_carbs
        })
        st.success(f"Added {selected_food} ({weight}g) to your daily log!")

# Display Daily Log
st.markdown("#### 📋 Today's Food Log")
if st.session_state.food_log:
    # Add edit mode toggle
    if 'food_log_edit_mode' not in st.session_state:
        st.session_state.food_log_edit_mode = False
        
    col1, col2 = st.columns([6, 1])
    with col1:
        # Create DataFrame from food log
        log_df = pd.DataFrame(st.session_state.food_log)
        
        # Display food log table
        st.dataframe(log_df[['food', 'weight', 'calories', 'protein', 'fat', 'carbs']].rename(columns={
            'food': 'Food',
            'weight': 'Weight (g)',
            'calories': 'Calories (kcal)',
            'protein': 'Protein (g)',
            'fat': 'Fat (g)',
            'carbs': 'Carbs (g)'
        }), use_container_width=True)
    
    with col2:
        if st.button(
            "✏️ Edit" if not st.session_state.food_log_edit_mode else "Done",
            key="edit_food_log"  # Added unique key
        ):
            st.session_state.food_log_edit_mode = not st.session_state.food_log_edit_mode
            st.rerun()
    
    # Show edit interface if in edit mode
    if st.session_state.food_log_edit_mode:
        st.markdown("### Edit Food Log")
        items_to_remove = []
        
        for idx, item in enumerate(st.session_state.food_log):
            col1, col2, col3 = st.columns([4, 2, 1])
            with col1:
                st.text(f"{item['food']}")
            with col2:
                new_weight = st.number_input(
                    "Weight (g)", 
                    value=float(item['weight']), 
                    min_value=1.0, 
                    key=f"weight_{idx}"
                )
                # Update weight and recalculate nutrition
                if new_weight != item['weight']:
                    ratio = new_weight / item['weight']
                    st.session_state.food_log[idx]['weight'] = new_weight
                    st.session_state.food_log[idx]['calories'] *= ratio
                    st.session_state.food_log[idx]['protein'] *= ratio
                    st.session_state.food_log[idx]['fat'] *= ratio
                    st.session_state.food_log[idx]['carbs'] *= ratio
            with col3:
                if st.button("🗑️", key=f"delete_{idx}"):
                    items_to_remove.append(idx)
        
        # Remove marked items
        if items_to_remove:
            for idx in sorted(items_to_remove, reverse=True):
                st.session_state.food_log.pop(idx)
            st.rerun()
    
    # Calculate totals
    total_calories = log_df['calories'].sum()
    total_protein = log_df['protein'].sum()
    total_fat = log_df['fat'].sum()
    total_carbs = log_df['carbs'].sum()
    
    # Display totals
    st.markdown("#### 📊 Daily Nutrition Totals")
    col1, col2, col3, col4 = st.columns(4)
    
    # Calculate target calories (TDEE - deficit)
    target_calories = tdee - calorie_deficit
    calories_difference = total_calories - target_calories
    
    # Format the difference string
    if calories_difference > 0:
        difference_str = f"{calories_difference:.0f} kcal over target"
        difference_color = "inverse"
    else:
        difference_str = f"{abs(calories_difference):.0f} kcal under target"
        difference_color = "normal"
    
    with col1:
        st.metric("Total Calories", f"{total_calories:.0f} kcal", 
                 difference_str, 
                 delta_color=difference_color)
    with col2:
        st.metric("Total Protein", f"{total_protein:.1f} g")
    with col3:
        st.metric("Total Fat", f"{total_fat:.1f} g")
    with col4:
        st.metric("Total Carbs", f"{total_carbs:.1f} g")
    
    # Progress bar for daily calories
    st.markdown(f"**Daily Calorie Progress (Target: {target_calories:.0f} kcal)**")
    progress = total_calories / target_calories
    st.progress(min(progress, 1.0))
    
    # NEW SECTION: Exercise Recommendations
    st.markdown("#### 🏃‍♀️ Exercise Recommendations")
    
    # Add custom CSS for exercise display
    st.markdown("""
        <style>
        .exercise-container {
            text-align: center;
            padding: 1rem;
            width: 100%;
        }
        .exercise-icon {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }
        .exercise-name {
            font-size: 0.9rem;
            color: #666;
            margin-bottom: 0.5rem;
            min-height: 3.5em;
            display: flex;
            align-items: center;
            justify-content: center;
            white-space: nowrap;
            flex-direction: column;
            line-height: 1.2;
        }
        .exercise-time {
            font-size: 1.2rem;
            font-weight: bold;
            margin: 0;
            min-height: 2.5em;
            display: flex;
            align-items: center;
            justify-content: center;
            white-space: nowrap;
            flex-direction: column;
        }
        </style>
    """, unsafe_allow_html=True)
    
    if calories_difference > 0:
        st.markdown(f"To reach your daily goal, you need to burn **{calories_difference:.0f}** excess calories")
        
        # Define exercise burn rates (calories/hour) for a person of average weight (~70kg)
        exercise_burn_rates = {
            "Running\n(10 km/h)": 700,
            "Biking\n(15 km/h)": 500,
            "Weight\nLifting": 350,
            "Swimming\n(moderate)": 600,
            "Walking\n(5 km/h)": 280
        }
        
        # Create a container for better spacing
        with st.container():
            # Use columns for layout with more space between them
            cols = st.columns(5, gap="large")
            
            # Exercise icons
            icons = {
                "Running\n(10 km/h)": "🏃",
                "Biking\n(15 km/h)": "🚴",
                "Weight\nLifting": "🏋️",
                "Swimming\n(moderate)": "🏊",
                "Walking\n(5 km/h)": "🚶"
            }
            
            for i, (exercise, burn_rate) in enumerate(exercise_burn_rates.items()):
                # Calculate hours needed
                hours = calories_difference / burn_rate
                
                # Format time display with line break
                if hours < 1:
                    time_str = f"{int(hours * 60)}\nmin"
                else:
                    hrs = int(hours)
                    mins = int((hours - hrs) * 60)
                    if mins > 0:
                        time_str = f"{hrs} hrs\n{mins} min"
                    else:
                        time_str = f"{hrs}\nhrs"
                
                # Display in columns with custom layout
                with cols[i]:
                    st.markdown(f"""
                        <div class="exercise-container">
                            <div class="exercise-icon">{icons[exercise]}</div>
                            <div class="exercise-name">{exercise.replace('\\n', '<br>')}</div>
                            <div class="exercise-time">{time_str.replace('\\n', '<br>')}</div>
                        </div>
                    """, unsafe_allow_html=True)
    else:
        st.success(f"👏 Great job! You're under your calorie target by {abs(calories_difference):.0f} kcal. Keep it up!")
    
    # Clear log button
    if st.button("🗑️ Clear Daily Log"):
        st.session_state.food_log = []
        st.rerun()
else:
    st.info("No foods logged yet. Add some foods to your daily log!")

# Add some spacing
st.markdown("---")
















