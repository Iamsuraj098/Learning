# Complete Chatbot Installation & Usage Guide

## 📋 System Requirements

- **OS**: Windows 10+, macOS, or Linux
- **Python**: 3.8 or higher
- **RAM**: Minimum 8GB (16GB recommended)
- **Disk Space**: 3-5GB for models
- **Browser**: Chrome, Edge, or Brave (for STT/TTS support)

---

## ⚡ Quick Start (Windows)

### Option 1: Automatic Setup (Recommended)
```bash
setup.bat
```
Just double-click `setup.bat` file in the Chatbot folder. It will handle everything!

### Option 2: Manual Setup
1. Open PowerShell/Command Prompt
2. Navigate to the Chatbot folder
3. Run:
```bash
pip install -r requirements.txt
```

---

## 📝 Step-by-Step Setup Guide

### Step 1: Install Python (if not already installed)
1. Go to https://www.python.org/downloads/
2. Download Python 3.9 or 3.10
3. **IMPORTANT**: During installation, check "Add Python to PATH"
4. Click "Install Now"

**Verify installation:**
```bash
python --version
```
Should show: `Python 3.9.x` or similar

### Step 2: Install Dependencies
1. Open PowerShell/Command Prompt
2. Navigate to Chatbot folder:
```bash
cd "C:\Users\YourUsername\Desktop\New folder\AI\Chatbot"
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

**⏱️ This takes 10-15 minutes on first run** (downloading AI models ~2GB)

### Step 3: Prepare PDF Files
1. Go to the `pdfs` folder inside Chatbot directory
2. Add your PDF files (minimum 1, recommend 2-5 for best results)
3. Supported formats: `.pdf`

Example:
```
Chatbot/
├── pdfs/
│   ├── company_handbook.pdf
│   ├── product_guide.pdf
│   └── faq.pdf
```

### Step 4: Run the Application
Open PowerShell/Command Prompt in Chatbot folder and run:
```bash
python app.py
```

**Expected output:**
```
🚀 Initializing Chatbot Components...
📚 Loading Embedding Model...
🤖 Loading Language Model...
🔊 Initializing Text-to-Speech...
📂 Initializing Knowledge Base from 'pdfs' folder...
📄 Found 3 PDF files
📖 Processing: company_handbook.pdf...
✅ Total chunks created: 342
✅ Knowledge base initialized successfully!

🌐 Starting Flask server...
📍 Open your browser at: http://localhost:5000
```

### Step 5: Open in Browser
1. Open any web browser
2. Go to: **http://localhost:5000**
3. Start chatting!

---

## 🎤 How to Use the Chatbot

### Text Chat
1. Type your question in the input box
2. Press Enter or click "Send"
3. Wait for response (usually 2-5 seconds)
4. Continue the conversation

### Voice Input (Speech-to-Text)
1. Click the 🎤 microphone button
2. Speak your question clearly
3. Wait for text to appear
4. Question is automatically sent
5. **Note**: Works best in Chrome/Edge

### Voice Output (Text-to-Speech)
- Responses are **automatically read aloud**
- OR click 🔊 speaker button to replay the last response
- **Note**: Works best in Chrome/Edge

### Example Questions
- "What does the document say about..."
- "Tell me about..."
- "How do I..."
- "Summarize the..."

---

## 🐛 Troubleshooting

### Issue: "Python is not recognized"
**Cause**: Python not installed or not in PATH
**Solution**:
1. Uninstall Python completely
2. Reinstall from https://www.python.org/downloads/
3. **IMPORTANT**: Check "Add Python to PATH" during installation
4. Restart PowerShell/Command Prompt

### Issue: "No module named 'flask'"
**Cause**: Dependencies not installed
**Solution**:
```bash
pip install -r requirements.txt
```

### Issue: "Connection refused" or "Can't reach localhost:5000"
**Cause**: Server not running
**Solution**:
1. Make sure `python app.py` is still running
2. Check PowerShell/Command Prompt window
3. If stopped, run `python app.py` again

### Issue: "Knowledge base not loaded" error
**Cause**: No PDF files in `pdfs` folder
**Solution**:
1. Add at least one PDF file to `pdfs` folder
2. Restart the app: Press Ctrl+C, then `python app.py` again

### Issue: Speech recognition not working
**Cause**: Browser doesn't support Web Speech API
**Solution**:
1. Use Chrome, Edge, or Brave browser
2. Check microphone permissions
3. Allow microphone access when prompted

### Issue: Text-to-Speech not playing
**Cause**: Browser or speaker issues
**Solution**:
1. Check speaker volume
2. Try different browser
3. Check browser media permissions

### Issue: Very slow responses
**Cause**: Large PDF files or weak computer
**Solution**:
1. Use smaller PDF files
2. Use fewer PDFs (2-3 maximum)
3. Close other applications
4. Increase computer RAM if possible

### Issue: "OutOfMemory" error
**Cause**: Not enough RAM
**Solution**:
1. Close other applications
2. Reduce number of PDFs
3. Split large PDFs into smaller ones
4. Increase system RAM

### Issue: Wrong or irrelevant answers
**Cause**: 
- Questions don't match PDF content
- PDFs not properly indexed
**Solution**:
1. Ask more specific questions
2. Use similar terminology to PDFs
3. Restart app to re-index PDFs
4. Check that PDFs have readable text

---

## 💾 File Structure Explained

```
Chatbot/
│
├── app.py                    # Main backend application
├── requirements.txt          # Python dependencies
├── setup.bat                 # Windows setup script
├── setup.sh                  # Linux/Mac setup script
├── README.md                 # Full documentation
├── QUICKSTART_WINDOWS.md     # Quick start guide
├── ADVANCED_CONFIG.md        # Advanced settings
├── advanced_llm.py           # Optional better LLM
│
├── templates/
│   └── index.html           # Web interface (what you see in browser)
│
├── pdfs/                     # Your PDF files (add here!)
│   ├── document1.pdf
│   └── document2.pdf
│
└── venv/                     # Virtual environment (created after setup)
    └── (Python packages)
