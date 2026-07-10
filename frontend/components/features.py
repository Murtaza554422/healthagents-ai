import streamlit as st


def features():

    st.markdown("## 🚀 Core Features")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown("""
<div class="feature-card">

<h2>💬</h2>

<h3>Medical Chat</h3>

<p>

Evidence-based medical assistant using
Retrieval-Augmented Generation.

</p>

</div>
""", unsafe_allow_html=True)

    with c2:

        st.markdown("""
<div class="feature-card">

<h2>📄</h2>

<h3>Report Analyzer</h3>

<p>

Automatically analyze
CBC, Blood Tests,
Lab Reports.

</p>

</div>
""", unsafe_allow_html=True)

    with c3:

        st.markdown("""
<div class="feature-card">

<h2>🖼️</h2>

<h3>Vision AI</h3>

<p>

Analyze skin diseases,
X-rays,
MRI and CT scans.

</p>

</div>
""", unsafe_allow_html=True)