import streamlit as st
import pandas as pd
import plotly.express as px

# ========================
# Page Configuration
# ========================
st.set_page_config(page_title="Objective 1: Physical Activity Analysis", layout="wide")

# ========================
# Title
# ========================
st.title("🎯 Objective 1: Physical Activity Analysis")

# ========================
# Load Data
# ========================
url = 'https://raw.githubusercontent.com/atiqahfsl-oli25/Assignment1/refs/heads/main/dataframe.csv'

try:
    df = pd.read_csv(url)
    st.success("✅ Data successfully loaded!")
except Exception as e:
    st.error(f"❌ Failed to load data: {e}")
    st.stop()

# ========================
# Preview Columns
# ========================
st.subheader("📋 Dataset Columns (Before Cleaning)")
st.write(df.columns.tolist())

# ========================
# Clean Column Names
# ========================
df.columns = df.columns.str.strip().str.replace(" ", "_").str.replace("-", "_")

st.subheader("🧹 Cleaned Column Names")
st.write(df.columns.tolist())

# ========================
# Check required columns
# ========================
required_cols = ["Physical_Activity_Label", "Gender"]
missing_cols = [col for col in required_cols if col not in df.columns]

if missing_cols:
    st.error(f"❌ Missing columns: {missing_cols}. Please check your CSV file column names.")
    st.stop()

# ========================
# Plot
# ========================
fig = px.histogram(
    df,
    x="Physical_Activity_Label",
    color="Gender",
    barmode="group",
    title="Physical Activity Level by Gender",
)

st.plotly_chart(fig, use_container_width=True)

# ========================
# Data Preview
# ========================
with st.expander("🔍 View Sample Data"):
    st.dataframe(df.head())
