import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🧠 Objective 3: Mental Health & Lifestyle")

url = 'https://raw.githubusercontent.com/atiqahfsl-oli25/Assignment1/refs/heads/main/dataframe.csv' 
df = pd.read_csv(url)

st.subheader("💤 3. Mental Health Issue Frequency vs Sleep Issues")

# Convert to numeric safely
df["Mental_Health_Frequency"] = pd.to_numeric(df["Mental Health Frequency"], errors="coerce")

sleep_health_mean = (
    df.groupby(["Sleep Issues", "Gender"])["Mental Health Frequency"].mean().reset_index()
)

fig3 = px.line(
    sleep_health_mean,
    x="Sleep Issues",
    y="Mental Health Frequency",
    color="Gender",
    markers=True,
    title="Mental Health Issue Frequency vs Sleep Issues",
    color_discrete_sequence=px.colors.qualitative.Set2
)

fig3.update_traces(line=dict(width=2), marker=dict(size=8, symbol="circle"))
fig3.update_layout(
    xaxis_title="Sleep Issues",
    yaxis_title="Frequency of Mental Health Issues",
    legend_title="Gender",
    template="simple_white",
    hovermode="x unified",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(showgrid=True, gridwidth=1, gridcolor="lightgray"),
    yaxis=dict(showgrid=True, gridwidth=1, gridcolor="lightgray")
)
st.plotly_chart(fig3, use_container_width=True)
