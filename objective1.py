import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🎯 Objective 1: Mental Health")

url = 'https://raw.githubusercontent.com/atiqahfsl-oli25/Assignment1/refs/heads/main/dataframe.csv'  
df = pd.read_csv(url)

st.subheader("🍷 1. Distribution of Alcohol Consumption by Gender")
fig1 = px.histogram(
    df,
    x="Gender",
    color="Alcohol Consumption",
    barmode="group",
    title="Distribution of Alcohol Consumption by Gender",
    color_discrete_sequence=px.colors.qualitative.Set2
)
fig1.update_layout(
    xaxis_title="Gender",
    yaxis_title="Number of Respondents",
    legend_title="Alcohol Consumption"
)
st.plotly_chart(fig1, use_container_width=True)

st.title("🧠 Mental Health Frequency vs Sleep Issues")
st.markdown("""
This interactive line chart shows how **mental health issue frequency** varies 
based on **sleep issues**, categorized by **gender**.
""")

# --- Create Plotly Line Chart ---
fig = px.line(
    df,
    x="Sleep Issues",
    y="Mental Health Frequency",
    color="Gender",
    markers=True,
    title="Mental Health Issue Frequency vs Sleep Issues",
    line_shape="linear",
    color_discrete_sequence=px.colors.qualitative.Pastel
)

# --- Customize Layout ---
fig.update_layout(
    xaxis_title="Sleep Issues",
    yaxis_title="Frequency of Mental Health Issues",
    template="plotly_white",
    legend_title="Gender",
    legend=dict(x=1, y=1),
)

# --- Show Chart ---
st.plotly_chart(fig, use_container_width=True)
