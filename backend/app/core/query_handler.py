from app.services.embedding_service import embed_query
from app.services.vector_db_service import search_document_chunks
from app.services.llm_service import get_summarized_theme

async def handle_query(question: str):
    q_emb = embed_query(question)
    chunks = search_document_chunks(q_emb, n_results=10)

    citations = [
        {
            "text": c["text"],
            "doc_id": c["doc_id"],
            "page": c["page"],
            "chunk_index": c["chunk_index"],
            "distance": c["distance"]
        }
        for c in chunks
    ]

    theme = get_summarized_theme(citations, question)
    return {"theme_summary": theme, "citations": citations}
