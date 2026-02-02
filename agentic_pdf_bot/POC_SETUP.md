# PDF Agent Chatbot - POC Setup Guide

## 🎯 Quick Start (POC)

### Prerequisites
- Python 3.8+
- Ollama (https://ollama.ai)

### Setup

```bash
# 1. Download and start Ollama model
ollama pull mistral
ollama serve

# 2. In new terminal - Install dependencies
cd agentic_pdf_bot/backend
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# 3. Install packages
pip install -r requirements.txt

# 4. Add your PDF file(s)
# Copy your PDFs to ../pdfs/ folder
# Example: ../pdfs/document.pdf

# 5. Start backend
python app.py
```

### Access

Open browser: **http://localhost:5000**

## 📋 How It Works

1. **Upload PDFs**: Copy PDF files to `pdfs/` folder
2. **Load Knowledge Base**: Click "Load PDFs" button - indexes document chunks
3. **Ask Questions**: Type question in chat box
4. **Agent Responds**: AI searches document context and provides intelligent answer

## 🤖 Agent Behavior

The system uses **Retrieval-Augmented Generation (RAG)**:
- Searches most relevant parts of PDF
- Generates context-aware responses
- Handles 45+ page documents efficiently
- Provides accurate, document-grounded answers

## 🔧 Configuration

Edit `backend/config.py`:

```python
LLM_MODEL = "mistral"       # Model name
TEMPERATURE = 0.7          # 0-1: Lower = factual, Higher = creative
MAX_TOKENS = 500           # Response length
```

## 📊 API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | Web UI |
| `/api/chat` | POST | Send message |
| `/api/load-pdfs` | POST | Load PDFs |
| `/api/status` | GET | System status |

## ✅ Requirements Met

✓ Backend-only implementation  
✓ Simple Flask UI (no heavy frontend)  
✓ Agent-type intelligent responses  
✓ Handles large PDFs (45+ pages)  
✓ RAG for accurate document-based answers  
✓ POC ready  

## 🆘 Troubleshooting

**Ollama not running:**
```bash
ollama serve
```

**Model not found:**
```bash
ollama pull mistral
```

**Port in use:**
Edit `backend/app.py`, change `port=5000` to `port=5001`

**No response:**
- Check Ollama is running
- Check PDFs are loaded
- Check system status indicators

## 📁 Project Structure

```
agentic_pdf_bot/
├── backend/
│   ├── app.py              ← Flask API + UI
│   ├── config.py           ← Settings
│   ├── pdf_loader.py       ← PDF indexing
│   ├── llm_service.py      ← LLM agent logic
│   └── requirements.txt    ← Dependencies
├── pdfs/                   ← Your PDFs
└── README.md              ← Full documentation
```

## 🎯 Next Steps

1. Add your 45-page PDF to `pdfs/` folder
2. Run setup above
3. Visit http://localhost:5000
4. Click "Load PDFs"
5. Start asking questions

---

**Ready for Client POC! 🚀**
