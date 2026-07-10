import streamlit as st

from components.header import load_css
from components.sidebar import sidebar

st.set_page_config(
    page_title="Medical Vision AI",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()
sidebar()

st.markdown("""
<div class="hero">

<h1>🏥 About HealthAgents AI</h1>

<p>
A Multi-Agent Healthcare Assistant powered by Generative AI.
</p>

</div>
""", unsafe_allow_html=True)

st.header("🎯 Overview")

st.write("""
HealthAgents AI is an intelligent healthcare assistant
designed to help users understand medical reports,
answer health-related questions using trusted
medical literature, and analyze medical images
through AI.
""")

st.divider()

st.header("🏗 System Architecture")

st.code("""

Frontend (Streamlit)

        ↓

FastAPI Backend

        ↓

Router Agent

        ↓

Medical Chat

Medical Reports

Vision AI

        ↓

Gemini 2.5 Flash

        ↓

FAISS Vector Database

""")

st.divider()

st.header("⚙ Technology Stack")

col1,col2,col3=st.columns(3)

with col1:

    st.success("Python")

    st.success("FastAPI")

    st.success("Streamlit")

with col2:

    st.success("LangChain")

    st.success("Gemini")

    st.success("FAISS")

with col3:

    st.success("HuggingFace")

    st.success("PyPDF")

    st.success("Pillow")

st.divider()

st.header("📚 Medical Knowledge Base")

st.write("""
• WHO Guidelines

• CDC Guidelines

• ADA Standards

• Medical Textbooks

• First Aid Manuals

• Nutrition Guides

• Mental Health Resources

• Cardiovascular Disease

• Diabetes

• Hypertension
""")

st.divider()

st.header("🚀 Future Enhancements")

st.checkbox("Voice Assistant")

st.checkbox("OCR Reports")

st.checkbox("Doctor Recommendation")

st.checkbox("Appointment Booking")

st.checkbox("Medicine Reminder")

st.checkbox("Multi-language Support")

st.divider()

st.success("""
🏆 Built for the AI Healthcare Hackathon 2026

HealthAgents AI demonstrates how Retrieval-Augmented
Generation, Vision AI, and Multi-Agent systems can work
together to support healthcare information and education.
""")

