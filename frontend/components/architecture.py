import streamlit as st


def architecture():

    st.markdown("## 🏗 AI System Architecture")

    st.markdown("""
<div class="architecture-card">

<h3 align="center">👤 User</h3>

<p align="center">⬇</p>

<h3 align="center">🧠 Router Agent</h3>

<p align="center">⬇</p>

<div style="display:flex;justify-content:space-around;">

<div align="center">
💬<br>
Medical Chat
</div>

<div align="center">
📄<br>
Report Analyzer
</div>

<div align="center">
🖼️<br>
Vision AI
</div>

</div>

<p align="center">⬇</p>

<h3 align="center">🤖 Gemini AI</h3>

<p align="center">⬇</p>

<h3 align="center">📚 FAISS Vector Database</h3>

<p align="center">39 Medical PDFs</p>

</div>
""", unsafe_allow_html=True)