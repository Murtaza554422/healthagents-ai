import streamlit as st


def summary(text):

    st.markdown(f"""
<div class='summary-card'>

<h3>📋 Summary</h3>

<p>{text}</p>

</div>
""", unsafe_allow_html=True)


def severity(level):

    colors = {
        "Low":"🟢",
        "Moderate":"🟠",
        "High":"🔴",
        "Critical":"🚨"
    }

    icon = colors.get(level,"⚪")

    st.metric(
        "Severity",
        f"{icon} {level}"
    )


def findings(items):

    st.subheader("🩸 Abnormal Findings")

    for item in items:

        st.markdown(f"""
<div class='finding-card'>

❌ {item}

</div>
""", unsafe_allow_html=True)


def conditions(items):

    st.subheader("🩺 Possible Conditions")

    for item in items:

        st.markdown(f"""
<div class='condition-card'>

{item}

</div>
""", unsafe_allow_html=True)


def recommendations(items):

    st.subheader("✅ Recommendations")

    for item in items:

        st.markdown(f"""
<div class='recommend-card'>

☑ {item}

</div>
""", unsafe_allow_html=True)