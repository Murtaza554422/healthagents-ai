from backend.rag.pipeline import rag_pipeline
from backend.services.gemini_service import gemini_service


class RAGAgent:

    def process(self, question: str):

        docs = rag_pipeline.search(question)

        if not docs:
            return {
                "agent": "Medical RAG Agent",
                "answer": "Sorry, I couldn't find relevant medical information.",
                "sources": []
            }

        context = "\n\n".join(
            doc.page_content for doc in docs
        )

        sources = []

        for doc in docs:

            filename = doc.metadata.get("filename", "Unknown")
            page = doc.metadata.get("page", "Unknown")

            sources.append(f"{filename} (Page {page})")

        prompt = f"""
You are an expert AI Medical Assistant.

Use ONLY the medical information provided below.

If the answer is not present in the context, reply:
"I couldn't find enough information in the medical knowledge base."

Medical Context:
{context}

Question:
{question}

Instructions:
- Give a clear answer.
- Use simple English.
- Do not invent facts.
- Keep the answer between 100 and 250 words.
"""

        answer = gemini_service.generate(prompt)

        return {
            "agent": "Medical RAG Agent",
            "question": question,
            "answer": answer,
            "sources": list(set(sources))
        }


rag_agent = RAGAgent()