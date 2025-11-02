import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Health Overview", layout="wide")

st.title("🩺 Health & Lifestyle Overview")

# Load dataset
url = 'https://raw.githubusercontent.com/atiqahfsl-oli25/Assignment1/refs/heads/main/dataframe.csv' 
df = pd.read_csv(url)

st.sidebar.header("Filter Options")
gender = st.sidebar.multiselect("Select Gender", options=df["Gender"].unique(), default=df["Gender"].unique())

filtered_df = df[df["Gender"].isin(gender)]

# 1️⃣ Alcohol Consumption by Gender
fig1 = px.histogram(filtered_df, x="Alcohol_Consumption", color="Gender", barmode="group", title="Alcohol Consumption by Gender")
st.plotly_chart(fig1, use_container_width=True)

# 2️⃣ Smoking Habits by Gender
fig2 = px.histogram(filtered_df, x="Smoking_Habit", color="Gender", barmode="group", title="Smoking Habits by Gender")
st.plotly_chart(fig2, use_container_width=True)

# 3️⃣ Mental Health vs Sleep Issues
fig3 = px.scatter(filtered_df, x="Sleep_Hours", y="Mental_Health_Score", color="Gender", trendline="ols", title="Mental Health vs Sleep Hours")
st.plotly_chart(fig3, use_container_width=True)

# 4️⃣ Health Conditions by Age
fig4 = px.box(filtered_df, x="Health_Condition", y="Age", color="Gender", title="Health Condition by Age Group")
st.plotly_chart(fig4, use_container_width=True)

