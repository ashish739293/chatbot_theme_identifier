# 📚 Document Theme Identifier Chatbot

An AI-powered chatbot that allows users to upload documents (PDFs/images), ask questions, and get **theme-based summaries** with **sentence-level citations**.

✨ **Features Implemented:**

- 🧠 LLM-powered theme summary (Mistral-7B via HuggingFace)
- 🔍 Sentence-level citations (not just page-level)
- 📄 PDF/image document upload
- 🌐 Modern UI with loading indicators, clean layout

---

## 🧩 Tech Stack

| Layer      | Tech Used                        |
|------------|----------------------------------|
| Frontend   | React.js                         |
| Backend    | FastAPI                          |
| Vector DB  | ChromaDB                         |
| Embedding  | SentenceTransformers (`MiniLM`)  |
| OCR Engine | PyMuPDF + Tesseract              |
| LLM Model  | HuggingFace Inference API        |

---

## 📁 Project Structure

```
document-theme-chatbot/
├── backend/
│   ├── app/
│   │   ├── routers/       # API endpoints
│   │   ├── services/      # OCR, vector search, LLM logic
│   │   ├── config.py      # Env setup and constants
│   │   └── main.py        # App entry
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js         # Main UI component
│   │   ├── App.css        # Styling
│   │   └── index.js       # Entry point
│   └── package.json
└── README.md              # You're here!
```

---

## 🚀 How to Run

### 1. Clone the Project

```bash
git clone https://github.com/ashish739293/chatbot_theme_identifier.git
cd chatbot_theme_identifier
```

---

### 2. Setup: Backend (FastAPI)

#### ✅ Prerequisites

- Python 3.9+
- [Tesseract OCR installed](https://github.com/tesseract-ocr/tesseract)

#### 📦 Install dependencies

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### 🗝️ Add `.env` file

Create `backend/.env`:

```env
HF_API_TOKEN=your_huggingface_api_key
```

#### ▶️ Start the FastAPI server

```bash
uvicorn app.main:app --reload
```

---

### 3. Setup: Frontend (React)

#### 📦 Install dependencies

```bash
cd frontend
npm install
```

#### ▶️ Start React app

```bash
npm start
```

App runs at: [http://localhost:3000](http://localhost:3000)

---

## 💡 How It Works

1. **Upload Document**  
   PDF or image files are uploaded → text extracted via PyMuPDF or Tesseract OCR.

2. **Text Chunks & Embeddings**  
   Each paragraph/sentence is split into chunks → embedded using `MiniLM`.

3. **Store in Chroma VectorDB**  
   Embeddings + metadata (doc_id, page, sent_idx) are stored in Chroma.

4. **Ask Questions**  
   Questions are embedded → semantic similarity search finds relevant chunks.

5. **LLM Summary**  
   Top N citations are passed into an LLM prompt → generates theme-level summary with references.

6. **UI**  
   React shows:
   - Summary
   - Sentence-level citations
---

## 🧠 Backend Code Overview 

### `main.py`

```python
from fastapi import FastAPI
from app.api.routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Document Theme Chatbot")


# Allow CORS for your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")

```

### Services

- `ocr_service.py` – extracts text from PDF/image (including scanned)
- `embeddings_service.py` – generates dense vectors using MiniLM
- `vector_db_service.py` – ChromaDB logic for insert/search
- `llm_service.py` – summarizes with HuggingFace LLM
- `pdf_service.py` – file storage, chunking, metadata

---

## 🖼️ Frontend UI Overview

### `App.js`

- Upload panel
- Ask question input
- Filters (filetype, include/exclude)
- Summary output
- Citation table with clickable modal

### `App.css`

Styled with attractive, clean layout:
- `box` – each panel
- `modal` – citation popups
- `loading` – button state and indicator

---

## 📦 Backend Dependencies

### `requirements.txt`

```
fastapi
uvicorn
python-dotenv
sentence-transformers
chromadb
pytesseract
pillow
PyMuPDF
requests
```

---

## 🌐 Deployment Notes

- You can Dockerize both frontend and backend separately.
- HuggingFace API requires a free token (for Mistral model).
- For production, use Postgres or Qdrant for vectors instead of local Chroma.

---

## 🏁 Future Enhancements

✅ Implemented:
- ✅ Sentence-level citations
- ✅ Loading state UI

Coming Soon:
- 🧾 PDF rendering with `react-pdf`
- 🧭 Map view of document sections
- 📚 Clustered theme extraction

---

## 🤝 Contributions & License

MIT License.  
Feel free to fork and contribute. Credit appreciated.
