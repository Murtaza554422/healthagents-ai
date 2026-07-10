import streamlit as st

from api import report

from components.header import load_css
from components.sidebar import sidebar

from components.report_ui import (
    summary,
    severity,
    findings,
    conditions,
    recommendations
)

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Medical Report Analyzer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()
sidebar()

# ==========================================================
# SESSION STATE
# ==========================================================

if "report_result" not in st.session_state:
    st.session_state.report_result = None

# ==========================================================
# HERO
# ==========================================================

st.markdown("""
<div class="hero">

<h1>📄 Medical Report Analyzer</h1>

<p>
Upload laboratory reports, CBC reports, blood test reports,
or other medical PDF documents and receive an AI-powered
clinical analysis within seconds.
</p>

</div>
""", unsafe_allow_html=True)

# ==========================================================
# FILE UPLOAD
# ==========================================================

uploaded_file = st.file_uploader(
    "📂 Drag & Drop your Medical Report",
    type=["pdf"],
    help="Supported format: PDF"
)

# ==========================================================
# ANALYZE BUTTON
# ==========================================================

if uploaded_file is not None:

    st.success(f"✅ Uploaded: {uploaded_file.name}")

    if st.button(
        "🧠 Analyze Medical Report",
        use_container_width=True
    ):

        with st.spinner("🩺 AI is analyzing your medical report..."):

            try:

                st.session_state.report_result = report(uploaded_file)

            except Exception as e:

                st.error(f"Error: {e}")

# ==========================================================
# DISPLAY RESULT
# ==========================================================

if st.session_state.report_result is not None:

    result = st.session_state.report_result

    st.success("✅ Analysis Completed Successfully")

    # ==================================================
    # CONFIDENCE
    # ==================================================

    confidence = result.get("confidence", 0)

    if confidence > 0:
        st.progress(confidence / 100)

    st.divider()

    # ==================================================
    # DASHBOARD
    # ==================================================

    left, right = st.columns([3, 1])

    with left:

        summary(
            result.get(
                "summary",
                "No summary available."
            )
        )

    with right:

        severity(
            result.get(
                "severity",
                "Unknown"
            )
        )

        st.metric(
            "Confidence",
            f"{confidence}%"
        )

        st.metric(
            "Emergency",
            result.get(
                "emergency",
                "Unknown"
            )
        )

    st.divider()

    # ==================================================
    # FINDINGS
    # ==================================================

    findings(
        result.get(
            "abnormal_findings",
            []
        )
    )

    st.divider()

    # ==================================================
    # CONDITIONS
    # ==================================================

    conditions(
        result.get(
            "possible_conditions",
            []
        )
    )

    st.divider()

    # ==================================================
    # RECOMMENDATIONS
    # ==================================================

    recommendations(
        result.get(
            "recommendations",
            []
        )
    )

    st.divider()

    # ==================================================
    # DISCLAIMER
    # ==================================================

    st.markdown("## ⚠ Medical Disclaimer")

    st.info(
        result.get(
            "disclaimer",
            "This analysis is for informational purposes only."
        )
    )

    st.divider()

    # ==================================================
    # AI SUMMARY
    # ==================================================

    st.markdown("## 📊 Analysis Summary")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "AI Engine",
            "Gemini 2.5"
        )

    with c2:
        st.metric(
            "Knowledge Base",
            "Medical RAG"
        )

    with c3:
        st.metric(
            "Report Status",
            "Analyzed"
        )

# ==========================================================
# CLEAR RESULT
# ==========================================================

st.sidebar.divider()

if st.sidebar.button(
    "🗑 Clear Analysis",
    use_container_width=True
):

    st.session_state.report_result = None

    st.rerun()