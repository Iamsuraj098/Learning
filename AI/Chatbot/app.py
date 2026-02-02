import os
import json
import numpy as np
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pdfplumber
from sentence_transformers import SentenceTransformer
import faiss
import torch
from transformers import pipeline
import pyttsx3

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Initialize components
print("🚀 Initializing Chatbot Components...")

# 1. Load Sentence Transformer for embeddings
print("📚 Loading Embedding Model...")
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# 2. Load LLM (using Hugging Face for context enhancement)
print("🤖 Loading Language Model...")
try:
    generator = pipeline("text-generation", model="gpt2", device=-1)
except:
    print("⚠️ LLM loading failed, using context-only mode...")
    generator = None

# 3. Initialize TTS engine
print("🔊 Initializing Text-to-Speech...")
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 150)  # Speed of speech

# Global variables for knowledge base
knowledge_base = []
vector_store = None
metadata_store = []
pdf_folder = "pdfs"

# ============================================================================
# KNOWLEDGE BASE MANAGEMENT
# ============================================================================

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF file"""
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                text += f"\n[Page {page_num + 1}]\n"
                text += page.extract_text() or ""
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text

def chunk_text(text, chunk_size=500, overlap=100):
    """Split text into overlapping chunks"""
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunk = text[i:i + chunk_size]
        if len(chunk.strip()) > 50:  # Only keep meaningful chunks
            chunks.append(chunk.strip())
    return chunks

def initialize_knowledge_base():
    """Load all PDFs from the pdfs folder and create vector store"""
    global knowledge_base, vector_store, metadata_store
    
    print(f"📂 Initializing Knowledge Base from '{pdf_folder}' folder...")
    
    # Create pdfs folder if it doesn't exist
    os.makedirs(pdf_folder, exist_ok=True)
    
    knowledge_base = []
    metadata_store = []
    
    # Process all PDFs in the folder
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    
    if not pdf_files:
        print(f"⚠️ No PDF files found in '{pdf_folder}' folder")
        print(f"📝 Please add PDF files to the '{pdf_folder}' folder")
        return False
    
    print(f"📄 Found {len(pdf_files)} PDF files")
    
    for pdf_file in pdf_files:
        print(f"📖 Processing: {pdf_file}...")
        pdf_path = os.path.join(pdf_folder, pdf_file)
        
        # Extract text
        text = extract_text_from_pdf(pdf_path)
        
        # Create chunks
        chunks = chunk_text(text)
        
        # Store chunks with metadata
        for i, chunk in enumerate(chunks):
            knowledge_base.append(chunk)
            metadata_store.append({
                "source": pdf_file,
                "chunk": i,
                "text": chunk[:100] + "..."
            })
    
    print(f"✅ Total chunks created: {len(knowledge_base)}")
    
    if len(knowledge_base) == 0:
        print("⚠️ No text content extracted from PDFs")
        return False
    
    # Create embeddings and FAISS vector store
    print("🔢 Creating embeddings...")
    embeddings = embedding_model.encode(knowledge_base, show_progress_bar=True)
    
    # Create FAISS index
    dimension = embeddings.shape[1]
    vector_store = faiss.IndexFlatL2(dimension)
    vector_store.add(embeddings.astype(np.float32))
    
    print("✅ Knowledge base initialized successfully!")
    return True

def retrieve_relevant_context(query, top_k=3):
    """Retrieve relevant chunks from knowledge base - filter out bad chunks"""
    if vector_store is None or len(knowledge_base) == 0:
        return ""
    
    try:
        # Encode query
        query_embedding = embedding_model.encode([query])[0]
        
        # Search in FAISS - get more candidates to filter
        k = min(top_k + 2, len(knowledge_base))
        distances, indices = vector_store.search(
            np.array([query_embedding]).astype(np.float32), 
            k
        )
        
        # Retrieve context - filter out bad/corrupted chunks
        context = ""
        added_chunks = set()
        
        for idx, distance in zip(indices[0], distances[0]):
            # Include chunks that are reasonably similar (distance < 2.0)
            if distance < 2.0:
                chunk = knowledge_base[idx]
                
                # Skip corrupted/bad chunks
                if len(chunk.strip()) < 20:
                    continue
                if chunk.startswith('equired') or chunk.startswith('roved'):
                    continue
                
                chunk_hash = hash(chunk[:100])
                
                if chunk_hash not in added_chunks:
                    context += chunk + "\n\n"
                    added_chunks.add(chunk_hash)
        
        return context.strip() if context else ""
    except Exception as e:
        print(f"Error retrieving context: {e}")
        return ""

# ============================================================================
# RESPONSE GENERATION
# ============================================================================

def generate_response(query, context):
    """Generate response using BOTH context + LLM for best accuracy"""
    
    try:
        # First: Try to get good context from PDFs
        if context and len(context.strip()) > 50:
            # Clean up context - remove bad chunks
            cleaned_context = clean_context(context)
            
            if cleaned_context and len(cleaned_context.strip()) > 30:
                # If we have good context, use LLM to enhance it
                if generator:
                    prompt = f"""Based on this document information:
{cleaned_context}

Answer this question: {query}

