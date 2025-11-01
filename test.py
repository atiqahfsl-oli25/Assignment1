# test.py
import streamlit as st

st.set_page_config(page_title="Student Survey", page_icon="🎓")

# Homepage content
st.title("🏠 Home Page — Student Survey")

st.markdown("""
Welcome to the **Student Health & Lifestyle Dashboard**!  
Use the sidebar to navigate between pages.
""")

# You can add any homepage visuals or info here
st.image("https://raw.githubusercontent.com/fakhitah3/FHPK-TVET/main/3u1i.jpeg", use_container_width=True)

streamlit run test.py

