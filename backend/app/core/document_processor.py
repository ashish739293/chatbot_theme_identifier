import os, uuid
from fastapi import UploadFile
from app.services.pdf_service import extract_text_from_pdf
from app.services.ocr_service import extract_text_with_ocr
from app.services.embedding_service import embed_text
from app.services.vector_db_service import store_document_chunks
from app.config import settings

async def process_document(file: UploadFile):
    doc_id = str(uuid.uuid4())
    path = os.path.join(settings.DATA_DIR, f"{doc_id}_{file.filename}")
    os.makedirs(settings.DATA_DIR, exist_ok=True)
    with open(path, "wb") as f:
        f.write(await file.read())

    if path.lower().endswith(".pdf"):
        chunks = extract_text_from_pdf(path)
    else:
        chunks = [{"page": 1, "text": t} for t in extract_text_with_ocr(path)]

    texts = [c["text"] for c in chunks]
    embeddings = embed_text(texts)
    store_document_chunks(doc_id, chunks, embeddings)

    return {"status": "uploaded", "doc_id": doc_id, "chunks": len(chunks)}
