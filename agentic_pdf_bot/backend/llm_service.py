"""Simple LLM Service"""

import requests
from config import OLLAMA_BASE_URL, LLM_MODEL, MAX_TOKENS, TEMPERATURE
from pdf_loader import pdf_service

class SimpleLLMService:
    def __init__(self):
        """Initialize LLM Service"""
        self.base_url = OLLAMA_BASE_URL
        self.model = LLM_MODEL
        
    def check_ollama_connection(self) -> bool:
        """Check if Ollama is running"""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=2)
            return response.status_code == 200
        except:
            return False
    
    def get_available_models(self) -> list:
        """Get available models"""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=2)
            if response.status_code == 200:
                return [m["name"] for m in response.json().get("models", [])]
        except:
            pass
        return []
    
    def generate_response(self, user_query: str) -> str:
        """Generate response using Ollama with PDF context"""
        
        # Get relevant context from PDFs
        context = pdf_service.search_similar_docs(user_query, k=3)
        
        # Build prompt
        if context:
            prompt = f"""Based on this document context, answer the question:

CONTEXT:
{context}

QUESTION: {user_query}

Answer directly and concisely."""
        else:
            prompt = f"Answer this question: {user_query}"
        
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "temperature": TEMPERATURE,
                    "num_predict": MAX_TOKENS,
                    "stream": False
                },
                timeout=30
            )
            
            if response.status_code == 200:
                return response.json().get("response", "No response")
            else:
                return f"LLM Error: {response.status_code}"
        except Exception as e:
            return f"Connection error: {str(e)}"

# Global instance
llm_service = SimpleLLMService()
