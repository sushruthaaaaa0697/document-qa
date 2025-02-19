from langchain_chroma import Chroma
from src.embeddings.vectorizer import ConvertToVectors
import logging

embedder = ConvertToVectors()


class VectorStore:
    def __init__(self):
        pass

    def get_store(self, chunks):
        vector_store = Chroma.from_documents(
            documents=chunks,  # List of Document objects
            embedding=embedder,  # Custom embedding function
            persist_directory="./chroma_db"  # Directory to persist the database
        )
        logging.info("Vector store created and persisted successfully.")

        return vector_store

    def get_similarity(self, query, client_id):
        vector_store = Chroma(
            persist_directory="./chroma_db",  # Directory where the database is stored
            embedding_function=embedder  # Custom embedding class
        )

        # Perform a similarity search for a user query
        results = vector_store.similarity_search(query, k=5, filter={"client_id": client_id})
        combined_results = [
            f"{res.page_content} [Metadata: {res.metadata}]"
            for res in results
        ]
        return combined_results
