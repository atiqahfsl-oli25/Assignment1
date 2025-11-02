import streamlit as st
import pandas as pd
import plotly.express as px

st.title("💤 Objective 2: Sleep Pattern Analysis")

url = "https://raw.githubusercontent.com/yourusername/yourrepo/main/dataframe.csv"
df = pd.read_csv(url)

fig = px.box(df, x="Gender", y="Sleep_Hours", color="Gender", title="Sleep Hours Distribution by Gender")
st.plotly_chart(fig, use_container_width=True)

