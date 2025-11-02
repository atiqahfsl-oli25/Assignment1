import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🧠 Objective 3: Food and Water Consumption")

url = 'https://raw.githubusercontent.com/atiqahfsl-oli25/Assignment1/refs/heads/main/dataframe.csv' 
df = pd.read_csv(url)

st.subheader("🥗 Diet Type Distribution by Gender")
# Create grouped bar chart (equivalent to Seaborn countplot with hue)
fig_diet_gender = px.histogram(
    df,
    x="Diet Type",
    color="Gender",
    barmode="group",
    title="Diet Type by Gender",
    color_discrete_sequence=px.colors.qualitative.Set2
)
# Customize layout
fig_diet_gender.update_layout(
    xaxis_title="Diet Type",
    yaxis_title="Count",
    legend_title="Gender",
    template='plotly_white'
)
st.plotly_chart(fig_diet_gender, use_container_width=True)
