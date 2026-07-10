from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


class PDFLoader:

    def load(self, folder_path: str):

        documents = []

        folder = Path(folder_path)

        pdf_files = list(folder.rglob("*.pdf"))

        print(f"📚 Found {len(pdf_files)} PDF(s)")

        for pdf_file in pdf_files:

            print(f"Loading: {pdf_file.name}")

            loader = PyPDFLoader(str(pdf_file))

            docs = loader.load()

            category = pdf_file.parent.name

            for doc in docs:
                doc.metadata["source"] = str(pdf_file)
                doc.metadata["filename"] = pdf_file.name
                doc.metadata["category"] = category

            documents.extend(docs)

        return documents


pdf_loader = PDFLoader()