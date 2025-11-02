import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🧠 Objective 3: Food and Water Consumption")

url = 'https://raw.githubusercontent.com/atiqahfsl-oli25/Assignment1/refs/heads/main/dataframe.csv' 
df = pd.read_csv(url)

st.subheader("🥗 1. Diet Type Distribution by Gender")
df_male = df[df['Gender'] == 'Male']
df_female = df[df['Gender'] == 'Female']

diet_counts_male = df_male['Diet Type'].value_counts().reset_index()
diet_counts_male.columns = ['Diet Type', 'Count']

diet_counts_female = df_female['Diet Type'].value_counts().reset_index()
diet_counts_female.columns = ['Diet Type', 'Count']

col1, col2 = st.columns(2)

    with col1:
        fig_male = px.pie(
            diet_counts_male,
            names='Diet Type',
            values='Count',
            title="Diet Type Distribution for Male",
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig_male.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig_male, use_container_width=True)

    with col2:
        fig_female = px.pie(
        diet_counts_female,
        names='Diet Type',
        values='Count',
        title="Diet Type Distribution for Female",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    fig_female.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_female, use_container_width=True)

 
st.subheader("💧 2. Average Water Intake per Day by Age Group")
average_water_intake_by_age = (
    df.groupby('Age Group')['Water Intake per Day']
    .mean()
    .reset_index()
    .sort_values('Age Group')
)
fig_line = px.line(
    average_water_intake_by_age,
    x='Age Group',
    y='Water Intake per Day',
    markers=True,
    title="Average Water Intake per Day by Age Group",
    color_discrete_sequence=px.colors.qualitative.Pastel
)
fig_line.update_layout(
    xaxis_title="Age Group",
    yaxis_title="Average Water Intake (litres)",
    legend_title_text="",
    template='plotly_white'
 )
 st.plotly_chart(fig_line, use_container_width=True)
