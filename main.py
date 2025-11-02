import streamlit as st

st.set_page_config(page_title="Healthcare and Lifestyle", layout="wide")

# Pages
home = st.Page("home.py", title="🏠 Home", default=True)
objective1 = st.Page("objective1.py", title="🎓 Objective 1: Alcohol")
objective2 = st.Page("objective2.py", title="🌾 Objective 2: Smoking Habit")
objective3 = st.Page("objective3.py", title="🌱 Objective 3: Food and Water Consumption")
objective4 = st.Page("objective4.py", title="🌱 Objective 4: Current Health Condition")

# Navigation
pg = st.navigation({
    "Main Menu": [home, objective1, objective2, objective3, objective4]
})
pg.run()
