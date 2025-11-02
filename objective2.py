import streamlit as st
import pandas as pd
import plotly.express as px

st.title("💤 Objective 2: Physical Health")

url = 'https://raw.githubusercontent.com/atiqahfsl-oli25/Assignment1/refs/heads/main/dataframe.csv' 
df = pd.read_csv(url)

st.subheader("🚬 2. Smoking Habit Distribution by Gender")
fig2 = px.histogram(
    df,
    x="Smoking Habit",
    color="Gender",
    barmode="group",
    title="Smoking Habit Distribution by Gender",
    color_discrete_sequence=px.colors.qualitative.Pastel
)
fig2.update_layout(
    xaxis_title="Smoking Habit",
    yaxis_title="Number of Respondents",
    legend_title="Gender"
)
st.plotly_chart(fig2, use_container_width=True)

st.subheader("🎻 Distribution of Current Health Conditions by Smoking Habit")
fig_violin = px.violin(
    df,
    x='Smoking Habit',
    y='Current Health Conditions',
    color='Smoking Habit',
    box=True,             # adds inner box showing quartiles
    points='all',         # shows all data points
    hover_data=df.columns,
    title='Distribution Density of Current Health Conditions by Smoking Habit',
    color_discrete_sequence=px.colors.qualitative.Pastel
)
fig_violin.update_layout(
    xaxis_title="Smoking Habit",
    yaxis_title="Current Health Conditions",
    template='plotly_white',
    showlegend=False
)
st.plotly_chart(fig_violin, use_container_width=True)

st.subheader("🔥 2D Heatmap: Frequency of Physical Activity Level and Health Conditions")
    df['Current Health Conditions'] = pd.to_numeric(df['Current Health Conditions'], errors='coerce')
    df['Physical Activity Level'] = pd.to_numeric(df['Physical Activity Level'], errors='coerce')
    df.dropna(subset=['Current Health Conditions', 'Physical Activity Level'], inplace=True)

# Create 2D heatmap using Plotly
fig_heatmap = px.density_heatmap(
    df,
    x='Physical Activity Level',
    y='Current Health Conditions',
    nbinsx=6,  # Same as bins=6 in seaborn
    nbinsy=6,
    color_continuous_scale='Mako',
    title='2D Histogram: Frequency of Activity Level and Health Conditions'
)
# Customize layout
fig_heatmap.update_layout(
    xaxis_title="Physical Activity Level",
    yaxis_title="Current Health Conditions",
    coloraxis_colorbar_title="Frequency (Count)",
    template='plotly_white'
)
st.plotly_chart(fig_heatmap, use_container_width=True)

