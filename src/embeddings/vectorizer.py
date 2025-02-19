from typing import List
from sentence_transformers import SentenceTransformer
import logging

# class ConvertToVectors:
#     def __init__(self):
#         self.model_name = "BAAI/bge-small-en"
#         self.model_kwargs = {"device": "cpu"}
#         self.encode_kwargs = {"normalize_embeddings": True}
#
#     def vectorize(self, texts):
#         hf = HuggingFaceBgeEmbeddings(
#             model_name=self.model_name, model_kwargs=self.model_kwargs, encode_kwargs=self.encode_kwargs
#         )
#
#         vectors = hf.embed_documents(texts)
#         return vectors
#
#     def vectorize_query(self, query):
#         return self.vectorize([query])[0]


class ConvertToVectors:
    def __init__(self):
        self.model_name = "BAAI/bge-small-en"
        self.model_kwargs = {"device": "cpu"}
        self.encode_kwargs = {"normalize_embeddings": True}
        self.model = SentenceTransformer(self.model_name, device=self.model_kwargs["device"])

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for a list of texts.
        This method is required by Chroma DB.
        """
        embeddings = self.model.encode(texts, normalize_embeddings=self.encode_kwargs["normalize_embeddings"])
        logging.info("Embeddings generated successfully.")
        return embeddings.tolist()  # Convert numpy array to list of lists

    def embed_query(self, text: str) -> List[float]:
        """
        Generate an embedding for a single query.
        This method is required by Chroma DB.
        """
        return self.embed_documents([text])[0]

    # Optional: Keep your original methods for backward compatibility
    def vectorize(self, texts: List[str]) -> List[List[float]]:
        """Alias for embed_documents."""
        return self.embed_documents(texts)

    def vectorize_query(self, query: str) -> List[float]:
        """Alias for embed_query."""
        return self.embed_query(query)

