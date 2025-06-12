import fitz  # PyMuPDF

def extract_text_from_pdf(path: str) -> list[str]:
    doc = fitz.open(path)
    chunks = []
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text("text") or ""
        for para in text.split("\n\n"):
            para_clean = para.strip()
            if para_clean:
                chunks.append({"page": page_num, "text": para_clean})
    return chunks
