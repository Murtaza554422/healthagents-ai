import streamlit as st


def hero():
    st.markdown("""
<div class="hero">

<h1>🩺 HealthAgents AI</h1>
<h2>AI-Powered Healthcare Assistant</h2>

<p>
        Ask evidence-based medical questions, analyze laboratory reports,
        interpret medical images, and receive AI-powered healthcare insights
        using Gemini AI, Medical RAG, Vision Intelligence, and Multi-Agent AI.
</p>

</div>
""", unsafe_allow_html=True)

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.page_link(
            "pages/1_💬_Medical_Chat.py",
            label="💬 Medical Chat",
            icon="💬",
            use_container_width=True,
        )

    with col2:
        st.page_link(
            "pages/2_📄_Report_Analyzer.py",
            label="📄 Report Analyzer",
            icon="📄",
            use_container_width=True,
        )

    with col3:
        st.page_link(
            "pages/3_🖼️_Vision_Analyzer.py",
            label="🖼️ Vision AI",
            icon="🖼️",
            use_container_width=True,
        )

    st.write("")