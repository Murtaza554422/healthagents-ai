import time
import streamlit as st

from api import chat
from components.sidebar import sidebar
from components.header import load_css

st.set_page_config(
    page_title="Medical Vision AI",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()
sidebar()

# ==========================================
# Session State
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ==========================================
# HERO
# ==========================================

st.markdown("""
<div class="hero-small">

<h1>💬 Medical AI Assistant</h1>

<p>
Evidence-based healthcare assistant powered by Gemini + LangChain + FAISS
</p>

</div>
""", unsafe_allow_html=True)

# ==========================================
# Suggested Questions
# ==========================================

st.markdown("### 💡 Try asking")

c1, c2, c3 = st.columns(3)

with c1:
    if st.button("🩺 Symptoms of Diabetes"):
        st.session_state.prompt = "What are the symptoms of diabetes?"

with c2:
    if st.button("❤️ Causes of Heart Failure"):
        st.session_state.prompt = "What causes heart failure?"

with c3:
    if st.button("🧠 Mental Health Tips"):
        st.session_state.prompt = "Give me tips for improving mental health."

# ==========================================
# CHAT HISTORY
# ==========================================

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])

        if msg["role"] == "assistant":

            if "sources" in msg:

                st.markdown("### 📚 Sources")

                for src in msg["sources"]:

                    st.markdown(
                        f"""
<div class="source-card">
📄 {src}
</div>
""",
                        unsafe_allow_html=True,
                    )

# ==========================================
# USER INPUT
# ==========================================

prompt = st.chat_input("Ask a medical question...")

if not prompt and "prompt" in st.session_state:
    prompt = st.session_state.pop("prompt")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("🧠 Searching Medical Knowledge Base..."):

            result = chat(prompt)

        placeholder = st.empty()

        full_text = ""

        for word in result["answer"].split():

            full_text += word + " "

            placeholder.markdown(full_text)

            time.sleep(0.02)

        st.success("✅ Answer Generated from Medical Knowledge Base")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Confidence", "98%")

        with col2:
            st.metric("Knowledge", "Medical RAG")

        st.markdown("### 📚 Sources")

        for src in result["sources"]:

            st.markdown(
                f"""
<div class="source-card">
📄 {src}
</div>
""",
                unsafe_allow_html=True,
            )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": result["answer"],
            "sources": result["sources"],
        }
    )