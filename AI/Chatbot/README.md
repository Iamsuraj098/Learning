# 🤖 AI Knowledge Base Chatbot

A fully functional chatbot that answers questions based on PDF documents using AI, with Speech-to-Text (STT) and Text-to-Speech (TTS) capabilities.

## Features ✨

✅ **PDF Knowledge Base**: Automatic text extraction and chunking from PDF files
✅ **Semantic Search**: Uses embeddings to find relevant context (FAISS + Sentence Transformers)
✅ **AI Response Generation**: Natural language processing with human-like responses
✅ **Speech-to-Text (STT)**: Voice input using Web Speech API
✅ **Text-to-Speech (TTS)**: Audio response playback
✅ **Beautiful UI**: Modern, responsive web interface
✅ **100% Free**: No API costs, runs locally

## Architecture 🏗️

```
User Input (Text/Voice)
        ↓
    Backend Server (Flask)
        ↓
    ├─ STT Processing
    ├─ Query Embedding
    ├─ Vector Search (FAISS)
    ├─ Context Retrieval
    ├─ LLM Response Generation
    └─ TTS Output
        ↓
    User Output (Text/Audio)
```

## Installation 📦

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Step 1: Install Python Dependencies

```bash
cd "path\to\Chatbot"
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- Sentence Transformers (embeddings)
- FAISS (vector search)
- PyPDF2 & pdfplumber (PDF processing)
- pyttsx3 (text-to-speech)
- Transformers (LLM)

**Note**: First installation may take 10-15 minutes as it downloads AI models (~2GB).

### Step 2: Add PDF Files

1. Create a `pdfs` folder in the chatbot directory (already created)
2. Add your PDF files to this folder:
   ```
   Chatbot/
   ├── pdfs/
   │   ├── document1.pdf
   │   ├── document2.pdf
   │   └── ...
   ```

### Step 3: Run the Chatbot

```bash
python app.py
```

You'll see output like:
```
🚀 Initializing Chatbot Components...
📚 Loading Embedding Model...
🤖 Loading Language Model...
🔊 Initializing Text-to-Speech...
📂 Initializing Knowledge Base from 'pdfs' folder...
📄 Found 2 PDF files
📖 Processing: document1.pdf...
📖 Processing: document2.pdf...
✅ Total chunks created: 250
✅ Knowledge base initialized successfully!

🌐 Starting Flask server...
📍 Open your browser at: http://localhost:5000
```

### Step 4: Open the Web Interface

Open your browser and go to: **http://localhost:5000**

## Usage 🎯

### Text Input
1. Type your question in the input field
2. Click "Send" or press Enter
3. Wait for the AI response

### Voice Input (STT)
1. Click the 🎤 microphone button
2. Speak your question clearly
3. Release when done - text will appear automatically
4. The chatbot will respond

### Voice Output (TTS)
1. After receiving a response, click 🔊 speaker button
2. The response will be read aloud
3. Responses are also auto-played by default

## File Structure 📁

```
Chatbot/
├── app.py                  # Main Flask backend
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html         # Web interface
├── pdfs/                  # Your PDF files (add here!)
│   └── (add your PDFs)
└── README.md              # This file
```

## How It Works 🔧

### 1. PDF Processing
- Extracts text from all PDFs in the `pdfs` folder
- Splits text into overlapping chunks (500 characters, 100 char overlap)
- Creates semantic embeddings using Sentence Transformers

### 2. Query Processing
- Encodes user question into embeddings
- Searches FAISS vector store for similar chunks
- Retrieves top-3 relevant context pieces

### 3. Response Generation
- Sends query + context to LLM
- Generates natural, contextual response
- Ensures human-like tone and conversational style

### 4. Output
- Returns text response to UI
- Auto-plays audio using TTS
- Displays in chat interface

## Technology Stack 🛠️

| Component | Technology | Why |
|-----------|-----------|-----|
| Backend | Flask | Lightweight, easy to use |
| Embeddings | Sentence Transformers | Fast, accurate semantic search |
| Vector DB | FAISS | High-performance similarity search |
| LLM | Hugging Face (distilgpt2) | Free, runs locally |
| PDF Processing | PyPDF2 + pdfplumber | Reliable text extraction |
| TTS | pyttsx3 | Offline, free text-to-speech |
| STT | Web Speech API | Browser native, free |
| Frontend | HTML/CSS/JavaScript | No dependencies, responsive |

## Customization 🎨

### Change AI Model
Edit `app.py` line where LLM is loaded:
```python
# Use a larger model (slower but better quality)
generator = pipeline("text-generation", model="gpt2", device=0)
```

### Adjust TTS Speed
Edit `app.py` line:
```python
tts_engine.setProperty('rate', 150)  # Change 150 to 100-300
```

### Change Chunk Size
Edit `app.py` function `chunk_text()`:
```python
def chunk_text(text, chunk_size=1000, overlap=200):  # Adjust sizes
```

## Troubleshooting 🐛

### "Knowledge base not loaded"
- **Solution**: Add PDF files to the `pdfs` folder and restart

### Slow on first start
- **Solution**: First run downloads AI models. Subsequent runs are fast. This is normal!

### Speech recognition not working
- **Solution**: 
  - Use Chrome, Edge, or other Chromium-based browser
  - Safari and Firefox have limited STT support

### Out of memory error
- **Solution**: 
  - Close other applications
  - Reduce number of PDFs or their size
  - Use CPU instead of GPU

### Wrong or irrelevant answers
- **Solution**:
  - Make sure PDFs are in `pdfs` folder
  - Try asking more specific questions
  - Use similar wording to PDF content

## Performance Tips ⚡

1. **Fewer PDFs = Faster responses**: Start with 2-3 documents
2. **Smaller PDFs = Better quality**: Large PDFs may result in lower quality chunks
3. **Specific questions = Better answers**: More specific queries get better results
4. **Browser**: Use Chrome or Edge for best STT/TTS support

## Future Enhancements 🚀

- [ ] Multi-language support
- [ ] Persistent chat history
- [ ] Document management UI
- [ ] Advanced RAG (Reranking)
- [ ] Streaming responses
- [ ] Docker containerization
- [ ] Mobile app

## License 📄

Free to use and modify for personal and commercial projects.

## Support 💬

For issues or questions:
1. Check the troubleshooting section
2. Ensure all dependencies are installed: `pip install -r requirements.txt`
3. Check that PDFs are in the correct folder
4. Restart the application

---

**Happy chatting! 🎉**
