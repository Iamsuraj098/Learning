@echo off
REM Simple Startup Script - Just double-click to run!

echo.
echo ╔════════════════════════════════════════╗
echo ║   PDF Agent Chatbot - Starting          ║
echo ╚════════════════════════════════════════╝
echo.

echo ✓ Checking setup...
cd backend

REM Check if venv exists, if not create it
if not exist venv (
    echo Creating Python environment...
    python -m venv venv
)

REM Activate venv
call venv\Scripts\activate.bat

echo.
echo ✓ Starting Backend Server...
echo.
echo 🔗 Opening http://localhost:5000
echo Press Ctrl+C to stop the server
echo.

REM Start the app
python app.py
