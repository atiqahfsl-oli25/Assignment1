import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🧠 Objective 3: Mental Health & Lifestyle")

url = "https://raw.githubusercontent.com/yourusername/yourrepo/main/dataframe.csv"
df = pd.read_csv(url)

fig = px.scatter(df, x="Stress_Level", y="Mental_Health_Score", color="Gender", trendline="ols", title="Stress vs Mental Health Score")
st.plotly_chart(fig, use_container_width=True)