Provide a clear, concise answer using the document information above:"""
                    
                    try:
                        response = generator(
                            prompt,
                            max_length=200,
                            num_return_sequences=1,
                            temperature=0.3,  # Lower temp for accuracy
                            top_p=0.7,
                            do_sample=True
                        )
                        answer = response[0]['generated_text']
                        
                        # Extract just the answer part
                        if "answer" in answer.lower():
                            answer = answer.split("answer")[-1].strip()
                        answer = answer.replace("Provide", "").strip()
                        
                        if len(answer) > 15:
                            return answer
                    except:
                        pass
                
                # Fallback: Return cleaned context directly
                return f"Based on available documents:\n\n{cleaned_context}"
        
        # If no context found, use LLM to generate informed response
        if generator:
            prompt = f"Question: {query}\n\nProvide a helpful response:"
            try:
                response = generator(
                    prompt,
                    max_length=150,
                    num_return_sequences=1,
                    temperature=0.5,
                    top_p=0.8,
                    do_sample=True
                )
                answer = response[0]['generated_text'].split("response:")[-1].strip()
                if len(answer) > 10:
                    return answer
            except:
                pass
        
        return f"I don't have information about '{query}' in the current documents. Please add relevant PDF files to the knowledge base."
    
    except Exception as e:
        print(f"Error generating response: {e}")
        return f"Unable to process your question about '{query}'. Please try again or rephrase your question."

def clean_context(text):
    """Clean corrupted or bad context"""
    if not text:
        return ""
    
    # Remove fragments, keep only meaningful sentences
    lines = text.split('\n')
    clean_lines = []
    
    for line in lines:
        line = line.strip()
        # Skip very short lines or lines that look corrupted
        if len(line) > 15 and not line.startswith('['):
            # Check if line is reasonably English-like
            if not line.startswith('equired') and not line.startswith('roved'):
                clean_lines.append(line)
    
    return ' '.join(clean_lines[:5])  # Return first 5 good lines

# ============================================================================
# WEB ROUTES
# ============================================================================

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/api/status', methods=['GET'])
def status():
    """Check chatbot status and knowledge base"""
    return jsonify({
        "status": "running",
        "kb_loaded": len(knowledge_base) > 0,
        "documents": len(set([m["source"] for m in metadata_store])),
        "chunks": len(knowledge_base)
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    """Main chat endpoint"""
    try:
        data = request.json
        user_query = data.get('message', '').strip()
        
        if not user_query:
            return jsonify({"error": "Empty message"}), 400
        
        if len(knowledge_base) == 0:
            return jsonify({
                "error": "Knowledge base not loaded",
                "message": "No PDF files found. Please add PDF files to the 'pdfs' folder and restart the app"
            }), 400
        
        # Retrieve context
        context = retrieve_relevant_context(user_query, top_k=3)
        
        # Generate response
        response = generate_response(user_query, context)
        
        # Ensure response is valid
        if not response or len(response.strip()) < 5:
            response = f"I found information related to your question about '{user_query}'. Please review the documents for complete details."
        
        return jsonify({
            "message": response.strip(),
            "context_used": len(context) > 10,
            "success": True
        })
    
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        error_msg = str(e)
        return jsonify({
            "message": "I encountered an error processing your question. Please try again.",
            "error": error_msg,
            "success": False
        }), 500

@app.route('/api/tts', methods=['POST'])
def text_to_speech():
    """Convert text to speech"""
    try:
        data = request.json
        text = data.get('text', '')
        
        if not text:
            return jsonify({"error": "No text provided"}), 400
        
        # Generate speech
        audio_file = "temp_audio.mp3"
        tts_engine.save_to_file(text, audio_file)
        tts_engine.runAndWait()
        
        # Read and return audio file
        with open(audio_file, 'rb') as f:
            audio_data = f.read()
        
        os.remove(audio_file)
        
        return audio_data, 200, {'Content-Type': 'audio/mp3'}
    
    except Exception as e:
        print(f"Error in TTS: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/reload-kb', methods=['POST'])
def reload_knowledge_base():
    """Reload knowledge base"""
    try:
        success = initialize_knowledge_base()
        return jsonify({
            "success": success,
            "message": "Knowledge base reloaded",
            "chunks": len(knowledge_base),
            "documents": len(set([m["source"] for m in metadata_store]))
        })
    except Exception as e:
        print(f"Error reloading KB: {e}")
        return jsonify({"error": str(e)}), 500

# ============================================================================
# STARTUP & SHUTDOWN
# ============================================================================

@app.before_request
def before_request():
    """Initialize knowledge base on first request"""
    if len(knowledge_base) == 0 and request.path != '/':
        initialize_knowledge_base()

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🤖 CHATBOT INITIALIZATION")
    print("="*60)
    
    # Initialize knowledge base
    initialize_knowledge_base()
    
    print("\n" + "="*60)
    print("✅ CHATBOT READY!")
    print("="*60)
    print("\n🌐 Starting Flask server...")
    print("📍 Open your browser at: http://localhost:5000")
    print("\n💡 Remember to add PDF files to the 'pdfs' folder!\n")
    
    # Run Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
