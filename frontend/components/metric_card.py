import streamlit as st

def metric_card(icon, value, title):

    st.markdown(
        f"""
<div class="metric-card-v2">

<div class="metric-icon">{icon}</div>

<div class="metric-value">{value}</div>

<div class="metric-title">{title}</div>

</div>
""",
        unsafe_allow_html=True
    )