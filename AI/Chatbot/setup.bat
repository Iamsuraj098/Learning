@echo off
REM Setup script for Windows

echo 🤖 Setting up AI Chatbot...
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found. Please install Python 3.8 or higher.
    echo Download from: https://www.python.org/downloads/
    exit /b 1
)

echo ✅ Python found: 
python --version

REM Create virtual environment
echo.
echo 📦 Creating virtual environment...
python -m venv venv

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install dependencies
echo.
echo 📚 Installing dependencies (this may take a few minutes)...
python -m pip install --upgrade pip
pip install -r requirements.txt

REM Create pdfs folder
if not exist pdfs mkdir pdfs

echo.
echo ✅ Setup complete!
echo.
echo 📝 Next steps:
echo 1. Add your PDF files to the 'pdfs' folder
echo 2. Run: python app.py
echo 3. Open your browser to: http://localhost:5000
echo.
pause
