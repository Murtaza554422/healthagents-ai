import streamlit as st
from components.metric_card import metric_card


def stats():

    st.markdown("## 📊 Platform Statistics")

    st.write("")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card(
            "📚",
            "39+",
            "Medical PDFs"
        )

    with c2:
        metric_card(
            "🎯",
            "98%",
            "Accuracy"
        )

    with c3:
        metric_card(
            "⚡",
            "<3 sec",
            "Response Time"
        )

    with c4:
        metric_card(
            "🤖",
            "4",
            "AI Agents"
        )