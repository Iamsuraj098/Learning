# Quick Start Guide for Windows

## One-Command Setup

```bash
setup.bat
```

This will:
1. ✅ Install Python dependencies
2. ✅ Create virtual environment
3. ✅ Set up folders
4. ✅ Display next steps

## Manual Setup (if setup.bat doesn't work)

### 1. Install Python
- Download from: https://www.python.org/downloads/
- **Important**: Check "Add Python to PATH" during installation

### 2. Install Dependencies
Open PowerShell/Command Prompt and run:
```bash
cd "path\to\Chatbot"
pip install -r requirements.txt
```

### 3. Add PDF Files
- Create/use `pdfs` folder
- Add your `.pdf` files there

### 4. Run the App
```bash
python app.py
```

### 5. Open Browser
Visit: **http://localhost:5000**

## If Installation Fails

### Error: "python is not recognized"
- Python not installed or not in PATH
- Solution: Reinstall Python and check "Add Python to PATH"

### Error: "Permission denied"
- Run PowerShell as Administrator
- Then run the commands again

### Error: "No module named 'flask'"
- Dependencies not installed
- Run: `pip install -r requirements.txt`

### Out of Memory
- Close other applications
- Reduce PDF file count
- Restart computer if needed

## Tips

💡 **First run takes longer** (downloading AI models ~2GB)
💡 **Subsequent runs are faster**
💡 **Use Chrome for best STT/TTS support**
💡 **Add 2-5 PDFs for best performance**

---

Need help? Check README.md for more details.
