# 🤖 AI CHATBOT WITH PDF KNOWLEDGE BASE

A **pure Python** AI chatbot that answers questions based on PDF documents using Speech-to-Text (STT), Language Models (LLM), and Text-to-Speech (TTS). **100% free, no frameworks, no frontend!**

## 🎯 Features

- ✅ **PDF Knowledge Base** - Load and search multiple PDF documents
- ✅ **Speech-to-Text** - Ask questions using your microphone
- ✅ **AI Response Generation** - Realistic, conversational answers
- ✅ **Text-to-Speech** - Hear responses spoken aloud
- ✅ **RAG (Retrieval Augmented Generation)** - Answers based on your documents
- ✅ **Offline Capable** - Works with local LLM (Ollama)
- ✅ **100% Free** - No paid APIs, no subscriptions
- ✅ **Pure Python** - No Flask, FastAPI, or other frameworks

## 🏗️ Architecture

```
User (Speech/Text)
        ↓
    [STT Module]
        ↓
    Query Processing
        ↓
    [Vector Search] ←→ [PDF Knowledge Base with Embeddings]
        ↓
    [Retrieved Context]
        ↓
    [LLM Module]
        ↓
    Generated Response
        ↓
    [TTS Module]
        ↓
    User (Speech/Text Output)
```

## 📦 Technology Stack (All Free)

| Component | Technology | Purpose |
|-----------|-----------|---------|
| PDF Processing | PyPDF2 | Extract text from PDFs |
| Embeddings | Sentence Transformers | Convert text to vectors |
| Vector Search | FAISS | Fast similarity search |
| Language Model | Ollama + Mistral | Generate responses |
| Speech-to-Text | SpeechRecognition | Convert speech to text |
| Text-to-Speech | pyttsx3 | Convert text to speech |
| Audio Input | PyAudio | Microphone input |

## 🚀 Quick Start

### 1. Install Dependencies
```bash
cd chatbotV2
pip install -r requirements.txt
```

### 2. Add PDF Files
Place your PDF files in the `knowledge_base/` folder:
```
chatbotV2/
  └─ knowledge_base/
     ├─ document1.pdf
     └─ document2.pdf
```

### 3. Optional: Install Ollama
For better AI responses (local, offline):
```bash
# Download from https://ollama.ai
# Then:
ollama serve
# In another terminal:
ollama pull mistral
```

### 4. Run the Chatbot

**Interactive Chat Mode:**
```bash
python chatbot.py
```

**Text-only Mode (no microphone needed):**
```bash
python chatbot.py --no-audio
```

**Single Query:**
```bash
python chatbot.py --no-audio "What does the document say?"
```

## 💻 Code Structure

### Main Files

**[chatbot.py](chatbot.py)** - Main application
- `Chatbot` class: Main orchestrator
- `chat_loop()`: Interactive conversation mode
- `process_query()`: Single query processing

**[pdf_loader.py](pdf_loader.py)** - PDF processing
- `PDFKnowledgeBase` class: Load and index PDFs
- `extract_text_from_pdf()`: Extract text from PDF
- `chunk_text()`: Split text into overlapping chunks
- `search()`: Vector similarity search

**[audio_handler.py](audio_handler.py)** - Audio I/O
- `AudioHandler` class: STT and TTS
- `speech_to_text()`: Microphone to text
- `text_to_speech()`: Text to speaker

**[llm_handler.py](llm_handler.py)** - AI responses
- `LLMHandler` class: Generate responses
- Supports Ollama (preferred) or template-based fallback

**[quick_start.py](quick_start.py)** - Example usage

## 🔄 How It Works

### 1. PDF Loading (Startup)
```
1. Scan knowledge_base/ folder for PDFs
2. Extract text from each PDF
3. Split text into 256-character chunks (with overlap)
4. Generate embeddings using Sentence Transformers
5. Store in FAISS vector database
```

### 2. User Query Processing (During Chat)
```
1. Capture user input (speech or text)
2. Generate embedding for query
3. Search vector DB for top-3 similar chunks
4. Send query + context to LLM
5. Generate conversational response
6. Output response (text + speech)
```

### 3. Response Generation
- Uses Ollama (if available) for realistic AI responses
- Falls back to template-based responses if Ollama unavailable
- Includes document context for accuracy

## 📝 Example Usage

