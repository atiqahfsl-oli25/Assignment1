import streamlit as st

st.set_page_config(page_title="Healthcare and Lifestyle", layout="wide")

# Pages
home = st.Page("home.py", title="🏠 Home", default=True)
objective1 = st.Page("objective1.py", title="Objective 1: Mental Health")
objective2 = st.Page("objective2.py", title="Objective 2: Physical Health")
objective3 = st.Page("objective3.py", title="Objective 3: Food and Water Consumption")

# Navigation
pg = st.navigation({
    "Main Menu": [home, objective1, objective2, objective3]
})

pg.run()
