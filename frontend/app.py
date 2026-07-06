import streamlit as st

st.set_page_config(
    page_title="HealthAgents",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 HealthAgents")
st.subheader("Multi-Agent Medical Intelligence Platform")

st.markdown("---")

st.write("Welcome to HealthAgents!")

user_input = st.text_input("Ask a medical question")

if st.button("Send"):
    if user_input:
        st.success(f"You asked: {user_input}")
    else:
        st.warning("Please enter a question.")