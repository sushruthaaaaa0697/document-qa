from src.text_process.chunking import TextChunker
from src.embeddings.vectorizer import ConvertToVectors
from src.document_processor.reader_factory import AdapterFactory
from src.ops.vector_database.chroma_db import VectorStore
from src.query_service.llm import answer, prompt_builder
import uuid

myuuid = uuid.uuid4()

reader = AdapterFactory.get_adapter("document")(r"C:\Users\SushrutaBhat\Downloads\s41598-024-83664-1.pdf")

text = reader.read()

chunks = TextChunker(text)
split = chunks.chunker(myuuid, "DriversLicense")

vector_ops = VectorStore()
vector_store = vector_ops.get_store(split)
query = "What are some opportunities for recovery of cost? "
# myuuid = "85953836-c1cf-40ae-b903-97940abd95bf"
# print(myuuid)
results = vector_ops.get_similarity(query, str(myuuid))
print(results)

input_to_llm = prompt_builder(str(results), query)
response = answer(input_to_llm)
print(response)
