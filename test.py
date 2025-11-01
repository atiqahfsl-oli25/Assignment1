import streamlit as st

st.set_page_config(
    page_title="Online Learning Survey",
    layout="wide"
)

# Define your pages
home = st.Page("home.py", title="Homepage", icon=":material/home:", default=True)
page1 = st.Page("Health.py", title="Kepuasan Pelajar Dalam Pembelajaran", icon=":material/thumb_up_off_alt:")

# Group pages into navigation
pg = st.navigation({
    "Menu": [home, page1, page2]
})

# Run navigation
pg.run()
