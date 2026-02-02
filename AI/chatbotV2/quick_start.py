"""
Quick Start Script
Demonstrates how to use the chatbot programmatically
"""

from chatbot import Chatbot


def main():
    """Quick start example"""
    
    print("\n" + "=" * 60)
    print("🚀 QUICK START - AI CHATBOT")
    print("=" * 60)
    
    # Initialize chatbot
    print("\nInitializing chatbot...")
    bot = Chatbot(kb_folder="knowledge_base", use_audio=False)
    
    if not bot.kb_loaded:
        print("⚠️  No PDFs found in knowledge_base/ folder")
        print("Please add some PDF files first!")
        return
    
    # Example queries
    example_queries = [
        "What are the main topics covered?",
        "Tell me about the first document",
        "What key information is available?",
    ]
    
    print("\n" + "=" * 60)
    print("📝 RUNNING EXAMPLE QUERIES")
    print("=" * 60)
    
    for i, query in enumerate(example_queries, 1):
        print(f"\n\nQuery {i}/{len(example_queries)}:")
        print(f"❓ Question: {query}")
        print("-" * 60)
        
        response = bot.process_query(query)
        
        if response:
            print(f"\n✅ Answer:\n{response}")
        else:
            print("No response generated")
    
    # Interactive mode
    print("\n\n" + "=" * 60)
    print("💬 INTERACTIVE MODE")
    print("=" * 60)
    print("Now entering interactive chat mode...")
    print("Type 'quit' to exit\n")
    
    while True:
        try:
            query = input("\n👤 Your question: ").strip()
            
            if not query:
                continue
            
            if query.lower() in ['quit', 'exit']:
                break
            
            response = bot.process_query(query)
            if response:
                print(f"\n🤖 Answer:\n{response}")
        
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
    
    # Cleanup
    bot.close()


if __name__ == "__main__":
    main()
