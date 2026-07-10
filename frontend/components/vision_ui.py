import streamlit as st


def image_preview(image):

    st.image(
        image,
        use_container_width=True
    )


def ai_dashboard(result):

    severity = result.get(
        "severity",
        "Unknown"
    )

    colors = {
        "Low": "🟢",
        "Moderate": "🟠",
        "High": "🔴",
        "Critical": "🚨"
    }

    st.metric(
        "Image Type",
        result.get(
            "image_type",
            "Unknown"
        )
    )

    st.metric(
        "Severity",
        f"{colors.get(severity,'⚪')} {severity}"
    )

    confidence = result.get(
        "confidence",
        0
    )

    st.metric(
        "Confidence",
        f"{confidence}%"
    )

    st.progress(confidence / 100)


def findings(text):

    st.subheader("🔬 AI Findings")

    st.info(text)


def conditions(items):

    st.subheader("🩺 Possible Conditions")

    if not items:

        st.info("No possible conditions detected.")

        return

    for item in items:

        st.success(f"✔ {item}")


def recommendations(items):

    st.subheader("💊 Recommendations")

    if not items:

        st.info("No recommendations available.")

        return

    for item in items:

        st.markdown(
            f"- ✅ {item}"
        )