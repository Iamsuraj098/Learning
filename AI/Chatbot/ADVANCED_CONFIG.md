# Configuration for Advanced Users

## Environment Variables
Create a `.env` file in the root directory:

```
FLASK_ENV=development
FLASK_DEBUG=True
PORT=5000
HOST=0.0.0.0
MAX_CONTEXT_CHUNKS=5
CHUNK_SIZE=500
CHUNK_OVERLAP=100
EMBEDDING_MODEL=all-MiniLM-L6-v2
LLM_MODEL=distilgpt2
TTS_RATE=150
LLM_MAX_LENGTH=300
LLM_TEMPERATURE=0.7
```

## Advanced Configuration in app.py

### 1. Use Different Embedding Model
Better quality (slower):
```python
embedding_model = SentenceTransformer('all-mpnet-base-v2')
```

Faster (lower quality):
```python
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
```

### 2. Use Different LLM
For better responses (requires more memory):
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
model_name = "gpt2"  # or "EleutherAI/gpt-neo-125M"
```

### 3. Adjust Context Retrieval
In `retrieve_relevant_context()` function:
```python
top_k=5  # Retrieve more context for better answers
```

### 4. Change Chunk Size
In `chunk_text()` function:
```python
chunk_size=750  # Larger = fewer chunks, potentially better context
overlap=150     # More overlap = more redundancy
```

### 5. TTS Voice Settings
In app.py initialization:
```python
tts_engine.setProperty('rate', 100)    # 50-300 (words per minute)
tts_engine.setProperty('volume', 0.9)  # 0.0-1.0
```

## Performance Optimization

### For CPU-Limited Devices:
1. Use smaller embedding model
2. Use smaller LLM (distilgpt2 is already small)
3. Reduce chunk size
4. Limit PDFs to 5 or less

### For Memory-Limited Systems:
```python
import torch
torch.cuda.empty_cache()  # Add to app.py
```

### For Faster Responses:
1. Use quantized models
2. Enable GPU if available
3. Reduce number of context chunks

## Running on GPU

If you have CUDA-capable GPU:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

Then in app.py, change:
```python
device = 0  # Use GPU
```

## Docker Deployment

Create `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["python", "app.py"]
```

Build and run:
```bash
docker build -t chatbot .
docker run -p 5000:5000 -v $(pwd)/pdfs:/app/pdfs chatbot
```

## MongoDB Integration (Optional)

Store chat history:

```python
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['chatbot']
chats = db['conversations']

# Save conversation
chats.insert_one({
    "user_query": query,
    "bot_response": response,
    "timestamp": datetime.now()
})
```

## Monitoring & Logging

Add to app.py:

```python
import logging

logging.basicConfig(
    filename='chatbot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@app.after_request
def log_request(response):
    logging.info(f'{request.method} {request.path} - {response.status_code}')
    return response
```

## Production Deployment

### Using Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Using Nginx as Reverse Proxy:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---

For more info, check the main README.md
