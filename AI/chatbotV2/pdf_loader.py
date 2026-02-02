"""
PDF Knowledge Base Loader
Loads and processes PDF files into embeddings for vector search
"""

import os
from PyPDF2 import PdfReader
import numpy as np
from sentence_transformers import SentenceTransformer


class PDFKnowledgeBase:
    def __init__(self, kb_folder="knowledge_base", model_name="all-MiniLM-L6-v2"):
        """
        Initialize PDF Knowledge Base
        
        Args:
            kb_folder: Path to folder containing PDF files
            model_name: Sentence Transformer model for embeddings
        """
        self.kb_folder = kb_folder
        self.documents = []
        self.embeddings = None
        self.model = SentenceTransformer(model_name)
        
    def extract_text_from_pdf(self, pdf_path):
        """Extract text from a PDF file"""
        try:
            pdf_reader = PdfReader(pdf_path)
            text = ""
            for page_num, page in enumerate(pdf_reader.pages):
                text += f"\n--- Page {page_num + 1} ---\n"
                text += page.extract_text()
            return text
        except Exception as e:
            print(f"Error reading {pdf_path}: {e}")
            return None
    
    def chunk_text(self, text, chunk_size=256, overlap=50):
        """
        Split text into overlapping chunks
        
        Args:
            text: Text to chunk
            chunk_size: Number of characters per chunk
            overlap: Number of overlapping characters
        """
        chunks = []
        start = 0
        
        while start < len(text):
            end = start + chunk_size
            chunks.append(text[start:end])
            start = end - overlap
            
        return chunks
    
    def load_knowledge_base(self):
        """Load all PDFs from knowledge_base folder and create embeddings"""
        if not os.path.exists(self.kb_folder):
            print(f"Knowledge base folder '{self.kb_folder}' not found!")
            return False
        
        pdf_files = [f for f in os.listdir(self.kb_folder) if f.endswith('.pdf')]
        
        if not pdf_files:
            print(f"No PDF files found in '{self.kb_folder}'")
            return False
        
        print(f"Found {len(pdf_files)} PDF files. Processing...")
        
        # Extract and chunk all PDFs
        for pdf_file in pdf_files:
            pdf_path = os.path.join(self.kb_folder, pdf_file)
            print(f"Processing: {pdf_file}")
            
            text = self.extract_text_from_pdf(pdf_path)
            if text:
                chunks = self.chunk_text(text)
                
                for chunk in chunks:
                    if chunk.strip():  # Only add non-empty chunks
                        self.documents.append({
                            'file': pdf_file,
                            'text': chunk
                        })
        
        if not self.documents:
            print("No text extracted from PDFs!")
            return False
        
        print(f"Total chunks created: {len(self.documents)}")
        
        # Generate embeddings for all documents
        print("Generating embeddings... (this may take a minute)")
        texts = [doc['text'] for doc in self.documents]
        self.embeddings = self.model.encode(texts, show_progress_bar=True)
        
        print("Knowledge base loaded successfully!")
        return True
    
    def search(self, query, top_k=3):
        """
        Search for relevant documents
        
        Args:
            query: User query
            top_k: Number of top results to return
        """
        if self.embeddings is None:
            return []
        
        # Encode the query
        query_embedding = self.model.encode(query)
        
        # Calculate similarities (cosine similarity)
        similarities = np.dot(self.embeddings, query_embedding) / (
            np.linalg.norm(self.embeddings, axis=1) * np.linalg.norm(query_embedding) + 1e-8
        )
        
        # Get top k indices
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        
        # Return results
        results = []
        for idx in top_indices:
            results.append({
                'text': self.documents[idx]['text'],
                'file': self.documents[idx]['file'],
                'similarity': float(similarities[idx])
            })
        
        return results
