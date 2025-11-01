import streamlit as st

st.set_page_config(
    page_title="Online Learning Survey"
)

page1 = st.Page('Health.py', title='Kepuasan Pelajar Dalam Pembelajaran', icon=":material/thumb_up_off_alt:")

home = st.Page('Homepage.py', title='Homepage', default=True, icon=":material/home:")

pg = st.navigation(
        {
            "Menu": [home, page1, page2]
        }
    )

pg.run()
