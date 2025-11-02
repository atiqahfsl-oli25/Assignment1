import streamlit as st
import plotly.express as px


def visualize_health_conditions(df):
st.header("👥 Average Health Conditions by Age Group")


health_conditions_by_age = df.groupby('Age Group')['Current Health Conditions'].mean().reset_index()
fig = px.line(health_conditions_by_age, x='Age Group', y='Current Health Conditions', markers=True,
title='Average Current Health Conditions by Age Group',
color_discrete_sequence=px.colors.qualitative.Safe)
st.plotly_chart(fig, use_container_width=True)
