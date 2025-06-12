from pydantic import BaseModel

class UploadResponse(BaseModel):
    status: str
    doc_id: str

class QueryResponse(BaseModel):
    theme_summary: str
    citations: list
