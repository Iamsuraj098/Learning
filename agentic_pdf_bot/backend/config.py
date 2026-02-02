import os

# API Configuration
FLASK_ENV = os.getenv("FLASK_ENV", "development")
DEBUG = True

# LLM Configuration
LLM_MODEL = "mistral"  # or "llama2", requires Ollama running locally
OLLAMA_BASE_URL = "http://localhost:11434"

# Vector Database
VECTOR_DB_PATH = "./vector_store"
PDF_UPLOAD_FOLDER = "./pdfs"

# API Settings
CORS_ORIGINS = ["http://localhost:3000", "http://localhost:5000", "*"]
MAX_TOKENS = 500
TEMPERATURE = 0.7

# Ensure directories exist
os.makedirs(PDF_UPLOAD_FOLDER, exist_ok=True)
os.makedirs(VECTOR_DB_PATH, exist_ok=True)
