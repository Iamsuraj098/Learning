"""
Test/Demo Script
This script demonstrates the chatbot components independently
"""

from pdf_loader import PDFKnowledgeBase
from audio_handler import AudioHandler
from llm_handler import LLMHandler


def test_pdf_loader():
    """Test PDF loading and search"""
    print("\n" + "=" * 60)
    print("TEST 1: PDF LOADER")
    print("=" * 60)
    
    kb = PDFKnowledgeBase(kb_folder="knowledge_base")
    
    if not kb.load_knowledge_base():
        print("⚠️  No PDFs found to test")
        return False
    
    # Test search
    print("\nTesting search functionality...")
    query = "What is the main topic?"
    results = kb.search(query, top_k=2)
    
    print(f"\nSearch results for: '{query}'")
    for i, result in enumerate(results, 1):
        print(f"\n{i}. File: {result['file']}")
        print(f"   Similarity: {result['similarity']:.3f}")
        print(f"   Text preview: {result['text'][:100]}...")
    
    return True


def test_audio_handler():
    """Test audio components"""
    print("\n" + "=" * 60)
    print("TEST 2: AUDIO HANDLER")
    print("=" * 60)
    
    audio = AudioHandler()
    
    print("\n1. Testing Text-to-Speech...")
    test_text = "Hello! This is a test of the text to speech system."
    print(f"Speaking: '{test_text}'")
    audio.text_to_speech(test_text, play=True)
    print("✓ Text-to-speech working!")
    
    print("\n2. Testing Speech-to-Text...")
    print("Skipping audio test (requires microphone)")
    print("To test: Uncomment speech_to_text() call")
    
    audio.close()


def test_llm_handler():
    """Test LLM response generation"""
    print("\n" + "=" * 60)
    print("TEST 3: LLM HANDLER")
    print("=" * 60)
    
    llm = LLMHandler()
    
    # Mock context
    context = [
        {'text': 'Machine learning is a branch of artificial intelligence that enables systems to learn and improve from experience.'},
        {'text': 'Deep learning uses neural networks with multiple layers to process data.'},
    ]
    
    query = "What is machine learning?"
    
    print(f"\nQuery: {query}")
    print(f"Context provided: {len(context)} documents")
    print("\nGenerating response...")
    
    response = llm.generate_response(query, context)
    print(f"\nResponse:\n{response}")


def test_full_pipeline():
    """Test complete pipeline"""
    print("\n" + "=" * 60)
    print("TEST 4: FULL PIPELINE")
    print("=" * 60)
    
    print("\nInitializing components...")
    
    kb = PDFKnowledgeBase(kb_folder="knowledge_base")
    kb.load_knowledge_base()
    
    llm = LLMHandler()
    
    if kb.documents:
        query = "Tell me about the documents"
        print(f"\nQuery: {query}")
        
        # Retrieve
        context = kb.search(query, top_k=2)
        print(f"Retrieved {len(context)} documents")
        
        # Generate
        response = llm.generate_response(query, context)
        print(f"\nResponse:\n{response}")
    else:
        print("⚠️  No documents to test with")


def main():
    """Run all tests"""
    print("\n╔═══════════════════════════════════════════════════╗")
    print("║     CHATBOT COMPONENT TESTS                       ║")
    print("╚═══════════════════════════════════════════════════╝")
    
    print("\nAvailable tests:")
    print("1. PDF Loader")
    print("2. Audio Handler")
    print("3. LLM Handler")
    print("4. Full Pipeline")
    print("5. All Tests")
    
    choice = input("\nSelect test (1-5): ").strip()
    
    try:
        if choice == "1":
            test_pdf_loader()
        elif choice == "2":
            test_audio_handler()
        elif choice == "3":
            test_llm_handler()
        elif choice == "4":
            test_full_pipeline()
        elif choice == "5":
            test_pdf_loader()
            test_audio_handler()
            test_llm_handler()
            test_full_pipeline()
        else:
            print("Invalid choice")
    
    except Exception as e:
        print(f"\n❌ Error during test: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n" + "=" * 60)
    print("✓ Tests completed")
    print("=" * 60)


if __name__ == "__main__":
    main()
