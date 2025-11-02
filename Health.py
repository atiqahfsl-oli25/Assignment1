# Health.py
import streamlit as st
import pandas as pd
import plotly.express as px

# --- Streamlit Page Configuration ---
st.set_page_config(page_title="Health & Lifestyle Dashboard", layout="wide")

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to:",
    ["Overview", "Alcohol", "Smoking", "Sleep & Mental Health", "Health Conditions"]
)

st.sidebar.markdown("---")
st.sidebar.write("📊 Use the sidebar to navigate through the visualizations.")


# --- Title ---
st.title("🩺 Health & Lifestyle Visualization Dashboard")
st.markdown("Analyze lifestyle habits and health conditions interactively using Plotly visualizations.")

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
df.columns = df.columns.str.strip().str.replace(" ", "_")

st.dataframe(df.head(), use_container_width=True)

# --- Check Columns Needed ---
required_cols = [
    "Gender",
    "Alcohol_Consumption",
    "Smoking_Habit",
    "Sleep_Issues",
    "Mental_Health_Frequency",
    "Age_Group",
    "Current_Health_Conditions"
]

missing = [c for c in required_cols if c not in df.columns]
if missing:
    st.error(
        "The dataset is missing expected columns needed for the visualizations:\n\n"
        f"{missing}\n\n"
        "Please check your CSV header names (they are case-sensitive)."
    )
    st.stop()

# ==============================
# Visualization 1: Alcohol Consumption by Gender
# ==============================
st.subheader("🍷 1. Distribution of Alcohol Consumption by Gender")
fig1 = px.histogram(
    df,
    x="Gender",
    color="Alcohol_Consumption",
    barmode="group",
    title="Distribution of Alcohol Consumption by Gender",
    color_discrete_sequence=px.colors.qualitative.Set2
)
fig1.update_layout(
    xaxis_title="Gender",
    yaxis_title="Number of Respondents",
    legend_title="Alcohol Consumption"
)
st.plotly_chart(fig1, use_container_width=True)

# ==============================
# Visualization 2: Smoking Habit Distribution by Gender
# ==============================
st.subheader("🚬 2. Smoking Habit Distribution by Gender")
fig2 = px.histogram(
    df,
    x="Smoking_Habit",
    color="Gender",
    barmode="group",
    title="Smoking Habit Distribution by Gender",
    color_discrete_sequence=px.colors.qualitative.Pastel
)
fig2.update_layout(
    xaxis_title="Smoking Habit",
    yaxis_title="Number of Respondents",
    legend_title="Gender"
)
st.plotly_chart(fig2, use_container_width=True)

# ==============================
# Visualization 3: Mental Health Frequency vs Sleep Issues
# ==============================
st.subheader("💤 3. Mental Health Issue Frequency vs Sleep Issues")

# Convert to numeric safely
df["Mental_Health_Frequency"] = pd.to_numeric(df["Mental_Health_Frequency"], errors="coerce")

sleep_health_mean = (
    df.groupby(["Sleep_Issues", "Gender"])["Mental_Health_Frequency"].mean().reset_index()
)

fig3 = px.line(
    sleep_health_mean,
    x="Sleep_Issues",
    y="Mental_Health_Frequency",
    color="Gender",
    markers=True,
    title="Mental Health Issue Frequency vs Sleep Issues",
    color_discrete_sequence=px.colors.qualitative.Set2
)

fig3.update_traces(line=dict(width=2), marker=dict(size=8, symbol="circle"))
fig3.update_layout(
    xaxis_title="Sleep Issues",
    yaxis_title="Frequency of Mental Health Issues",
    legend_title="Gender",
    template="simple_white",
    hovermode="x unified",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(showgrid=True, gridwidth=1, gridcolor="lightgray"),
    yaxis=dict(showgrid=True, gridwidth=1, gridcolor="lightgray")
)
st.plotly_chart(fig3, use_container_width=True)

# ==============================
# Visualization 4: Average Health Conditions by Age Group
# ==============================
st.subheader("👥 4. Average Current Health Conditions by Age Group")

df["Current_Health_Conditions"] = pd.to_numeric(df["Current_Health_Conditions"], errors="coerce")
health_conditions_by_age = df.groupby("Age_Group")["Current_Health_Conditions"].mean().reset_index()

fig4 = px.line(
    health_conditions_by_age,
    x="Age_Group",
    y="Current_Health_Conditions",
    markers=True,
    title="Average Current Health Conditions by Age Group",
    color_discrete_sequence=px.colors.qualitative.Safe
)
fig4.update_layout(
    xaxis_title="Age Group",
    yaxis_title="Average Current Health Conditions",
    template="simple_white",
    hovermode="x unified",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(showgrid=True, gridwidth=1, gridcolor="lightgray"),
    yaxis=dict(showgrid=True, gridwidth=1, gridcolor="lightgray")
)
st.plotly_chart(fig4, use_container_width=True)
