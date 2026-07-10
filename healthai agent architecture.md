                                     👤 USER
                           (Doctor / Patient / Student)
                                            │
                                            │
                                            ▼
 ┌────────────────────────────────────────────────────────────────────┐
 │                    HealthAgents AI Web Application                 │
 │                 Streamlit • Responsive Glassmorphism UI            │
 └────────────────────────────────────────────────────────────────────┘
                                            │
                                            ▼
                         ┌────────────────────────────┐
                         │     Request Router         │
                         │        FastAPI            │
                         └────────────┬──────────────┘
                                      │
             ┌────────────────────────┼────────────────────────┐
             │                        │                        │
             ▼                        ▼                        ▼
 ┌─────────────────────┐   ┌──────────────────────┐  ┌─────────────────────┐
 │ 💬 Medical Chat     │   │ 📄 Report Analyzer   │  │ 🖼 Vision Analyzer  │
 │ LangChain + RAG     │   │ PDF Understanding    │  │ Image Understanding │
 └──────────┬──────────┘   └──────────┬───────────┘  └──────────┬──────────┘
            │                         │                         │
            └──────────────┬──────────┴──────────────┬──────────┘
                           ▼                         ▼
                 ┌────────────────────────────────────────┐
                 │          Google Gemini 2.5 AI          │
                 │      Reasoning • Summarization         │
                 │ Medical QA • Clinical Interpretation   │
                 └────────────────┬───────────────────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
                    ▼                           ▼
         ┌──────────────────────┐    ┌──────────────────────┐
         │ Medical RAG Engine   │    │ Vision Intelligence  │
         │ LangChain Retrieval  │    │ Image Reasoning      │
         └──────────┬───────────┘    └──────────────────────┘
                    │
                    ▼
         ┌────────────────────────────┐
         │     FAISS Vector Store      │
         │ Semantic Embedding Search   │
         └──────────────┬──────────────┘
                        │
                        ▼
         ┌────────────────────────────┐
         │   Medical Knowledge Base    │
         │ 39+ Medical PDF Books       │
         │ Clinical Guidelines         │
         │ Medical Documentation       │
         └────────────────────────────┘