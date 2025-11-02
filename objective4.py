import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🫀 Objective 4: Chronic Health Condition Insights")

url = 'https://raw.githubusercontent.com/atiqahfsl-oli25/Assignment1/refs/heads/main/dataframe.csv' 
df = pd.read_csv(url)

st.subheader("👥 4. Average Current Health Conditions by Age Group")

df["Current Health Conditions"] = pd.to_numeric(df["Current Health Conditions"], errors="coerce")
health_conditions_by_age = df.groupby("Age Group")["Current Health Conditions"].mean().reset_index()

fig4 = px.line(
    health_conditions_by_age,
    x="Age Group",
    y="Current Health Conditions",
    markers=True,
    title="Average Current Health Conditions by Age Group",
    color_discrete_sequence=px.colors.qualitative.Safe
)
fig4.update_layout(
    xaxis_title="Age Group",
    yaxis_title="Average Current Health Conditions",
    template="simple_white",
    hovermode="x unified",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(showgrid=True, gridwidth=1, gridcolor="lightgray"),
    yaxis=dict(showgrid=True, gridwidth=1, gridcolor="lightgray")
)
st.plotly_chart(fig4, use_container_width=True)


