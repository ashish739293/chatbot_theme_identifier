from chromadb import PersistentClient

client = PersistentClient(path="./backend/data/chroma")
collection = client.get_or_create_collection(name="document_chunks")

def store_document_chunks(doc_id: str, chunks: list[dict[str, str]], embeddings: list[list[float]]):
    for i, (chunk, emb) in enumerate(zip(chunks, embeddings)):
        collection.add(
            documents=[chunk["text"]],
            embeddings=[emb],
            metadatas=[{"doc_id": doc_id, "page": chunk["page"], "chunk_index": i}],
            ids=[f"{doc_id}_{i}"]
        )

def search_document_chunks(query_emb: list[float], n_results: int = 5) -> list[dict]:
    res = collection.query(
        query_embeddings=[query_emb],
        n_results=n_results,
        include=["documents", "metadatas", "distances"]
    )
    out = []
    for text, meta, dist in zip(res["documents"][0], res["metadatas"][0], res["distances"][0]):
        out.append({
            "text": text,
            "doc_id": meta["doc_id"],
            "page": meta["page"],
            "chunk_index": meta["chunk_index"],
            "distance": dist
        })
    return out
