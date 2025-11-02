import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Objective 1: Mental Health")

url = 'https://raw.githubusercontent.com/atiqahfsl-oli25/Assignment1/refs/heads/main/dataframe.csv'  
df = pd.read_csv(url)

# --- 1. Distribution of Alcohol Consumption by Gender ---
st.subheader("🍷 1. Distribution of Alcohol Consumption by Gender")

# --- Summary Box for Alcohol Consumption ---
male_counts = df[df['Gender']=='Male']['Alcohol Consumption'].value_counts()
female_counts = df[df['Gender']=='Female']['Alcohol Consumption'].value_counts()

st.markdown("**Summary of Alcohol Consumption by Gender:**")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**Male**")
    for value, count in male_counts.items():
        st.metric(label=value, value=count)
with col2:
    st.markdown("**Female**")
    for value, count in female_counts.items():
        st.metric(label=value, value=count)

# Histogram
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


# --- 2. Mental Health Issue Frequency vs Sleep Issues ---
st.subheader("💤 2. Mental Health Issue Frequency vs Sleep Issues")

# Group and average data by Sleep Issues and Gender
sleep_health_mean = df.groupby(['Sleep Issues', 'Gender'])['Mental Health Frequency'].mean().reset_index()

# --- Summary Box for Mental Health Frequency ---
st.markdown("**Average Mental Health Frequency by Gender:**")
avg_mh_by_gender = df.groupby('Gender')['Mental Health Frequency'].mean()
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Male Avg Frequency", value=f"{avg_mh_by_gender.get('Male',0):.2f}")
with col2:
    st.metric(label="Female Avg Frequency", value=f"{avg_mh_by_gender.get('Female',0):.2f}")

# Line plot
fig = px.line(
    sleep_health_mean,
    x='Sleep Issues',
    y='Mental Health Frequency',
    color='Gender',
    markers=True,
    title='Mental Health Issue Frequency vs Sleep Issues',
    color_discrete_sequence=px.colors.qualitative.Set2
)
fig.update_traces(line=dict(width=2), marker=dict(size=8, symbol='circle'))
fig.update_layout(
    xaxis_title="Sleep Issues",
    yaxis_title="Frequency of Mental Health Issues",
    legend_title="Gender",
    template="simple_white",
    hovermode="x unified",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(showgrid=True, gridwidth=1, gridcolor='lightgray'),
    yaxis=dict(showgrid=True, gridwidth=1, gridcolor='lightgray')
)
st.plotly_chart(fig, use_container_width=True)


# --- 3. Distribution of Sleep Duration by Alcohol Consumption ---
st.subheader("🧃 3. Distribution of Sleep Duration by Alcohol Consumption")

if 'Alcohol Consumption' in df.columns:
    df['Alcohol Consumption'] = pd.Categorical(df['Alcohol Consumption'], categories=['No', 'Yes'], ordered=True)

# Summary Box for Sleep Duration
st.markdown("**Average Sleep Duration by Alcohol Consumption:**")
avg_sleep = df.groupby('Alcohol Consumption')['Sleep Duration'].mean()
col1, col2 = st.columns(2)
with col1:
    st.metric(label="No Alcohol", value=f"{avg_sleep.get('No',0):.2f} hrs")
with col2:
    st.metric(label="Yes Alcohol", value=f"{avg_sleep.get('Yes',0):.2f} hrs")

# Box plot
fig_box = px.box(
    df,
    x='Alcohol Consumption',
    y='Sleep Duration',
    color='Alcohol Consumption',
    title='Distribution of Sleep Duration by Alcohol Consumption',
    color_discrete_sequence=px.colors.sequential.Viridis
)
fig_box.update_layout(
    xaxis_title="Alcohol Consumption",
    yaxis_title="Sleep Duration (Hours)",
    template='plotly_white',
    showlegend=False
)
st.plotly_chart(fig_box, use_container_width=True)
