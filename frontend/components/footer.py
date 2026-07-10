import streamlit as st


def footer():

    st.divider()

    st.markdown(
        """
<center>

### 🩺 HealthAgents AI

AI-Powered Healthcare Assistant

Built with ❤️ using Streamlit • FastAPI • Gemini • LangChain

Hackathon 2026

</center>
""",
        unsafe_allow_html=True,
    )