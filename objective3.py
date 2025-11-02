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

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- Streamlit Page Configuration ---
st.set_page_config(page_title="Diet Type Distribution by Gender", layout="wide")

# --- Title ---
st.title("🥗 Diet Type Distribution by Gender")
df['Diet Type'] = df['Diet Type'].replace('nonveg', 'non veg')

df_male = df[df['Gender'] == 'Male']
df_female = df[df['Gender'] == 'Female']

diet_counts_male = df_male['Diet Type'].value_counts()
diet_counts_female = df_female['Diet Type'].value_counts()
fig = go.Figure()

# Male Pie
fig.add_trace(go.Pie(
    labels=diet_counts_male.index,
    values=diet_counts_male.values,
    name="Male",
    hole=0.3,
    domain={'x': [0, 0.45]},
    textinfo='percent+label',
    marker=dict(colors=['#66b3ff', '#99ff99', '#ffcc99', '#ff9999'])
))
# Female Pie
fig.add_trace(go.Pie(
    labels=diet_counts_female.index,
    values=diet_counts_female.values,
    name="Female",
    hole=0.3,
    domain={'x': [0.55, 1]},
    textinfo='percent+label',
    marker=dict(colors=['#ffb3e6', '#c2f0c2', '#ffcc99', '#ff9999'])
))
fig.update_layout(
    title_text="Diet Type Distribution for Male and Female",
    annotations=[
        dict(text='Male', x=0.20, y=0.5, font_size=16, showarrow=False),
        dict(text='Female', x=0.8, y=0.5, font_size=16, showarrow=False)
    ]
)
st.plotly_chart(fig, use_container_width=True)

st.subheader("💧 Average Water Intake per Day by Age Group")
average_water_intake_by_age = df.groupby('Age Group')['Water Intake per Day'].mean().reset_index()
fig = px.line(
    average_water_intake_by_age,
    x='Age Group',
    y='Water Intake per Day',
    markers=True,
    title='Average Water Intake per Day by Age Group',
    line_shape='linear',
    color_discrete_sequence=['#1f77b4']
)
fig.update_layout(
    xaxis_title="Age Group",
    yaxis_title="Average Water Intake (litres)",
    template="plotly_white",
    hovermode="x unified"
)
st.plotly_chart(fig, use_container_width=True)


