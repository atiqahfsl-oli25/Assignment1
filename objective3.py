import streamlit as st
import plotly.express as px


def visualize_relationships(df):
st.header("💤 Mental Health & Sleep Relationship")


sleep_health_mean = df.groupby(['Sleep Issues', 'Gender'])['Mental Health Frequency'].mean().reset_index()
fig = px.line(sleep_health_mean, x='Sleep Issues', y='Mental Health Frequency', color='Gender',
markers=True, title='Mental Health Issue Frequency vs Sleep Issues',
color_discrete_sequence=px.colors.qualitative.Set2)
st.plotly_chart(fig, use_container_width=True)
