import streamlit as st
import pandas as pd
import plotly.express as px

# ==============================
# 🩺 STREAMLIT PAGE CONFIGURATION
# ==============================
st.set_page_config(page_title="Health & Lifestyle Dashboard", layout="wide")

# ==============================
# 🏷️ TITLE & INTRODUCTION
# ==============================
st.title("🩺 Health & Lifestyle Visualization Dashboard")
st.markdown("Analyze lifestyle habits and health conditions interactively using Plotly visualizations.")

st.markdown("""
This Streamlit application allows you to explore lifestyle habits and health conditions 
using **interactive visualizations** built with Plotly.

### 📊 Sections:
- **Objective 1–3** → Specific analyses exploring relationships between lifestyle and health.

Use the sidebar on the left to navigate between pages.
""") 

# ==============================
# 📂 LOAD DATA
# ==============================
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

# ==============================
# 🧹 CLEAN COLUMN NAMES
# ==============================
df.columns = df.columns.str.strip().str.replace(" ", "_")

# ==============================
# 🔍 DATA PREVIEW
# ==============================
with st.expander("🔍 Preview Dataset (first 10 rows)"):
    st.dataframe(df.head(10), use_container_width=True)

st.caption(f"**Total Records:** {len(df)} | **Columns:** {len(df.columns)}")

# Show column list to verify correct naming
# st.write("🧾 **Columns in dataset:**")
# st.code(list(df.columns))

# # ==============================
# # ✅ CHECK REQUIRED COLUMNS
# # ==============================
# required_cols = [
#     "Gender",
#     "Alcohol_Consumption",
#     "Smoking_Habit",
#     "Sleep_Issues",
#     "Mental_Health_Frequency",
#     "Age_Group",
#     "Current_Health_Conditions",
#     "Diet_Type",
#     "Water_Intake_per_Day"
# ]

# missing = [c for c in required_cols if c not in df.columns]
# if missing:
#     st.error(
#         "🚨 The dataset is missing expected columns needed for the visualizations:\n\n"
#         f"{missing}\n\n"
#         "Please check your CSV header names (they are case-sensitive)."
#     )
#     st.stop()
# else:
#     st.success("✅ All required columns are present!")

