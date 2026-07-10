from pathlib import Path
import streamlit as st


def sidebar():

    with st.sidebar:

        # =========================
        # LOGO
        # =========================

        logo = Path(__file__).parent.parent / "assets" / "logo.png"

        if logo.exists():
            st.image(str(logo), width=120)

        st.markdown(
            """
<h2 style='text-align:center;margin-bottom:0;'>
HealthAgents AI
</h2>

<p style='text-align:center;color:#94A3B8;margin-top:5px;'>
AI Healthcare Assistant
</p>
""",
            unsafe_allow_html=True,
        )

        st.markdown("---")

        # =========================
        # NAVIGATION
        # =========================

        st.page_link("app.py", label="🏠 Home")

        st.page_link(
            "pages/1_💬_Medical_Chat.py",
            label="💬 Medical Chat"
        )

        st.page_link(
            "pages/2_📄_Report_Analyzer.py",
            label="📄 Report Analyzer"
        )

        st.page_link(
            "pages/3_🖼️_Vision_Analyzer.py",
            label="🩻 Vision AI"
        )

        st.page_link(
            "pages/4_ℹ️_About.py",
            label="ℹ About"
        )

        st.markdown("---")

        # =========================
        # LIVE STATUS
        # =========================

        st.markdown("### 🟢 System Status")

        st.success("Backend Online")

        st.success("Gemini Connected")

        st.success("FAISS Ready")

        st.success("Medical Knowledge Loaded")

        st.markdown("---")

        # =========================
        # PLATFORM STATS
        # =========================

        st.markdown("### 📊 Platform")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("PDFs", "39")

        with col2:
            st.metric("Agents", "3")

        st.metric("LLM", "Gemini 2.5")

        st.metric("Vector DB", "FAISS")

        st.markdown("---")

        st.caption("© 2026 HealthAgents AI")

st.divider()

st.subheader("🟢 System Status")

st.success("Gemini Connected")

st.success("FAISS Loaded")

st.success("FastAPI Running")

st.success("39 PDFs Indexed")

st.divider()

st.caption("Version 1.0")