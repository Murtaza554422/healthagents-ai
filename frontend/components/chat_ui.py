import streamlit as st


def user_message(message):

    st.markdown(f"""
<div class="chat-user">

<h4>👤 You</h4>

<p>{message}</p>

</div>
""", unsafe_allow_html=True)


def ai_message(message):

    st.markdown(f"""
<div class="chat-ai">

<h4>🤖 HealthAgents AI</h4>

<p>{message}</p>

</div>
""", unsafe_allow_html=True)


def sources(source_list):

    st.markdown("## 📚 Medical Sources")

    for source in source_list:

        with st.expander(f"📄 {source}"):

            st.success(source)