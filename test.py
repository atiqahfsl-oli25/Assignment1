import streamlit as st
import pandas as pd

st.title("🧩 Test & Validation Page")

url = "https://raw.githubusercontent.com/yourusername/yourrepo/main/dataframe.csv"
df = pd.read_csv(url)

st.write("Sample of the dataset:")
st.dataframe(df.head())

st.success("Data loaded successfully! ✅")

