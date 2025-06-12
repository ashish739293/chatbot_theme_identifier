from fastapi import APIRouter, File, UploadFile, Form
from app.core.document_processor import process_document
from app.core.query_handler import handle_query
from pydantic import BaseModel

router = APIRouter()

class QueryRequest(BaseModel):
    question: str

@router.post("/upload")
async def api_upload(file: UploadFile = File(...)):
    return await process_document(file)

@router.post("/query")
async def api_query(question: str = Form(...)):
    print("Question received:", question)
    return await handle_query(question)
