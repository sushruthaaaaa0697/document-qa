import os
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from src.text_process.chunking import TextChunker
from src.ops.vector_database.chroma_db import VectorStore
from src.document_processor.reader_factory import AdapterFactory
from fastapi import File, UploadFile, HTTPException, APIRouter, Form


ingestion_router = APIRouter()


class DocumentUploadRequest(BaseModel):
    client_id: str
    document_type: str
    file: UploadFile


@ingestion_router.post("/upload-document/")
async def upload_document(client_id: str = Form(...), document_type: str = Form(...), file: UploadFile = File(...)):
    try:
        # Save uploaded file temporarily
        temp_file_path = f"temp/{file.filename}"
        with open(temp_file_path, "wb") as buffer:
            buffer.write(await file.read())

        # Process the file
        reader = AdapterFactory.get_adapter(document_type)(temp_file_path)
        print(reader)
        text = reader.read()

        chunks = TextChunker(text)
        split = chunks.chunker(client_id, "DriversLicense")

        vector_ops = VectorStore()
        vector_store = vector_ops.get_store(split)

        # Clean up: remove the temporary file if needed
        os.remove(temp_file_path)

        return JSONResponse(status_code=200, content={"message": "Document processed successfully"})
    except Exception as e:
        # In case of any error during file handling or processing
        raise HTTPException(status_code=500, detail=str(e))

