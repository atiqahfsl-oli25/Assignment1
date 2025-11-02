import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Objective 2: Physical Health")

# --- Load Data ---
url = 'https://raw.githubusercontent.com/atiqahfsl-oli25/Assignment1/refs/heads/main/dataframe.csv' 
df = pd.read_csv(url)

# --- Summary Section ---
st.subheader("📋 Summary Overview")

# 1️⃣ Smoking Habit Summary
smoking_counts_male = df[df['Gender']=='Male']['Smoking Habit'].value_counts()
smoking_counts_female = df[df['Gender']=='Female']['Smoking Habit'].value_counts()

# 2️⃣ Current Health Conditions Summary
avg_health_by_smoking = df.groupby('Smoking Habit')['Current Health Conditions'].mean()

# 3️⃣ Average Health by Age Group
avg_health_by_age = df.groupby('Age Group')['Current Health Conditions'].mean()

# --- Display Summary Boxes ---
st.markdown("### Smoking Habit by Gender")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**Male**")
    for value, count in smoking_counts_male.items():
        st.metric(label=value, value=count)
with col2:
    st.markdown("**Female**")
    for value, count in smoking_counts_female.items():
        st.metric(label=value, value=count)

st.markdown("### Average Current Health Conditions by Smoking Habit")
for habit, avg in avg_health_by_smoking.items():
    st.metric(label=habit, value=f"{avg:.2f}")

st.markdown("### Average Current Health Conditions by Age Group")
for age_group, avg in avg_health_by_age.items():
    st.metric(label=age_group, value=f"{avg:.2f}")


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

# Interpretation
st.markdown("""
**Interpretation:**  
This histogram shows how smoking habits vary by gender. We can quickly see which gender has higher prevalence for each category (e.g., 'Non-Smoker', 'Occasional', 'Regular'). This insight helps understand gender-based differences in smoking, which can impact overall physical health.
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

# Interpretation
st.markdown("""
**Interpretation:**  
The violin plot shows the distribution of current health conditions for different smoking habits. The wider sections indicate more respondents with that health condition score. Generally, heavier smokers may show higher average health condition issues, highlighting the impact of smoking on physical health.
""")


# --- 3. Average Current Health Conditions by Age Group ---
st.subheader("🩺 3. Average Current Health Conditions by Age Group")
health_conditions_by_age = df.groupby('Age Group')['Current Health Conditions'].mean().reset_index()
fig = px.line(
    data_frame=health_conditions_by_age,
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

# Interpretation
st.markdown("""
**Interpretation:**  
The line plot shows how the average current health condition changes across different age groups. We can observe trends such as increasing health issues with age, which helps identify which age groups may need more health interventions or monitoring.
""")
