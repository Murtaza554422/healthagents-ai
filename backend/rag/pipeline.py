import os

from backend.rag.loader import pdf_loader
from backend.rag.splitter import text_splitter
from backend.rag.embeddings import embeddings
from backend.rag.vector_store import vector_store


class RAGPipeline:

    def __init__(self):
        self.db = None

    def build(self, folder_path: str):

        print("📚 Loading Medical Knowledge Base...")

        documents = pdf_loader.load(folder_path)

        print(f"✅ Loaded {len(documents)} pages")

        print("✂ Splitting documents...")

        chunks = text_splitter.split(documents)

        print(f"✅ Created {len(chunks)} chunks")

        print("🧠 Creating FAISS Index...")

        self.db = vector_store.create(
            chunks,
            embeddings
        )

        print("✅ FAISS Vector Database Created Successfully")

    def load(self):

        if os.path.exists("vector_store/faiss_index"):

            self.db = vector_store.load(embeddings)

            print("✅ FAISS Database Loaded")

    def search(self, query: str, k: int = 4):

        if self.db is None:
            self.load()

        if self.db is None:
            return []

        return self.db.max_marginal_relevance_search(
            query=query,
            k=k,
            fetch_k=20
        )


rag_pipeline = RAGPipeline()