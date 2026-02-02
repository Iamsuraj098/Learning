@echo off
REM POC Verification Script
REM Tests if all components are ready

echo.
echo ╔════════════════════════════════════════╗
echo ║   PDF Agent Chatbot - POC Verify       ║
echo ╚════════════════════════════════════════╝
echo.

echo 1. Checking Python...
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo    ✓ Python installed
) else (
    echo    ✗ Python NOT installed
    goto error
)

echo.
echo 2. Checking Ollama...
curl -s http://localhost:11434/api/tags >nul 2>&1
if %errorlevel% equ 0 (
    echo    ✓ Ollama running
) else (
    echo    ✗ Ollama NOT running
    echo    Start with: ollama pull mistral ^& ollama serve
    goto warning
)

echo.
echo 3. Checking project files...
if exist backend\app.py (
    echo    ✓ app.py found
) else (
    echo    ✗ app.py NOT found
    goto error
)

if exist backend\config.py (
    echo    ✓ config.py found
) else (
    echo    ✗ config.py NOT found
    goto error
)

if exist backend\pdf_loader.py (
    echo    ✓ pdf_loader.py found
) else (
    echo    ✗ pdf_loader.py NOT found
    goto error
)

if exist backend\llm_service.py (
    echo    ✓ llm_service.py found
) else (
    echo    ✗ llm_service.py NOT found
    goto error
)

if exist backend\requirements.txt (
    echo    ✓ requirements.txt found
) else (
    echo    ✗ requirements.txt NOT found
    goto error
)

if exist pdfs (
    echo    ✓ pdfs folder exists
) else (
    echo    ✗ pdfs folder NOT found
    mkdir pdfs
    echo    Created pdfs folder
)

echo.
echo 4. Checking documentation...
if exist README.md (
    echo    ✓ README.md found
) else (
    echo    ✗ README.md NOT found
)

if exist POC_SETUP.md (
    echo    ✓ POC_SETUP.md found
) else (
    echo    ✗ POC_SETUP.md NOT found
)

if exist POC_COMPLETE.md (
    echo    ✓ POC_COMPLETE.md found
) else (
    echo    ✗ POC_COMPLETE.md NOT found
)

echo.
echo ╔════════════════════════════════════════╗
echo ║  ✓ POC READY FOR TESTING              ║
echo ╚════════════════════════════════════════╝
echo.
echo Next steps:
echo   1. Add your PDF to pdfs/ folder
echo   2. Run: python backend/app.py
echo   3. Open: http://localhost:5000
echo   4. Click "Load PDFs" button
echo   5. Start asking questions!
echo.
goto end

:warning
echo.
echo ⚠ WARNING: Some components may not be ready
echo Check and fix the issues above

:error
echo.
echo ✗ ERROR: Setup incomplete
echo Please fix the errors above

:end
echo.
