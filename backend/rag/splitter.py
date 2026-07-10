from langchain_text_splitters import RecursiveCharacterTextSplitter


class TextSplitter:

    def split(self, documents):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

        return splitter.split_documents(documents)


text_splitter = TextSplitter()