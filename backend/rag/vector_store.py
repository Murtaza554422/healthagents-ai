from langchain_community.vectorstores import FAISS


class VectorStore:

    def create(self, documents, embeddings):
        db = FAISS.from_documents(documents, embeddings)
        db.save_local("vector_store/faiss_index")
        return db

    def load(self, embeddings):
        return FAISS.load_local(
            "vector_store/faiss_index",
            embeddings,
            allow_dangerous_deserialization=True
        )


vector_store = VectorStore()