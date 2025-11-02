import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🎯 Objective 1: Physical Activity Analysis")

url = 'https://raw.githubusercontent.com/atiqahfsl-oli25/Assignment1/refs/heads/main/dataframe.csv'  
df = pd.read_csv(url)

fig = px.histogram(df, x="Physical_Activity_Label", color="Gender", barmode="group", title="Physical Activity Level by Gender")
st.plotly_chart(fig, use_container_width=True)
