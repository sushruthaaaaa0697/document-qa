from fastapi import FastAPI
from src.routes.document_ingestion import ingestion_router
from src.routes.user_query import query_router

app = FastAPI()
app.include_router(ingestion_router, prefix="/document")
app.include_router(query_router, prefix="/query")

@app.get("/")
async def root():
    return {"message": "fact finding service"}


@app.get('/health')
async def health_check():
    return {"status": "UP"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
