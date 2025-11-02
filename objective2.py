import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Objective 2: Physical Health")

url = 'https://raw.githubusercontent.com/atiqahfsl-oli25/Assignment1/refs/heads/main/dataframe.csv' 
df = pd.read_csv(url)

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

st.subheader("🎻 2.Distribution of Current Health Conditions by Smoking Habit")
fig_violin = px.violin(
    df,
    x='Smoking Habit',
    y='Current Health Conditions',
    color='Smoking Habit',
    box=True,             # adds inner box showing quartiles
    points='all',         # shows all data points
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

st.subheader("🩺 3.Average Current Health Conditions by Age Group")
health_conditions_by_age = df.groupby('Age Group')['Current Health Conditions'].mean().reset_index()
fig = px.line(
    data_frame=health_conditions_by_age,
    x='Age Group',
    y='Current Health Conditions',
    markers=True,
    title='Average Current Health Conditions by Age Group',
    color_discrete_sequence=['#EF553B']  # soft red color
)
fig.update_layout(
    xaxis_title='Age Group',
    yaxis_title='Average Current Health Conditions',
    template='plotly_white',
    hovermode='x unified'
)
fig.update_xaxes(tickangle=45)
st.plotly_chart(fig, use_container_width=True)

