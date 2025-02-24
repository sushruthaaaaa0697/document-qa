from langchain_chroma import Chroma
from src.embeddings.vectorizer import ConvertToVectors
from src.helper.log_config import logging

embedder = ConvertToVectors()


class VectorStore:
    """
    A VectorStore class that manages vector storage and similarity searching for text chunks.

    This class is designed to handle operations related to storing text vectors and performing
    similarity searches on them. It utilizes an external vector database (e.g., Chroma) to persist
    and retrieve vector data efficiently.

    Methods:
        __init__(self): Initializes the VectorStore instance.
        get_store(self, chunks): Asynchronously initializes and populates the vector store with document vectors.
        get_similarity(self, query, client_id): Retrieves similar documents based on a query and client ID.
    """

    def __init__(self):
        """
        Initializes a new instance of the VectorStore class.

        This constructor is currently a placeholder that could be expanded to include initialization
        parameters if needed.
        """
        pass

    async def get_store(self, chunks):
        """
        Asynchronously creates and populates a vector store with document vectors.

        This method initializes a Chroma vector store using document data, custom embedding functions,
        and specifies a directory for persistence. It is designed to handle asynchronous operations
        to manage I/O-bound tasks efficiently.

        Args:
            chunks (list[Document]): A list of Document objects containing the text and metadata for embedding.

        Returns:
            Chroma: An initialized and populated Chroma vector store instance.

        Logs:
            Logs the successful creation and persistence of the vector store.
        """
        vector_store = Chroma.from_documents(
            documents=chunks,  # List of Document objects
            embedding=embedder,  # Custom embedding function
            persist_directory="./chroma_db_test"  # Directory to persist the database
        )
        logging.info("Vector store created and persisted successfully.")

        return vector_store

    def get_similarity(self, query, client_id):
        """
        Retrieves documents similar to a given query, filtered by client ID, from the vector store.

        This method initializes a Chroma instance pointing to an existing database and performs
        a similarity search using the provided query and client ID as a filter. The results are
        formatted to include both the content and metadata of each similar document.

        Args:
            query (str): The query string used to find similar documents.
            client_id (int or str): The client ID used to filter the results, ensuring results are relevant to a specific client.

        Returns:
            list[str]: A list of strings where each string contains the content and metadata of a similar document.

        Example of result:
            ['Document content [Metadata: {client_id: "123", document_type: "report"}]', ...]
        """
        vector_store = Chroma(
            persist_directory="./chroma_db_test",  # Directory where the database is stored
            embedding_function=embedder  # Custom embedding class
        )

        results = vector_store.similarity_search(query, k=5, filter={"client_id": client_id})
        print(results)
        combined_results = [
            f"{res.page_content} [Metadata: {res.metadata}]"
            for res in results
        ]
        return combined_results

