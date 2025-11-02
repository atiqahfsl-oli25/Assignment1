import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🫀 Objective 4: Chronic Health Condition Insights")

url = "https://raw.githubusercontent.com/yourusername/yourrepo/main/dataframe.csv"
df = pd.read_csv(url)

fig = px.pie(df, names="Health_Condition", title="Distribution of Health Conditions")
st.plotly_chart(fig, use_container_width=True)

