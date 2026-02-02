"""
LLM Handler for generating AI responses
Uses Ollama for local LLM inference (free and offline)
Falls back to simple template-based responses if Ollama is not available
"""

import requests
import json


class LLMHandler:
    def __init__(self, model="mistral", ollama_url="http://localhost:11434"):
        """
        Initialize LLM Handler
        
        Args:
            model: Model name (mistral, llama2, etc.)
            ollama_url: URL of Ollama service
        """
        self.model = model
        self.ollama_url = ollama_url
        self.use_ollama = self._check_ollama_available()
    
    def _check_ollama_available(self):
        """Check if Ollama is available and running"""
        try:
            response = requests.get(f"{self.ollama_url}/api/tags", timeout=2)
            return response.status_code == 200
        except:
            return False
    
    def generate_response(self, query, context):
        """
        Generate response based on query and context
        
        Args:
            query: User question
            context: Retrieved context from knowledge base
        
        Returns:
            Generated response text
        """
        if self.use_ollama:
            return self._generate_with_ollama(query, context)
        else:
            return self._generate_template_based(query, context)
    
    def _generate_with_ollama(self, query, context):
        """Generate response using Ollama"""
        try:
            # Build prompt
            system_prompt = """You are a helpful AI assistant with knowledge of the provided documents. 
Answer questions based on the context provided. Be conversational and helpful.
If the answer is not in the context, acknowledge this politely."""
            
            context_text = "\n".join([f"- {doc['text'][:200]}" for doc in context])
            
            prompt = f"""System: {system_prompt}

Context from documents:
{context_text}

User Question: {query}

Please provide a helpful and conversational answer based on the context above."""
            
            # Call Ollama API
            response = requests.post(
                f"{self.ollama_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                    "temperature": 0.7,
                },
                timeout=60
            )
            
            if response.status_code == 200:
                result = response.json()
                return result.get('response', 'Unable to generate response')
            else:
                return self._generate_template_based(query, context)
        
        except Exception as e:
            print(f"Ollama error: {e}")
            return self._generate_template_based(query, context)
    
    def _generate_template_based(self, query, context):
        """
        Fallback: Generate response using template-based approach
        This works without Ollama for demo purposes
        """
        if not context:
            return f"I don't have information about '{query}' in my knowledge base. Please ask about topics covered in my documents."
        
        # Extract key information from context
        context_summary = " ".join([doc['text'][:100] for doc in context])
        
        # Build conversational response
        response = f"""Based on the information in my knowledge base:

{context_summary}...

Regarding your question about '{query}': This is covered in my documents. The key points are reflected in the context above. 

Is there anything specific about this topic you'd like me to clarify?"""
        
        return response
