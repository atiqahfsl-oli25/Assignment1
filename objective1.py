# objective1.py
import streamlit as st
import pandas as pd
import plotly.express as px


def explore_data(df):
    st.header("📈 Exploratory Data Analysis")
    st.write("Preview of the dataset:")
    st.dataframe(df.head())


    # Alcohol Consumption by Gender
    st.subheader("🍷 Alcohol Consumption by Gender")
    fig = px.histogram(df, x='Gender', color='Alcohol Consumption', barmode='group',
                       title='Distribution of Alcohol Consumption by Gender',
                       color_discrete_sequence=px.colors.qualitative.Set2)
    st.plotly_chart(fig, use_container_width=True)


    # Smoking Habit Distribution by Gender
    st.subheader("🚬 Smoking Habit Distribution by Gender")
    fig2 = px.histogram(df, x='Smoking Habit', color='Gender', barmode='group',
                        title='Smoking Habit Distribution by Gender',
                        color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig2, use_container_width=True)
