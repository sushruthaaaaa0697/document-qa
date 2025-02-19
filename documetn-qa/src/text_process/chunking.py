import logging
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter


class TextChunker:
    def __init__(self, text):
        self.text = text
        logging.info("Text chunker initisliased.")

    def chunker(self, client_id, document_type):
        # split documents into text and embeddings
        text_splitter = RecursiveCharacterTextSplitter(
            # Set a really small chunk size, just to show.
            chunk_size=5000,
            chunk_overlap=1000,
            length_function=len,
            is_separator_regex=False,
        )
        logging.info("TextSplitter initialized.")
        documents = [Document(page_content=self.text, metadata={"client_id": str(client_id), "document_type": document_type})]

        chunks = text_splitter.split_documents(documents)
        return chunks

    def prepare_for_embedding(self, chunks):
        # Extract the page_content from each chunk and combine into a list
        chunk_texts = [chunk.page_content for chunk in chunks]
        logging.info("Chunks successfully prepared for embedding.")
        return chunk_texts
