# 🩺 HealthAgents AI

> **AI-Powered Multi-Agent Healthcare Assistant**
>
> HealthAgents AI is an intelligent healthcare platform that combines **Medical RAG**, **Google Gemini AI**, and **Medical Vision Intelligence** to assist users with medical questions, laboratory report analysis, and medical image interpretation.

---

# 🚀 Overview

HealthAgents AI is designed to provide evidence-based healthcare assistance through multiple AI agents. The system leverages Retrieval-Augmented Generation (RAG) with a medical knowledge base and Google's Gemini AI to deliver reliable responses.

The application consists of three major AI modules:

- 💬 Medical Chat Assistant
- 📄 Medical Report Analyzer
- 🖼️ Medical Vision Analyzer

---

# ✨ Features

## 💬 Medical Chat

- Medical Question Answering
- Retrieval-Augmented Generation (RAG)
- Medical Knowledge Base
- Source Citation
- Gemini AI Integration
- Conversation History

---

## 📄 Medical Report Analyzer

Analyze laboratory reports such as:

- CBC Reports
- Blood Tests
- Pathology Reports
- Laboratory Reports

Outputs include:

- Executive Summary
- Severity Level
- Confidence Score
- Abnormal Findings
- Possible Conditions
- Medical Recommendations
- AI Disclaimer

---

## 🖼️ Medical Vision Analyzer

Analyze medical images including:

- Skin Diseases
- X-Ray Images
- MRI Scans
- CT Scans
- Clinical Images

Outputs include:

- AI Findings
- Confidence Score
- Severity Level
- Possible Conditions
- Recommendations
- Disclaimer

---

# 🏗️ System Architecture

```
                    User
                      │
                      ▼
             HealthAgents AI
                      │
         ┌────────────┼────────────┐
         │            │            │
         ▼            ▼            ▼
   Medical Chat   Report AI   Vision AI
         │            │            │
         └────────────┼────────────┘
                      │
                      ▼
                 Gemini 2.5 AI
                      │
                      ▼
              Medical RAG Engine
                      │
                      ▼
           FAISS Vector Database
                      │
                      ▼
              Medical PDF Library
```

---

# 🧠 AI Technologies

- Google Gemini 2.5
- Retrieval-Augmented Generation (RAG)
- LangChain
- FAISS Vector Database
- Medical Prompt Engineering
- Vision AI

---

# 🛠 Technology Stack

### Frontend

- Streamlit
- HTML
- CSS
- Glassmorphism UI

### Backend

- FastAPI
- Python

### AI

- Google Gemini API
- LangChain
- FAISS

### Medical Processing

- PyPDF
- Pillow

---

# 📂 Project Structure

```
HealthAgentsAI/

│
├── backend/
│   ├── api.py
│   ├── rag.py
│   ├── ingest.py
│   ├── prompts.py
│   └── data/
│
├── frontend/
│   ├── app.py
│   ├── components/
│   ├── pages/
│   ├── styles/
│   └── assets/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/HealthAgentsAI.git

cd HealthAgentsAI
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## Add Medical PDFs

Create the folder:

```
backend/data/books/
```

Place your medical PDF files inside.

Run:

```bash
python backend/ingest.py
```

---

## Start Backend

```bash
uvicorn backend.main:app --reload
```

---

## Start Frontend

```bash
streamlit run frontend/app.py
```

---

# 📸 Screenshots

## Home

(Add Screenshot)

---

## Medical Chat

(Add Screenshot)

---

## Report Analyzer

(Add Screenshot)

---

## Vision Analyzer

(Add Screenshot)

---

# 📊 Current Capabilities

✅ AI Medical Chat

✅ Medical Report Analysis

✅ Medical Image Analysis

✅ Medical Knowledge Retrieval

✅ Source Citation

✅ Glassmorphism UI

✅ Responsive Dashboard

✅ Multi-Agent Architecture

---

# 🔮 Future Improvements

- Voice-based Medical Assistant
- OCR for Scanned Reports
- Electronic Health Record (EHR) Integration
- Doctor Appointment Recommendation
- Medicine Interaction Checker
- Multi-language Support
- Patient History Tracking

---

# ⚠ Disclaimer

This application is intended **only for educational and research purposes**.

It does **not** replace professional medical diagnosis, treatment, or advice. Always consult a qualified healthcare professional for medical concerns.

---

# 👨‍💻 Developed By

**Murtaza Khan**

BS Information Technology

Department of Computer and Software Technology (DCST)

University of Swat

---

# 🏆 Hackathon

Developed for the **AMD AI Developer Hackathon 2026**.

---

# 📜 License

This project is licensed under the MIT License.
