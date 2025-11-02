import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Objective 3: Food and Water Consumption")

url = 'https://raw.githubusercontent.com/atiqahfsl-oli25/Assignment1/refs/heads/main/dataframe.csv' 
df = pd.read_csv(url)

import streamlit as st
import plotly.express as px

import streamlit as st
import plotly.express as px

# --- Title ---
st.title("🍽️ 1.Diet Type Distribution by Gender")
df['Diet Type'] = df['Diet Type'].replace('nonveg', 'none veg')

df_male = df[df['Gender'] == 'Male']
df_female = df[df['Gender'] == 'Female']

fig_male = px.pie(
    df_male,
    names='Diet Type',
    title='Diet Type Distribution for Male',
    hole=0.4,
    color_discrete_sequence=px.colors.qualitative.Pastel
)
fig_female = px.pie(
    df_female,
    names='Diet Type',
    title='Diet Type Distribution for Female',
    hole=0.4,
    color_discrete_sequence=px.colors.qualitative.Pastel
)
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig_male, use_container_width=True)
with col2:
    st.plotly_chart(fig_female, use_container_width=True)

st.subheader("💧 2.Average Water Intake per Day by Age Group")
average_water_intake_by_age = df.groupby('Age Group')['Water Intake per Day'].mean().reset_index()
fig = px.line(
    data_frame=average_water_intake_by_age,
    x='Age Group',
    y='Water Intake per Day',
    markers=True,
    title='Average Water Intake per Day by Age Group',
    color_discrete_sequence=['#1f77b4']  # Blue color tone
)
fig.update_layout(
    xaxis_title='Age Group',
    yaxis_title='Average Water Intake (litres)',
    template='plotly_white',
    hovermode='x unified'
)
fig.update_xaxes(tickangle=45)
st.plotly_chart(fig, use_container_width=True)

st.subheader("🍔 3.Proportion of Fast Food Consumption Frequency by Diet Type")
# Create a contingency table (cross-tabulation)
contingency_table = pd.crosstab(df['Diet Type'], df['Fast Food Consumption Frequency'])

# Normalize to get proportions (percentages)
contingency_prop = contingency_table.apply(lambda r: r / r.sum(), axis=1).reset_index()

# Melt the table for Plotly (long format)
contingency_melted = contingency_prop.melt(id_vars='Diet Type', 
                                           var_name='Fast Food Consumption Frequency', 
                                           value_name='Proportion')
fig = px.bar(
    contingency_melted,
    x='Diet Type',
    y='Proportion',
    color='Fast Food Consumption Frequency',
    title='Proportion of Fast Food Consumption Frequency by Diet Type',
    text=contingency_melted['Proportion'].apply(lambda x: f"{x:.0%}"),
    color_discrete_sequence=px.colors.qualitative.Pastel
)
fig.update_layout(
    barmode='stack',
    xaxis_title='Diet Type',
    yaxis_title='Proportion (1.0 = 100%)',
    template='plotly_white',
    legend_title_text='Fast Food Frequency'
)
fig.update_yaxes(tickformat=".0%")
st.plotly_chart(fig, use_container_width=True)






