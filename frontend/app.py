import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(
    page_title="HealthAgents",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 HealthAgents")
st.subheader("Multi-Agent Medical Intelligence Platform")

user_input = st.text_input("Ask a medical question")

if st.button("Send"):

    if user_input:

        response = requests.post(
            API_URL,
            json={"message": user_input}
        )

        if response.status_code == 200:

            st.success(response.json()["reply"])

        else:

            st.error("Backend Error")