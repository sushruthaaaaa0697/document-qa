import logging
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter


class TextChunker:
    """
    A TextChunker class for dividing large text bodies into smaller chunks suitable for processing,
    especially for tasks like text embeddings or machine learning analysis.

    This class provides functionality to split a single large text document into manageable chunks and
    prepare these chunks for further text processing or embeddings generation.

    Attributes:
        text (str): The full text content that needs to be chunked.

    Methods:
        __init__(self, text): Initializes the TextChunker instance with the text to be chunked.
        chunker(self, client_id, document_type): Splits the text into smaller chunks based on specified parameters.
        prepare_for_embedding(self, chunks): Prepares the text chunks for embedding or further text processing.
    """

    def __init__(self, text):
        """
        Initializes a new instance of the TextChunker class with specified text.

        This constructor logs an informational message indicating that the TextChunker has been
        initialized, which is helpful for debugging and tracking the initialization state.

        Args:
            text (str): The full text content to be chunked.
        """
        self.text = text
        logging.info("Text chunker initialised.")

    def chunker(self, client_id, document_type):
        """
        Splits the provided text into smaller chunks using a recursive character-based text splitter.

        This method configures and uses a RecursiveCharacterTextSplitter to divide the text based on a specified
        chunk size and overlap. It attaches metadata such as client ID and document type to each chunk, which can
        be useful for downstream processing or tracking.

        Args:
            client_id (int or str): A unique identifier for the client, used for metadata tagging.
            document_type (str): The type of document or text being processed, also used for metadata.

        Returns:
            list[Document]: A list of Document objects, where each Document contains a chunk of text along with its metadata.

        Logs:
            Logs the initialization of the text splitter and the successful preparation of text chunks.
        """
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=5000,
            chunk_overlap=1000,
            length_function=len,
            is_separator_regex=False,
        )
        logging.info("TextSplitter initialized.")
        documents = [
            Document(page_content=self.text, metadata={"client_id": str(client_id), "document_type": document_type})]

        chunks = text_splitter.split_documents(documents)
        return chunks

    def prepare_for_embedding(self, chunks):
        """
        Prepares text chunks for embedding or further processing by extracting the text content from each chunk.

        This method simplifies the retrieval of text from each chunk for subsequent operations such as embedding
        or machine learning tasks.

        Args:
            chunks (list[Document]): A list of Document objects containing the text chunks.

        Returns:
            list[str]: A list containing the text of each chunk prepared for further processing.

        Logs:
            Logs the successful preparation of chunks for embedding.
        """
        chunk_texts = [chunk.page_content for chunk in chunks]
        logging.info("Chunks successfully prepared for embedding.")
        return chunk_texts

