import os

class Settings:
    DATA_DIR = os.getenv("DATA_DIR", "backend/data")
    CHROMA_DIR = os.path.join(DATA_DIR, "chroma")
    HF_API_TOKEN = os.getenv("HF_API_TOKEN")

settings = Settings()