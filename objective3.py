import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🧠 Objective 3: Food and Water Consumption")

url = 'https://raw.githubusercontent.com/atiqahfsl-oli25/Assignment1/refs/heads/main/dataframe.csv' 
df = pd.read_csv(url)

st.title("🥗 Diet Type by Gender Visualization")
df['Diet Type'] = df['Diet Type'].replace('nonveg', 'non veg')
fig = px.bar(
    df,
    x='Diet Type',
    color='Gender',
    barmode='group',
    title='Diet Type by Gender',
    color_discrete_sequence=px.colors.qualitative.Set2
)
fig.update_layout(
    xaxis_title="Diet Type",
    yaxis_title="Count",
    title_font=dict(size=20, color='darkblue'),
    plot_bgcolor='white',
    legend_title_text='Gender'
)
st.plotly_chart(fig, use_container_width=True)
