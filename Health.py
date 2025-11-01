import streamlit as st
import pandas as pd
import plotly.express as px   

# --- Streamlit Page Configuration ---
st.set_page_config(page_title="Health & Lifestyle Dashboard", layout="wide")

# --- Title ---
st.title("🩺 Health & Lifestyle Visualization Dashboard")
st.markdown("Analyze lifestyle habits and health conditions interactively using Plotly visualizations.")

# --- Load Data ---
url = 'https://raw.githubusercontent.com/atiqahfsl-oli25/Assignment1/refs/heads/main/dataframe.csv'

try:
    df = pd.read_csv(url)
    st.success("✅ Data successfully loaded from GitHub!")
    st.dataframe(df.head(), use_container_width=True)
except Exception as e:
    st.error(f"❌ Error loading data: {e}")
    st.stop()

# ==============================
# Visualization 1: Alcohol Consumption by Gender
# ==============================
st.subheader("🍷 1. Distribution of Alcohol Consumption by Gender")
fig1 = px.histogram(
    df,
    x='Gender',
    color='Alcohol Consumption',
    barmode='group',
    title='Distribution of Alcohol Consumption by Gender',
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
    x='Smoking Habit',
    color='Gender',
    barmode='group',
    title='Smoking Habit Distribution by Gender',
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
# =============================
st.subheader("💤 3. Mental Health Issue Frequency vs Sleep Issues")

# Group and average data by Sleep Issues and Gender
sleep_health_mean = df.groupby(['Sleep Issues', 'Gender'])['Mental Health Frequency'].mean().reset_index()

# Now plot the aggregated data
fig3 = px.line(
    sleep_health_mean,
    x='Sleep Issues',
    y='Mental Health Frequency',
    color='Gender',
    markers=True,
    title='Mental Health Issue Frequency vs Sleep Issues',
    color_discrete_sequence=px.colors.qualitative.Set2
)

fig3.update_traces(line=dict(width=2), marker=dict(size=8, symbol='circle'))
fig3.update_layout(
    xaxis_title="Sleep Issues",
    yaxis_title="Frequency of Mental Health Issues",
    legend_title="Gender",
    template="simple_white",
    hovermode="x unified",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(showgrid=True, gridwidth=1, gridcolor='lightgray'),
    yaxis=dict(showgrid=True, gridwidth=1, gridcolor='lightgray')
)

st.plotly_chart(fig3, use_container_width=True)

# ==============================
# Visualization 4: Average Health Conditions by Age Group
# ==============================
st.subheader("👥 4. Average Current Health Conditions by Age Group")
health_conditions_by_age = df.groupby('Age Group')['Current Health Conditions'].mean().reset_index()
fig4 = px.line(
    health_conditions_by_age,
    x='Age Group',
    y='Current Health Conditions',
    markers=True,
    title='Average Current Health Conditions by Age Group',
    color_discrete_sequence=px.colors.qualitative.Safe
)
fig4.update_layout(
    xaxis_title="Age Group",
    yaxis_title="Average Current Health Conditions",
    template="simple_white",
    hovermode="x unified",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(showgrid=True, gridwidth=1, gridcolor='lightgray'),
    yaxis=dict(showgrid=True, gridwidth=1, gridcolor='lightgray')
)
st.plotly_chart(fig4, use_container_width=True)

