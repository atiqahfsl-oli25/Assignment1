import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🧩 Test & Validation Page")

url = 'https://raw.githubusercontent.com/atiqahfsl-oli25/Assignment1/refs/heads/main/dataframe.csv' 
df = pd.read_csv(url)

st.write("Sample of the dataset:")
st.dataframe(df.head())

st.success("Data loaded successfully! ✅")

