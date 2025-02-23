from fastapi import APIRouter
from pydantic import BaseModel
from src.ops.vector_database.chroma_db import VectorStore
from src.query_service.llm import answer, prompt_builder

query_router = APIRouter()


class UserRequest(BaseModel):
    client_id: str
    query: str


@query_router.post("/user-query/")
async def cleanup_api(request: UserRequest):
    vector_ops = VectorStore()
    results = vector_ops.get_similarity(request.query, str(request.client_id))

    input_to_llm = prompt_builder(str(results), request.query)
    response = await answer(input_to_llm)
    return {"response": response}
