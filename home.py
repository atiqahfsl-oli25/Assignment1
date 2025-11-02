# home.py
import streamlit as st


def render_home():
st.header("🏠 Welcome to the Health & Lifestyle Dashboard")
st.markdown(
"""
This dashboard visualizes and analyzes various health and lifestyle factors
using interactive **Plotly** charts.\n\n
You can navigate between sections to explore insights such as:
- Alcohol consumption patterns
- Smoking habits by gender
- Relationships between mental health and sleep
- Average health conditions by age group\n\n
📊 The data is loaded directly from the project’s GitHub repository.
"""
)
