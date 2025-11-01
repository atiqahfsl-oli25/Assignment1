import streamlit as st

st.set_page_config(
    page_title="Health and Lifestyle" 
)

visualise = st.Page('Health.py', title='Health Among Citizen', icon=":material/school:")

home = st.Page('home.py', title='Homepage', default=True, icon=":material/home:") 

pg = st.navigation(
        {
            "Menu": [home, visualise]
        }
    )

pg.run()
