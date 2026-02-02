from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from pypdf import PdfReader
import numpy as np
import requests
import json
from difflib import SequenceMatcher

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

pdf_chunks = []
OLLAMA_URL = "http://localhost:11434"

def chunk_text(text, chunk_size=250, overlap=30):
    """Create focused chunks"""
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunk = text[i:i + chunk_size].strip()
        if chunk and len(chunk) > 20:
            chunks.append(chunk)
    return chunks

def simple_similarity(query, chunks):
    """Simple similarity matching"""
    best_matches = []
    query_words = set(query.lower().split())
    
    for chunk in chunks:
        chunk_words = set(chunk.lower().split())
        intersection = len(query_words & chunk_words)
        similarity = intersection / max(len(query_words), len(chunk_words), 1)
        best_matches.append((chunk, similarity))
    
    return sorted(best_matches, key=lambda x: x[1], reverse=True)

def load_pdf(file_path):
    global pdf_chunks
    try:
        reader = PdfReader(file_path)
        full_text = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                full_text += text + " "
        
        full_text = " ".join(full_text.split())
        pdf_chunks = chunk_text(full_text)
        
        print(f"✓ PDF ready: {len(pdf_chunks)} chunks")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def search_similar(query, top_k=2):
    """Get best matching chunks"""
    if not pdf_chunks:
        return []
    
    matches = simple_similarity(query, pdf_chunks)
    return [chunk for chunk, sim in matches[:top_k] if sim > 0.1]

def generate_answer(question, context):
    """Use Ollama to generate smart response"""
    try:
        prompt = f"""Answer ONLY based on the context provided. Be direct and concise (1-2 sentences).

Context: {context}

Question: {question}

Answer:"""
        
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False,
                "temperature": 0.3,
                "num_predict": 100
            },
            timeout=10
        )
        
        if response.status_code == 200:
            answer = response.json().get("response", "").strip()
            if answer and len(answer) > 10:
                return answer
        return context[:200]
    except:
        # Fallback - just return context
        return context[:200]

