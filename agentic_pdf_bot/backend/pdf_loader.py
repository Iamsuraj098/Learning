"""Simple PDF Loader using PyPDF"""
from pathlib import Path
from pypdf import PdfReader
from config import PDF_UPLOAD_FOLDER

class SimplePDFLoaderService:
    def __init__(self):
        self.pdf_folder = PDF_UPLOAD_FOLDER
        self.documents = []
        
    def load_pdfs(self):
        pdf_files = list(Path(self.pdf_folder).glob("*.pdf"))
        if not pdf_files:
            print("No PDFs found")
            return []
        
        self.documents = []
        for pdf_file in pdf_files:
            print(f"Loading: {pdf_file.name}")
            try:
                reader = PdfReader(str(pdf_file))
                text = ""
                for i, page in enumerate(reader.pages):
                    text += f"\n--- Page {i+1} ---\n" + page.extract_text()
                
                self.documents.append({
                    "filename": pdf_file.name,
                    "text": text,
                    "pages": len(reader.pages)
                })
                print(f"Loaded {len(reader.pages)} pages")
            except Exception as e:
                print(f"Error: {e}")
        return self.documents
    
    def search_similar_docs(self, query, k=3):
        if not self.documents:
            return ""
        
        results = []
        query_lower = query.lower()
        for doc in self.documents:
            for line in doc["text"].split("\n"):
                if query_lower in line.lower():
                    results.append(line.strip())
        
        return "\n".join(results[:k*50])

pdf_service = SimplePDFLoaderService()
