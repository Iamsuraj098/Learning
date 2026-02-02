# AI Chatbot Setup Guide

## Prerequisites
- Python 3.8+
- pip (Python package manager)
- Microphone (optional, for voice input)
- Speakers (optional, for voice output)

## Installation Steps

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Optional: Install Ollama (for better AI responses)
For offline, free LLM inference:
1. Download from: https://ollama.ai
2. Install and run Ollama
3. Download a model: `ollama pull mistral` or `ollama pull llama2`
4. Run: `ollama serve`

If Ollama is not available, the chatbot will use template-based responses.

### 3. Add PDF Files to Knowledge Base
1. Create PDF files or download them
2. Place them in the `knowledge_base/` folder
3. Example: `knowledge_base/document1.pdf`, `knowledge_base/document2.pdf`

### 4. Run the Chatbot

#### Interactive Chat Mode (with voice):
```bash
python chatbot.py
```

#### Text-only Mode (no voice):
```bash
python chatbot.py --no-audio
```

#### Single Query Mode:
```bash
python chatbot.py --no-audio "What is in the documents?"
```

## How It Works

1. **PDF Loading**: Reads all PDFs from `knowledge_base/` folder
2. **Text Extraction**: Extracts text and splits into chunks
3. **Embeddings**: Converts chunks to vectors for similarity search
4. **Query Processing**: User asks a question (voice or text)
5. **Knowledge Retrieval**: Finds similar chunks from PDFs
6. **Response Generation**: LLM generates conversational answer based on context
7. **Output**: Displays and speaks the response

## Troubleshooting

### "No PDFs found" error
- Make sure PDFs are in `knowledge_base/` folder
- Check file names end with `.pdf`

### Audio not working
- Check microphone is connected: `python -m speech_recognition`
- Try text mode: `python chatbot.py --no-audio`

### Slow responses
- This is normal on first run (loading models)
- Subsequent queries are faster
- Add fewer PDFs to reduce processing time

### "Ollama not available" message
- This is okay - the chatbot will work with template responses
- Install Ollama for better AI responses
- Or keep using the current mode

## Features

✅ **Free & Open Source**
✅ **Offline Operation** (with Ollama)
✅ **Speech Recognition** (STT)
✅ **Text-to-Speech** (TTS)
✅ **RAG (Retrieval Augmented Generation)**
✅ **No Framework Dependencies** (Pure Python)
✅ **Easy Setup** (One command)
✅ **Multi-PDF Support**

## Project Structure

```
chatbotV2/
├── chatbot.py           # Main chatbot application
├── pdf_loader.py        # PDF processing & embeddings
├── audio_handler.py     # Speech-to-text & text-to-speech
├── llm_handler.py       # Language model integration
├── requirements.txt     # Python dependencies
├── knowledge_base/      # Your PDF files here
└── setup_guide.md       # This file
```

## Example Usage

```python
from chatbot import Chatbot

# Initialize chatbot
bot = Chatbot(kb_folder="knowledge_base", use_audio=False)

# Ask a single question
bot.single_query_mode("What topics are covered in the documents?")

# Or start interactive chat
bot.chat_loop()
```

## Performance Notes

- **First Run**: 2-5 minutes (downloading models)
- **Subsequent Runs**: 30 seconds to 1 minute
- **Query Response**: 5-30 seconds (depends on model)
- **Vector Search**: < 1 second

## Tips for Best Results

1. **PDF Quality**: Use clear, text-based PDFs (not scanned images)
2. **Relevant Content**: PDFs directly related to expected questions work best
3. **Chunk Size**: Default is 256 characters - adjust in `pdf_loader.py` if needed
4. **Model Size**: Mistral is faster, Llama2 is more accurate
5. **Audio Quality**: Speak clearly for better speech recognition
