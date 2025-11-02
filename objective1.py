import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Objective 1: to quantify how Alcohol Consumption affects Sleep Duration")

# --- Load Data ---
url = 'https://raw.githubusercontent.com/atiqahfsl-oli25/Assignment1/refs/heads/main/dataframe.csv'  
df = pd.read_csv(url)

# --- Standardize categories ---
if 'Alcohol Consumption' in df.columns:
    df['Alcohol Consumption'] = pd.Categorical(df['Alcohol Consumption'], categories=['No', 'Yes'], ordered=True)

# --- Summary Section ---
st.subheader("📋 Summary Overview")

# Alcohol Consumption Summary
alcohol_male_counts = df[df['Gender']=='Male']['Alcohol Consumption'].value_counts()
alcohol_female_counts = df[df['Gender']=='Female']['Alcohol Consumption'].value_counts()

# Mental Health Frequency Summary
avg_mh_by_gender = df.groupby('Gender')['Mental Health Frequency'].mean()

# Sleep Duration Summary
avg_sleep_by_alcohol = df.groupby('Alcohol Consumption')['Sleep Duration'].mean()

# Display Summary Boxes
st.markdown("### Alcohol Consumption by Gender")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**Male**")
    for value, count in alcohol_male_counts.items():
        st.metric(label=value, value=count)
with col2:
    st.markdown("**Female**")
    for value, count in alcohol_female_counts.items():
        st.metric(label=value, value=count)

st.markdown("### Average Mental Health Frequency by Gender")
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Male Avg Frequency", value=f"{avg_mh_by_gender.get('Male',0):.2f}")
with col2:
    st.metric(label="Female Avg Frequency", value=f"{avg_mh_by_gender.get('Female',0):.2f}")

st.markdown("### Average Sleep Duration by Alcohol Consumption")
col1, col2 = st.columns(2)
with col1:
    st.metric(label="No Alcohol", value=f"{avg_sleep_by_alcohol.get('No',0):.2f} hrs")
with col2:
    st.metric(label="Yes Alcohol", value=f"{avg_sleep_by_alcohol.get('Yes',0):.2f} hrs")


# --- 1. Alcohol Consumption by Gender ---
st.subheader("🍷 1. Distribution of Alcohol Consumption by Gender")
fig1 = px.histogram(
    df,
    x="Gender",
    color="Alcohol Consumption",
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

# Interpretation
st.markdown("""
**Interpretation:**  
From the histogram, we can see how alcohol consumption varies between male and female respondents. For example, males might show a higher count of "Yes" for alcohol consumption compared to females. This helps understand gender differences in alcohol use, which could influence mental health patterns.
""")


# --- 2. Mental Health Frequency vs Sleep Issues ---
st.subheader("💤 2. Mental Health Issue Frequency vs Sleep Issues")
sleep_health_mean = df.groupby(['Sleep Issues', 'Gender'])['Mental Health Frequency'].mean().reset_index()
fig2 = px.line(
    sleep_health_mean,
    x='Sleep Issues',
    y='Mental Health Frequency',
    color='Gender',
    markers=True,
    title='Mental Health Issue Frequency vs Sleep Issues',
    color_discrete_sequence=px.colors.qualitative.Set2
)
fig2.update_traces(line=dict(width=2), marker=dict(size=8, symbol='circle'))
fig2.update_layout(
    xaxis_title="Sleep Issues",
    yaxis_title="Frequency of Mental Health Issues",
    legend_title="Gender",
    template="simple_white",
    hovermode="x unified",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(showgrid=True, gridwidth=1, gridcolor='lightgray'),
    yaxis=dict(showgrid=True, gridwidth=1, gridcolor='lightgray')
)
st.plotly_chart(fig2, use_container_width=True)

# Interpretation
st.markdown("""
**Interpretation:**  
The line plot shows the relationship between sleep issues and the frequency of mental health problems for each gender. Generally, as sleep issues increase, the frequency of mental health issues also tends to rise. Differences between genders can highlight if one gender is more affected by poor sleep.
""")


# --- 3. Sleep Duration by Alcohol Consumption ---
st.subheader("🧃 3. Distribution of Sleep Duration by Alcohol Consumption")
fig3 = px.box(
    df,
    x='Alcohol Consumption',
    y='Sleep Duration',
    color='Alcohol Consumption',
    title='Distribution of Sleep Duration by Alcohol Consumption',
    color_discrete_sequence=px.colors.sequential.Viridis
)
fig3.update_layout(
    xaxis_title="Alcohol Consumption",
    yaxis_title="Sleep Duration (Hours)",
    template='plotly_white',
    showlegend=False
)
st.plotly_chart(fig3, use_container_width=True)

# Interpretation
st.markdown("""
**Interpretation:**  
The box plot compares sleep duration between respondents who consume alcohol and those who do not. For example, alcohol consumers might show slightly lower median sleep hours or a wider range of sleep duration, suggesting that alcohol consumption could be associated with disrupted sleep patterns, which may impact mental health.
""")
