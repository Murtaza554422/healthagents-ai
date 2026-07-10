import streamlit as st


def tech_stack():

    st.markdown("## ⚙ Technology Stack")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.success("🧠 Gemini 2.5")

        st.success("🔍 LangChain")

        st.success("📚 FAISS")

    with c2:

        st.success("⚡ FastAPI")

        st.success("🎨 Streamlit")

        st.success("🐍 Python")

    with c3:

        st.success("📄 PyPDF")

        st.success("🖼 Pillow")

        st.success("🤖 Multi-Agent AI")