import streamlit as st


def stat_card(icon, title, value, subtitle):

    st.markdown(
        f"""
<div class="stat-card">

<div class="stat-icon">{icon}</div>

<div class="stat-value">{value}</div>

<div class="stat-title">{title}</div>

<div class="stat-subtitle">{subtitle}</div>

</div>
""",
        unsafe_allow_html=True,
    )


def feature_card(icon, title, desc):

    st.markdown(
        f"""
<div class="feature-card">

<div class="feature-icon">{icon}</div>

<h3>{title}</h3>

<p>{desc}</p>

</div>
""",
        unsafe_allow_html=True,
    )


def tech_badge(name):

    st.markdown(
        f"""
<span class="tech-badge">{name}</span>
""",
        unsafe_allow_html=True,
    )