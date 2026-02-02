# Installation & Setup Guide

## Step-by-Step Installation

### Prerequisites
- **Windows 10+**, **macOS**, or **Linux**
- **Python 3.8 or higher**
- **pip** (comes with Python)
- **Microphone** (optional, for voice input)
- **Speakers** (optional, for voice output)

---

## Windows Installation

### 1. Install Python
1. Download from: https://www.python.org/downloads/
2. Run installer, **CHECK "Add Python to PATH"**
3. Click "Install Now"

### 2. Verify Python Installation
Open PowerShell or Command Prompt:
```bash
python --version
pip --version
```

### 3. Clone/Download Chatbot
```bash
cd Desktop
git clone <chatbot-repo-url>
cd chatbotV2
```

Or download ZIP and extract to `chatbotV2` folder.

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

This installs:
- PyPDF2 (PDF reading)
- sentence-transformers (AI embeddings)
- faiss-cpu (vector search)
- torch (AI framework)
- pyttsx3 (text-to-speech)
- SpeechRecognition (speech-to-text)
- PyAudio (microphone input)

### 5. Add PDF Files
1. Create `knowledge_base` folder (if not exists)
2. Place PDF files there:
   ```
   chatbotV2/
     └─ knowledge_base/
        ├─ document1.pdf
        ├─ document2.pdf
        └─ ...
   ```

### 6. Test Installation
```bash
python test_components.py
```

Select option 2 (Audio Handler) to test if everything works.

### 7. Run Chatbot
```bash
python chatbot.py
```

---

## macOS Installation

### 1. Install Python (using Homebrew)
```bash
# Install Homebrew first (if needed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python@3.10

# Verify
python3 --version
```

### 2. Install Dependencies
```bash
cd chatbotV2
pip3 install -r requirements.txt
```

### 3. Install PyAudio (special step for macOS)
```bash
brew install portaudio
pip3 install PyAudio
```

### 4. Add PDFs and Run
Same as Windows steps 5-7

---

## Linux Installation

### Ubuntu/Debian:
```bash
# Install Python and dependencies
sudo apt-get update
sudo apt-get install python3 python3-pip python3-dev portaudio19-dev

# Install PyAudio specifically
pip3 install PyAudio

# Install chatbot dependencies
cd chatbotV2
pip3 install -r requirements.txt
```

### Fedora/RHEL:
```bash
sudo dnf install python3 python3-pip portaudio-devel
pip3 install PyAudio
cd chatbotV2
pip3 install -r requirements.txt
```

### Run:
```bash
python3 chatbot.py
```

---

## Optional: Install Ollama (Recommended)

For better AI responses using offline LLM:

### Windows:
1. Download: https://ollama.ai/download/windows
2. Run installer
3. Open PowerShell:
   ```bash
   ollama serve
   ```
4. In **new** PowerShell window:
   ```bash
   ollama pull mistral
   # or
   ollama pull llama2
   ```
5. Keep `ollama serve` running while using chatbot

### macOS:
```bash
brew install ollama
ollama serve

# In new terminal:
ollama pull mistral
```

### Linux:
```bash
curl https://ollama.ai/install.sh | sh
ollama serve

# In new terminal:
ollama pull mistral
```

---

## Verify Installation

### Quick Check
```bash
# Test each component
python test_components.py
```

### Full Test (requires PDFs)
```bash
python quick_start.py
```

### Minimal Test
```bash
python chatbot.py --no-audio
```

---

## Troubleshooting

### "Python not found"
- **Windows**: Reinstall Python, CHECK "Add to PATH"
- **macOS/Linux**: Use `python3` instead of `python`

### "pip: command not found"
- **Windows**: Use `python -m pip` instead
- **macOS**: Use `pip3` instead

### "No module named X"
```bash
# Reinstall requirements
pip install -r requirements.txt --force-reinstall
```

### Audio issues
```bash
# Test microphone
python -m speech_recognition

# Test speakers
python -c "import pyttsx3; pyttsx3.init().say('test'); pyttsx3.init().runAndWait()"
```

### PyAudio installation fails
**Windows**: 
```bash
pip install pipwin
pipwin install PyAudio
```

**macOS**:
```bash
brew install portaudio
pip install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio
```

**Linux**: Ensure `portaudio19-dev` is installed

### "Ollama not available" error
- This is fine! Chatbot works without it
- Install Ollama if you want better AI responses
- Or keep using template-based mode

---

## Running the Chatbot

### Mode 1: Interactive with Voice
```bash
python chatbot.py
```
- Asks questions by voice
- Responds with voice
- Requires microphone & speakers

### Mode 2: Text Only
```bash
python chatbot.py --no-audio
```
- Type questions
- Read responses
- No microphone needed

### Mode 3: Single Query
```bash
python chatbot.py --no-audio "What is in the documents?"
```
- Quick answer to one question
- No interactive mode

### Mode 4: Quick Start Demo
```bash
python quick_start.py
```
- Runs example queries
- Then enters interactive mode

---

## Project Structure After Setup

```
chatbotV2/
├── chatbot.py              # Main application ⭐
├── pdf_loader.py           # PDF processing
├── audio_handler.py        # Speech I/O
├── llm_handler.py          # AI responses
├── quick_start.py          # Demo
├── test_components.py      # Tests
├── requirements.txt        # Dependencies
├── README.md               # Documentation
├── setup_guide.md          # This file
│
├── knowledge_base/         # Your PDFs here ⭐
│   ├── document1.pdf
│   └── document2.pdf
│
└── .cache/                 # Auto-created (models cache)
    └── [downloaded models]
```

---

## First Run

First run may take 5-10 minutes because it:
1. Downloads embedding model (~500MB)
2. Downloads language model (if Ollama is used)
3. Loads all PDFs into memory
4. Creates vector embeddings

**This is normal!** Subsequent runs are much faster (30-60 seconds).

---

## Performance Tips

1. **Use smaller PDFs**: 10-50 pages each
2. **Use text-based PDFs**: Not scanned images
3. **Close other apps**: Frees up RAM
4. **Use SSD**: Faster loading
5. **Start Ollama separately**: Doesn't tie up Python

---

## Uninstall/Cleanup

### Remove chatbot:
```bash
rm -rf chatbotV2  # Linux/macOS
rmdir /s chatbotV2  # Windows
```

### Remove Python dependencies:
```bash
pip uninstall -r requirements.txt -y
```

### Remove Ollama:
- Windows: Go to Settings → Apps → Remove Ollama
- macOS: `brew uninstall ollama`
- Linux: `sudo apt-get remove ollama`

---

## Getting Help

1. **Check README.md** for features and examples
2. **Run test_components.py** to debug each part
3. **Check troubleshooting** above
4. **Verify PDFs exist** in `knowledge_base/` folder
5. **Check internet connection** if downloading models

---

**Ready to start?** Run: `python chatbot.py --no-audio`
