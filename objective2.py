import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Objective 2: Physical Health")

# --- Load Data ---
url = 'https://raw.githubusercontent.com/atiqahfsl-oli25/Assignment1/refs/heads/main/dataframe.csv' 
df = pd.read_csv(url)

# --- Summary Section ---
st.subheader("📋 Summary Overview")

# 1️⃣ Smoking Habit Distribution
smoking_counts = df['Smoking Habit'].value_counts()

# 2️⃣ Current Health Conditions by Smoking Habit
health_mean_by_smoking = df.groupby('Smoking Habit')['Current Health Conditions'].mean()

# 3️⃣ Average Current Health Conditions by Age Group
health_mean_by_age = df.groupby('Age Group')['Current Health Conditions'].mean()

# Display Summary Boxes
st.markdown("### Smoking Habit Distribution")
for habit, count in smoking_counts.items():
    st.metric(label=str(habit), value=int(count))

st.markdown("### Average Current Health Conditions by Smoking Habit")
for habit, avg in health_mean_by_smoking.items():
    st.metric(label=str(habit), value=f"{avg:.2f}")

st.markdown("### Average Current Health Conditions by Age Group")
for age_group, avg in health_mean_by_age.items():
    st.metric(label=f"Age Group: {age_group}", value=f"{avg:.2f}")

# --- 1. Smoking Habit Distribution by Gender ---
st.subheader("🚬 1. Smoking Habit Distribution by Gender")
fig2 = px.histogram(
    df,
    x="Smoking Habit",
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

st.markdown("""
**Interpretation:**  
This chart shows how smoking habits differ between male and female respondents. It helps identify which gender tends to smoke more and the distribution of different smoking habit categories.
""")

# --- 2. Distribution of Current Health Conditions by Smoking Habit ---
st.subheader("🎻 2. Distribution of Current Health Conditions by Smoking Habit")
fig_violin = px.violin(
    df,
    x='Smoking Habit',
    y='Current Health Conditions',
    color='Smoking Habit',
    box=True,
    points='all',
    hover_data=df.columns,
    title='Distribution Density of Current Health Conditions by Smoking Habit',
    color_discrete_sequence=px.colors.qualitative.Pastel
)
fig_violin.update_layout(
    xaxis_title="Smoking Habit",
    yaxis_title="Current Health Conditions",
    template='plotly_white',
    showlegend=False
)
st.plotly_chart(fig_violin, use_container_width=True)

st.markdown("""
**Interpretation:**  
The violin plot visualizes the distribution of health conditions across smoking habit groups. Wider sections indicate higher density of respondents at specific health condition levels. This shows how smoking may correlate with health severity.
""")

# --- 3. Average Current Health Conditions by Age Group ---
st.subheader("🩺 3. Average Current Health Conditions by Age Group")
fig = px.line(
    data_frame=health_mean_by_age.reset_index(),
    x='Age Group',
    y='Current Health Conditions',
    markers=True,
    title='Average Current Health Conditions by Age Group',
    color_discrete_sequence=['#EF553B']
)
fig.update_layout(
    xaxis_title='Age Group',
    yaxis_title='Average Current Health Conditions',
    template='plotly_white',
    hovermode='x unified'
)
fig.update_xaxes(tickangle=45)
st.plotly_chart(fig, use_container_width=True)

st.markdown("""
**Interpretation:**  
This line chart shows how the average health conditions change with age. It helps identify which age groups may be more vulnerable to health issues and can guide preventive health strategies.
""")
