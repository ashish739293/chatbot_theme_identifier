from huggingface_hub import InferenceClient
from app.config import settings

client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.3",
    token=settings.HF_API_TOKEN
)

def get_summarized_theme(citations: list[dict], question: str) -> str:
    texts = [f"(Doc {c['doc_id']} p{c['page']}) {c['text']}" for c in citations]
    context = "\n\n".join(texts)[:7000]

    prompt = f"Context:\n{context}\n\nQuestion: {question}\n\nSummarize main themes with citations."

    return client.text_generation(prompt, max_new_tokens=200)