### Interactive Chat
```bash
python chatbot.py

🤖 INITIALIZING AI CHATBOT
1️⃣  Loading PDF Knowledge Base...
   Found 2 PDF files
   Processing document1.pdf...
   Total chunks created: 150
✅ Knowledge base loaded!

2️⃣  Initializing Audio Handler...
✅ Audio handler ready!

💬 CHAT MODE
🎤 Say something or type your question:
> What are the main topics?

🔍 Searching knowledge base...
📚 Retrieved Documents:
   1. document1.pdf (relevance: 0.85)

🤔 Generating response...
🤖 Bot: Based on the documents, the main topics covered are...
```

### Programmatic Usage
```python
from chatbot import Chatbot

# Initialize
bot = Chatbot(kb_folder="knowledge_base", use_audio=False)

# Ask a question
response = bot.process_query("What is the main topic?")
print(response)

# Clean up
bot.close()
```

## 🎨 Customization

### Adjust Response Quality
Edit `llm_handler.py`:
```python
# Temperature: 0.0 = deterministic, 1.0 = creative
"temperature": 0.7,  # Modify this
```

### Change PDF Chunking
Edit `pdf_loader.py`:
```python
chunks = self.chunk_text(text, chunk_size=512, overlap=100)  # Adjust these
```

### Use Different Embedding Model
Edit `pdf_loader.py`:
```python
model_name="all-mpnet-base-v2"  # More accurate but slower
```

### Use Different LLM Model
Edit `llm_handler.py`:
```python
self.model = "llama2"  # or "neural-chat", "orca-mini"
```

## 🐛 Troubleshooting

### "No PDFs found"
- Check `knowledge_base/` folder exists
- Ensure PDFs end with `.pdf`
- Run: `ls knowledge_base/` (Linux/Mac) or `dir knowledge_base/` (Windows)

### Audio not working
- Check microphone is connected
- Test: `python -m speech_recognition`
- Use text mode: `python chatbot.py --no-audio`

### Slow startup (first run)
- Normal! Models are being downloaded
- Subsequent runs are much faster
- Progress bar will show

### "Ollama not available"
- Install from https://ollama.ai
- Run `ollama serve` in separate terminal
- Restart chatbot

## ⚡ Performance

| Operation | Time |
|-----------|------|
| First run (model download) | 2-5 min |
| Startup (after first run) | 30-60 sec |
| PDF loading (100 pages) | 10-20 sec |
| Vector search | < 1 sec |
| Response generation | 5-30 sec |

## 📚 Example PDFs for Testing

1. **Technical Documentation** - Computer science concepts
2. **Company Manual** - HR policies, procedures
3. **Product Guide** - Features, specifications
4. **Research Paper** - Academic content

Supported PDF types:
- ✅ Text-based PDFs (scanned with OCR)
- ❌ Image-only PDFs (no text layer)
- ✅ Multi-page PDFs
- ✅ PDFs with tables and lists

## 🔐 Privacy & Security

- ✅ **No cloud** - Everything runs locally
- ✅ **No data sent** - No external API calls (unless you use online TTS)
- ✅ **No tracking** - Pure Python, no telemetry
- ✅ **Privacy mode** - Use `--no-audio` for silent operation

## 🎓 Learning Resources

### Understanding RAG (Retrieval Augmented Generation)
The chatbot uses RAG to answer questions accurately:
1. **Retrieval** - Find relevant chunks from PDFs
2. **Augmentation** - Combine with user query
3. **Generation** - Use LLM to generate answer

### Embedding Models
Used to convert text to vectors for similarity search:
- `all-MiniLM-L6-v2` - Fast (default)
- `all-mpnet-base-v2` - More accurate
- `paraphrase-MiniLM-L6-v2` - Better for semantic similarity

## 🚧 Future Enhancements

- [ ] Support for DOC, DOCX files
- [ ] Web interface
- [ ] Multiple language support
- [ ] Document summarization
- [ ] Custom system prompts
- [ ] Chat history
- [ ] Performance metrics

## 📄 License

MIT License - Free to use and modify

## 🤝 Contributing

Contributions welcome! Areas:
- Additional file format support
- Better embedding models
- Alternative LLMs
- Performance optimization

## ⭐ Tips for Best Results

1. **Clear PDFs** - Text-based, well-formatted PDFs work best
2. **Relevant Content** - PDFs matching expected questions
3. **Adjust Chunk Size** - Larger for big topics, smaller for specific Q&A
4. **Speak Clearly** - For better STT accuracy
5. **Local LLM** - Install Ollama for best experience

---

**Built with ❤️ using Python** | **100% Free & Open Source**
