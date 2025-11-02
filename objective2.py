import streamlit as st
import pandas as pd
import plotly.express as px

st.title("💤 Objective 2: Sleep Pattern Analysis")

url = 'https://raw.githubusercontent.com/atiqahfsl-oli25/Assignment1/refs/heads/main/dataframe.csv' 
df = pd.read_csv(url)

fig = px.box(df, x="Gender", y="Sleep Duration", color="Gender", title="Sleep Hours Distribution by Gender")
st.plotly_chart(fig, use_container_width=True)

