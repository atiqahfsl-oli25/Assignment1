import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🫀 Objective 4: Chronic Health Condition Insights")

url = 'https://raw.githubusercontent.com/atiqahfsl-oli25/Assignment1/refs/heads/main/dataframe.csv' 
df = pd.read_csv(url)

fig = px.pie(df, names="Current Health Conditions", title="Distribution of Health Conditions")
st.plotly_chart(fig, use_container_width=True)

