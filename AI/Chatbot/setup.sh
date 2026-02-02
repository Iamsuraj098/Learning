#!/bin/bash
# Setup script for Linux/Mac

echo "🤖 Setting up AI Chatbot..."

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python found: $(python3 --version)"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "📚 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create pdfs folder
mkdir -p pdfs

echo ""
echo "✅ Setup complete!"
echo ""
echo "📝 Next steps:"
echo "1. Add your PDF files to the 'pdfs' folder"
echo "2. Activate environment: source venv/bin/activate"
echo "3. Run: python3 app.py"
echo "4. Open: http://localhost:5000"
echo ""
