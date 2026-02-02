from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import requests

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

PDF_DIR = Path("pdfs")
PDF_DIR.mkdir(exist_ok=True)
AUDIO_DIR = Path("uploads")
AUDIO_DIR.mkdir(exist_ok=True)

pdf_content = ""
whisper_model = None

def get_relevant_chunks(question, pdf_text, num_chunks=3):
    """Get most relevant chunks from PDF"""
    if not pdf_text:
        return []
    
    q_words = set(question.lower().split())
    chunks = []
    
    for i in range(0, len(pdf_text), 200):
        chunk = pdf_text[i:i+300]
        c_words = set(chunk.lower().split())
        score = len(q_words & c_words) / max(len(q_words), 1)
        if score > 0:
            chunks.append((chunk, score))
    
    chunks.sort(key=lambda x: x[1], reverse=True)
    return [c[0] for c in chunks[:num_chunks]]

def generate_smart_answer(question, context):
    """Use Ollama to generate answer"""
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": f"Based on: {context}\n\nQ: {question}\n\nShort answer:",
                "stream": False,
                "temperature": 0.3
            },
            timeout=10
        )
        if response.status_code == 200:
            result = response.json().get("response", "").strip()
            return result if result else context[:150]
    except:
        pass
    return context[:150]

HTML = """<!DOCTYPE html>
<html>
<head>
    <title>PDF Voice Chat</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial; background: #f0f2f5; height: 100vh; display: flex; }
        .sidebar { width: 280px; background: #1a1a2e; color: white; padding: 20px; }
        .sidebar h2 { margin-bottom: 20px; font-size: 20px; }
        .btn { width: 100%; padding: 12px; margin: 8px 0; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; }
        .btn-primary { background: #3498db; }
        .btn-primary:hover { background: #2980b9; }
        .btn-record { background: #e74c3c; }
        .btn-record:hover { background: #c0392b; }
        .btn-record.active { background: #c0392b; animation: pulse 1s infinite; }
        @keyframes pulse { 0%, 100% { box-shadow: 0 0 0 0 rgba(231, 76, 60, 0.7); } 50% { box-shadow: 0 0 0 15px rgba(231, 76, 60, 0); } }
        .status { background: rgba(255,255,255,0.1); padding: 10px; border-radius: 5px; font-size: 12px; margin-top: 8px; }
        .chat { flex: 1; display: flex; flex-direction: column; background: white; }
        .messages { flex: 1; overflow-y: auto; padding: 20px; }
        .msg { margin: 10px 0; padding: 12px 15px; border-radius: 8px; max-width: 85%; }
        .msg.user { background: #3498db; color: white; margin-left: auto; }
        .msg.bot { background: #ecf0f1; color: #2c3e50; }
        .input-area { padding: 15px; background: white; border-top: 1px solid #ddd; }
        input { width: 100%; padding: 10px; border: 2px solid #ddd; border-radius: 5px; }
        input:focus { outline: none; border-color: #3498db; }
        input[type="file"] { display: none; }
    </style>
</head>
<body>
    <div class="sidebar">
        <h2>🎙️ PDF Chat</h2>
        <input type="file" id="pdf" accept=".pdf">
        <button class="btn btn-primary" onclick="document.getElementById('pdf').click()">📁 Upload PDF</button>
        <div class="status" id="pdf-status">No PDF</div>
        
        <button class="btn btn-record" id="record-btn" onclick="toggleRecord()">🎤 Record</button>
        <div class="status" id="record-status">Ready</div>
    </div>
    
    <div class="chat">
        <div class="messages" id="messages"></div>
        <div class="input-area">
            <input type="text" id="text-input" placeholder="Type or click record..." onkeypress="if(event.key==='Enter') sendText()">
        </div>
    </div>

    <script>
        let mediaRecorder;
        let chunks = [];
        
        document.getElementById('pdf').addEventListener('change', async (e) => {
            const file = e.target.files[0];
            if (!file) return;
            const form = new FormData();
            form.append('file', file);
            document.getElementById('pdf-status').textContent = '⏳...';
            try {
                const r = await fetch('/upload-pdf', { method: 'POST', body: form });
                const d = await r.json();
                document.getElementById('pdf-status').textContent = d.status;
            } catch (e) {
                document.getElementById('pdf-status').textContent = '❌';
            }
        });
        
        async function toggleRecord() {
            const btn = document.getElementById('record-btn');
            if (mediaRecorder && mediaRecorder.state === 'recording') {
                mediaRecorder.stop();
                btn.classList.remove('active');
                btn.textContent = '🎤 Record';
            } else {
                chunks = [];
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                    mediaRecorder = new MediaRecorder(stream);
                    mediaRecorder.ondataavailable = (e) => chunks.push(e.data);
                    mediaRecorder.onstop = async () => {
                        const blob = new Blob(chunks, { type: 'audio/webm' });
                        const form = new FormData();
                        form.append('audio', blob, 'rec.webm');
                        
                        addMsg('⏳ Processing...', 'bot');
                        try {
                            const r = await fetch('/transcribe', { method: 'POST', body: form });
                            const d = await r.json();
                            if (d.success) {
                                document.getElementById('messages').removeChild(document.getElementById('messages').lastChild);
                                addMsg('You: ' + d.text, 'user');
                                
                                const cr = await fetch('/chat', {
                                    method: 'POST',
                                    headers: { 'Content-Type': 'application/json' },
                                    body: JSON.stringify({ q: d.text })
                                });
                                const cd = await cr.json();
                                addMsg(cd.answer, 'bot');
                            }
                        } catch (e) {
                            document.getElementById('messages').removeChild(document.getElementById('messages').lastChild);
                            addMsg('❌ Error: ' + e.message, 'bot');
                        }
                    };
                    mediaRecorder.start();
                    btn.classList.add('active');
                    btn.textContent = '⏹️ Stop';
                    document.getElementById('record-status').textContent = '🔴 Recording';
                } catch (e) {
                    alert('Mic error: ' + e.message);
                }
            }
        }
        
        async function sendText() {
            const input = document.getElementById('text-input');
            const text = input.value.trim();
            if (!text) return;
            input.value = '';
            addMsg('You: ' + text, 'user');
            try {
                const r = await fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ q: text })
                });
                const d = await r.json();
                addMsg(d.answer, 'bot');
            } catch (e) {
                addMsg('❌ Error', 'bot');
            }
        }
        
        function addMsg(text, type) {
            const msgs = document.getElementById('messages');
            const div = document.createElement('div');
            div.className = 'msg ' + type;
            div.textContent = text;
            msgs.appendChild(div);
            msgs.scrollTop = msgs.scrollHeight;
        }
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def home():
    return HTML

@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    global pdf_content
    try:
        from pypdf import PdfReader
        path = PDF_DIR / file.filename
        content = await file.read()
        with open(path, "wb") as f:
            f.write(content)
        reader = PdfReader(path)
        pdf_content = " ".join([p.extract_text() or "" for p in reader.pages])
        return {"status": f"✅ {len(pdf_content)//100} KB loaded"}
    except:
        return {"status": "❌ Error"}, 400

@app.post("/transcribe")
async def transcribe(audio: UploadFile = File(...)):
    try:
        import whisper
        global whisper_model
        if whisper_model is None:
            whisper_model = whisper.load_model("base")
        
        path = AUDIO_DIR / "audio.webm"
        with open(path, "wb") as f:
            f.write(await audio.read())
        result = whisper_model.transcribe(str(path), language="en")
        text = result["text"].strip()
        return {"success": True, "text": text}
    except Exception as e:
        return {"success": False, "error": str(e)}, 400

@app.post("/chat")
async def chat(data: dict):
    question = data.get("q", "").strip()
    if not pdf_content:
        return {"answer": "Upload PDF first"}
    
    relevant = get_relevant_chunks(question, pdf_content)
    context = " ".join(relevant) if relevant else pdf_content[:300]
    answer = generate_smart_answer(question, context)
    
    return {"answer": answer}

if __name__ == "__main__":
    import uvicorn
    print("🚀 http://localhost:8000")
    print("📌 Whisper + Ollama ready")
    uvicorn.run(app, host="0.0.0.0", port=8000)
