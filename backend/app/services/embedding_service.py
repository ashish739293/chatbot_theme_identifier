from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_text(text_chunks):
    return model.encode(text_chunks).tolist()

def embed_query(query):
    return model.encode([query])[0].tolist()
