# Health.py
import streamlit as st
import pandas as pd
import plotly.express as px

# --- Streamlit Page Configuration ---
st.set_page_config(page_title="Health & Lifestyle Dashboard", layout="wide")

# --- Title ---
st.title("🩺 Health & Lifestyle Visualization Dashboard")
st.markdown("Analyze lifestyle habits and health conditions interactively using Plotly visualizations.")

st.markdown("""
This Streamlit application allows you to explore lifestyle habits and health conditions 
using **interactive visualizations** built with Plotly.

### 📊 Sections:
- **Health Overview** → Key insights on habits and wellbeing.
- **Objective 1–4** → Specific analyses exploring relationships between lifestyle and health.
- **Test Page** → For additional data validation or experiments.

Use the sidebar on the left to navigate between pages.
""") 

# --- Load Data ---
url = "https://raw.githubusercontent.com/atiqahfsl-oli25/Assignment1/refs/heads/main/dataframe.csv"

@st.cache_data
def load_data(url):
    return pd.read_csv(url)

try:
    df = load_data(url)
    st.success("✅ Data successfully loaded from GitHub!")
except Exception as e:
    st.error(f"❌ Error loading data: {e}")
    st.stop()

# --- Clean Column Names ---
# This replaces spaces with underscores, removes accidental trailing spaces, etc.
# df.columns = df.columns.str.strip().str.replace(" ", "_")

# st.dataframe(df.head(), use_container_width=True)

# --- Check Columns Needed ---
required_cols = [
    "Gender",
    "Alcohol Consumption",
    "Smoking Habit",
    "Sleep Issues",
    "Mental Health Frequency",
    "Age Group",
    "Current Health Conditions",
    "Diet Type",
    "Water Intake per Day"
]

missing = [c for c in required_cols if c not in df.columns]
if missing:
    st.error(
        "The dataset is missing expected columns needed for the visualizations:\n\n"
        f"{missing}\n\n"
        "Please check your CSV header names (they are case-sensitive)."
    )
    st.stop()
