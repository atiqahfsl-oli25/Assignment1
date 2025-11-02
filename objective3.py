import streamlit as st
import pandas as pd
import plotly.express as px

# --- Title ---
st.title("Objective 3: Food and Water Consumption")

# --- Load Data ---
url = 'https://raw.githubusercontent.com/atiqahfsl-oli25/Assignment1/refs/heads/main/dataframe.csv' 
df = pd.read_csv(url)

# --- Standardize Diet Type ---
df['Diet Type'] = df['Diet Type'].replace(['nonveg', 'non veg', 'non-veg'], 'none veg')

# --- Summary Section ---
st.subheader("📋 Summary Overview")

# 1️⃣ Diet Type by Gender
diet_counts_male = df[df['Gender']=='Male']['Diet Type'].value_counts()
diet_counts_female = df[df['Gender']=='Female']['Diet Type'].value_counts()

# 2️⃣ Average Water Intake
avg_water_by_age = df.groupby('Age Group')['Water Intake per Day'].mean()

# 3️⃣ Fast Food Consumption Proportion
fastfood_prop = pd.crosstab(df['Diet Type'], df['Fast Food Consumption Frequency']).apply(lambda r: r/r.sum(), axis=1)

# Display Summary Boxes
st.markdown("### Diet Type by Gender")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**Male**")
    for diet, count in diet_counts_male.items():
        st.metric(label=str(diet), value=int(count))
with col2:
    st.markdown("**Female**")
    for diet, count in diet_counts_female.items():
        st.metric(label=str(diet), value=int(count))

st.markdown("### Average Water Intake by Age Group")
for age_group, avg in avg_water_by_age.items():
    st.metric(label=f"Age Group: {age_group}", value=f"{avg:.2f} litres")

st.markdown("### Fast Food Consumption Proportion by Diet Type")
for diet_type, row in fastfood_prop.iterrows():
    proportions = ", ".join([f"{freq}: {prop:.0%}" for freq, prop in row.items()])
    st.markdown(f"**{diet_type}**: {proportions}")

# --- 1. Diet Type Distribution by Gender ---
st.subheader("🍽️ 1. Diet Type Distribution by Gender")
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

st.markdown("""
**Interpretation:**  
The pie charts show the distribution of diet types by gender. This helps identify the proportion of male and female respondents following vegetarian, none-veg, or mixed diets. Dietary patterns may influence nutritional health.
""")

# --- 2. Average Water Intake by Age Group ---
st.subheader("💧 2. Average Water Intake per Day by Age Group")
average_water_intake_by_age = df.groupby('Age Group')['Water Intake per Day'].mean().reset_index()
fig = px.line(
    data_frame=average_water_intake_by_age,
    x='Age Group',
    y='Water Intake per Day',
    markers=True,
    title='Average Water Intake per Day by Age Group',
    color_discrete_sequence=['#1f77b4']
)
fig.update_layout(
    xaxis_title='Age Group',
    yaxis_title='Average Water Intake (litres)',
    template='plotly_white',
    hovermode='x unified'
)
fig.update_xaxes(tickangle=45)
st.plotly_chart(fig, use_container_width=True)

st.markdown("""
**Interpretation:**  
The line chart shows how average daily water intake varies by age group. This helps identify age groups with insufficient hydration and promotes healthy water consumption habits.
""")

# --- 3. Proportion of Fast Food Consumption Frequency by Diet Type ---
st.subheader("🍔 3. Proportion of Fast Food Consumption Frequency by Diet Type")
contingency_table = pd.crosstab(df['Diet Type'], df['Fast Food Consumption Frequency'])
contingency_prop = contingency_table.apply(lambda r: r / r.sum(), axis=1).reset_index()
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

st.markdown("""
**Interpretation:**  
The stacked bar chart shows the proportion of respondents in each diet type who consume fast food at different frequencies. It highlights the relationship between diet type and fast food habits, which is important for understanding dietary health patterns.
""")