HTML = """<!DOCTYPE html>
<html>
<head>
    <title>Smart PDF Chatbot</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f0f2f5; height: 100vh; display: flex; }
        .sidebar { width: 280px; background: linear-gradient(180deg, #2c3e50 0%, #34495e 100%); color: white; padding: 20px; display: flex; flex-direction: column; }
        .sidebar h2 { margin-bottom: 20px; font-size: 20px; font-weight: bold; }
        .upload-btn { padding: 12px; background: #3498db; border: none; color: white; border-radius: 6px; cursor: pointer; font-weight: bold; margin-bottom: 15px; transition: 0.3s; }
        .upload-btn:hover { background: #2980b9; transform: translateY(-2px); }
        .status { font-size: 13px; color: #bdc3c7; margin-top: 15px; background: rgba(255,255,255,0.1); padding: 10px; border-radius: 5px; }
        .chat-container { flex: 1; display: flex; flex-direction: column; }
        .messages { flex: 1; overflow-y: auto; padding: 20px; background: white; }
        .message { margin: 12px 0; padding: 12px 16px; border-radius: 12px; max-width: 85%; word-wrap: break-word; line-height: 1.6; animation: slideIn 0.3s ease; }
        @keyframes slideIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
        .user { background: #3498db; color: white; margin-left: auto; border-bottom-right-radius: 3px; }
        .bot { background: #ecf0f1; color: #2c3e50; border-bottom-left-radius: 3px; }
        .input-area { padding: 16px; background: white; border-top: 2px solid #e0e0e0; display: flex; gap: 10px; }
        input { flex: 1; padding: 12px 14px; border: 2px solid #ddd; border-radius: 6px; font-size: 14px; transition: 0.3s; }
        input:focus { outline: none; border-color: #3498db; box-shadow: 0 0 5px rgba(52, 152, 219, 0.3); }
        .voice-btn { padding: 12px 16px; background: #e74c3c; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 16px; transition: 0.3s; }
        .voice-btn:hover { background: #c0392b; }
        .voice-btn.recording { background: #c0392b; animation: pulse 0.6s infinite; }
        @keyframes pulse { 0%, 100% { box-shadow: 0 0 0 0 rgba(192, 57, 43, 0.7); } 50% { box-shadow: 0 0 0 10px rgba(192, 57, 43, 0); } }
        .send-btn { padding: 12px 25px; background: #27ae60; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: bold; transition: 0.3s; }
        .send-btn:hover { background: #229954; }
        .error { color: #e74c3c; background: #fadbd8; padding: 10px; border-radius: 5px; margin-top: 10px; }
        .success { color: #27ae60; background: #d5f4e6; padding: 10px; border-radius: 5px; }
    </style>
</head>
<body>
    <div class="sidebar">
        <h2>🤖 PDF Chat</h2>
        <input type="file" id="pdf" accept=".pdf" style="display:none;">
        <button class="upload-btn" onclick="document.getElementById('pdf').click()">📁 Upload PDF</button>
        <div class="status" id="status">📄 No PDF loaded</div>
    </div>
    <div class="chat-container">
        <div class="messages" id="messages"></div>
        <div class="input-area">
            <input type="text" id="input" placeholder="Type or click 🎤 to speak..." onkeypress="if(event.key==='Enter') send()">
            <button class="voice-btn" id="voice-btn" onclick="toggleVoice()" title="Click to speak">🎤</button>
            <button class="send-btn" onclick="send()">➤</button>
        </div>
    </div>

    <script>
        const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition || window.mozSpeechRecognition || window.msSpeechRecognition)();
        if (!recognition) {
            alert('Speech Recognition not supported in your browser. Use Chrome, Edge, or Firefox.');
        }
        
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = 'en-US';
        let isListening = false;

        document.getElementById('pdf').addEventListener('change', uploadPDF);

        function toggleVoice() {
            if (isListening) {
                recognition.stop();
                isListening = false;
                document.getElementById('voice-btn').classList.remove('recording');
            } else {
                recognition.start();
                isListening = true;
                document.getElementById('voice-btn').classList.add('recording');
            }
        }

        recognition.onstart = () => {
            document.getElementById('voice-btn').classList.add('recording');
            console.log('🎤 Listening...');
        };

        recognition.onend = () => {
            isListening = false;
            document.getElementById('voice-btn').classList.remove('recording');
        };

        recognition.onresult = (e) => {
            let transcript = '';
            for (let i = e.resultIndex; i < e.results.length; i++) {
                transcript += e.results[i][0].transcript + ' ';
            }
            if (transcript.trim()) {
                document.getElementById('input').value = transcript.trim();
                console.log('Transcribed:', transcript.trim());
                send();
            }
        };

        recognition.onerror = (e) => {
            console.error('Mic error:', e.error);
            const msgs = document.getElementById('messages');
            const errDiv = document.createElement('div');
            errDiv.className = 'message bot error';
            errDiv.textContent = '❌ Mic error: ' + e.error;
            msgs.appendChild(errDiv);
            isListening = false;
            document.getElementById('voice-btn').classList.remove('recording');
        };

        async function uploadPDF() {
            const file = document.getElementById('pdf').files[0];
            if (!file) return;
            const form = new FormData();
            form.append('file', file);
            document.getElementById('status').textContent = '⏳ Uploading...';
            
            try {
                const res = await fetch('/upload', { method: 'POST', body: form });
                const data = await res.json();
                document.getElementById('status').innerHTML = '<div style="background:rgba(39,174,96,0.2); padding:5px; border-radius:3px;">' + data.status + '</div>';
            } catch (e) {
                document.getElementById('status').innerHTML = '<div class="error">Error: ' + e.message + '</div>';
            }
        }

        async function send() {
            const input = document.getElementById('input');
            const msg = input.value.trim();
            if (!msg) return;
            input.value = '';

            const msgs = document.getElementById('messages');
            const userDiv = document.createElement('div');
            userDiv.className = 'message user';
            userDiv.textContent = msg;
            msgs.appendChild(userDiv);
            msgs.scrollTop = msgs.scrollHeight;

            const botDiv = document.createElement('div');
            botDiv.className = 'message bot';
            botDiv.textContent = '⏳ Thinking...';
            msgs.appendChild(botDiv);
            msgs.scrollTop = msgs.scrollHeight;

            try {
                const res = await fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: msg })
                });
                const data = await res.json();
                botDiv.textContent = data.response;
                msgs.scrollTop = msgs.scrollHeight;
                speak(data.response);
            } catch (e) {
                botDiv.textContent = '❌ Error: ' + e.message;
            }
        }

        function speak(text) {
            if ('speechSynthesis' in window) {
                speechSynthesis.cancel();
                const utterance = new SpeechSynthesisUtterance(text);
                utterance.rate = 0.95;
                utterance.pitch = 1;
                speechSynthesis.speak(utterance);
            }
        }
    </script>
</body>
</html>"""

@app.get("/", response_class=HTMLResponse)
def home():
    return HTML

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    Path("pdfs").mkdir(exist_ok=True)
    path = f"pdfs/{file.filename}"
    with open(path, "wb") as f:
        f.write(await file.read())
    if load_pdf(path):
        return {"status": f"✅ PDF loaded: {len(pdf_chunks)} chunks ready"}
    return {"status": "❌ Error loading PDF"}

@app.post("/chat")
async def chat(data: dict):
    question = data.get("message", "").strip()
    if not question or not pdf_chunks:
        return {"response": "Please upload a PDF first"}
    
    # Find relevant chunks
    chunks = search_similar(question, top_k=2)
    if not chunks:
        return {"response": "No matching information found in the PDF."}
    
    context = " ".join(chunks)
    
    # Generate smart answer using Ollama (or fallback)
    answer = generate_answer(question, context)
    
    return {"response": answer}

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting at http://localhost:8000")
    print("📌 Ollama: If you want AI responses, run 'ollama serve' in another terminal")
    print("✅ Otherwise, responses will be PDF excerpts\n")
    uvicorn.run(app, host="0.0.0.0", port=8000)
