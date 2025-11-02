import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🎯 Objective 1: Mental Health")

url = 'https://raw.githubusercontent.com/atiqahfsl-oli25/Assignment1/refs/heads/main/dataframe.csv'  
df = pd.read_csv(url)

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

st.subheader("💤 3. Mental Health Issue Frequency vs Sleep Issues")
# Group and average data by Sleep Issues and Gender
sleep_health_mean = df.groupby(['Sleep Issues', 'Gender'])['Mental Health Frequency'].mean().reset_index()

# Now plot the aggregated data
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

st.plotly_chart(fig3, use_container_width=True)