```

---

## ⚙️ Advanced Configuration

### Change AI Model Quality (in app.py)

**Faster but less accurate:**
```python
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
```

**Slower but more accurate:**
```python
embedding_model = SentenceTransformer('all-mpnet-base-v2')
```

### Adjust Context Amount
Find in app.py:
```python
context = retrieve_relevant_context(user_query, top_k=3)  # Change 3 to 5 for more context
```

### Change Text-to-Speech Speed
Find in app.py:
```python
tts_engine.setProperty('rate', 150)  # 50=slow, 150=normal, 300=fast
```

### Use Better LLM (requires more memory)
See `advanced_llm.py` for examples

---

## 🚀 Optimization Tips

### For Better Performance:
1. ✅ Use 2-5 small PDFs instead of 1 large PDF
2. ✅ Use Chrome or Edge browser
3. ✅ Close other applications
4. ✅ Place PDFs with readable text (not scanned images)

### For Better Answers:
1. ✅ Ask specific questions
2. ✅ Use terminology similar to PDFs
3. ✅ Provide context in questions
4. ✅ Ask follow-up questions for clarification

### For Faster Responses:
1. ✅ Reduce number of context chunks (top_k=2)
2. ✅ Use smaller embedding model
3. ✅ Reduce PDF file count

---

## 📊 How It Works Behind the Scenes

```
You Ask a Question
        ↓
    [STT: Convert voice to text if using mic]
        ↓
    [Embed question into mathematical representation]
        ↓
    [Search PDF knowledge base for similar chunks]
        ↓
    [Retrieve most relevant 3 chunks]
        ↓
    [Send to AI model with context]
        ↓
    [AI generates natural response]
        ↓
    [Display text in chat]
        ↓
    [TTS: Convert response to speech automatically]
        ↓
    [Play audio to speaker]
```

---

## 📱 Supported Platforms

| Platform | STT | TTS | Notes |
|----------|-----|-----|-------|
| Chrome (Windows/Mac/Linux) | ✅ | ✅ | Full support, recommended |
| Edge (Windows) | ✅ | ✅ | Full support |
| Firefox | ⚠️ | ✅ | Limited STT support |
| Safari (Mac) | ❓ | ✅ | Limited STT support |
| Mobile Browsers | ⚠️ | ✅ | Partial support |

---

## 🔒 Privacy & Security

✅ **All processing happens locally**
- ✅ PDFs never uploaded to cloud
- ✅ No personal data collection
- ✅ No third-party API calls
- ✅ 100% offline capable (after initial setup)

---

## 🎓 Learning Resources

- **Flask**: https://flask.palletsprojects.com/
- **Sentence Transformers**: https://www.sbert.net/
- **FAISS**: https://github.com/facebookresearch/faiss
- **Hugging Face**: https://huggingface.co/

---

## 💬 Common Questions

### Q: Can I use with cloud storage (Google Drive, OneDrive)?
**A**: The current version reads from local `pdfs` folder. You could sync it with cloud storage.

### Q: Can I deploy online?
**A**: Yes! Use platforms like Heroku, Railway, or Render. See ADVANCED_CONFIG.md

### Q: Does it work without internet?
**A**: First setup needs internet (model download). After that, it works offline.

### Q: Can I add more PDFs without restarting?
**A**: Add PDFs to `pdfs` folder, then go to Status page and click "Reload"

### Q: Can I use different languages?
**A**: Yes, with appropriate language models. Currently optimized for English.

### Q: What if I have very large PDFs?
**A**: Split them into smaller PDFs. Larger files = longer processing time.

---

## 🆘 Still Having Issues?

1. **Check the logs**: Look at the PowerShell/Command Prompt output
2. **Read error messages carefully**: They often suggest solutions
3. **Try restarting**: Close and reopen the application
4. **Verify installation**: Run `pip list` to check all packages
5. **Check Python version**: Run `python --version`

---

## 📞 Getting Help

1. Run `python app.py` again - might fix temporary issues
2. Delete `pdfs` folder content and add simple test PDF
3. Check your PDF files are not corrupted
4. Try with a different PDF
5. Reinstall all dependencies: `pip install -r requirements.txt --force-reinstall`

---

**Happy Chatting! 🚀**

*For more information, see README.md or ADVANCED_CONFIG.md*
