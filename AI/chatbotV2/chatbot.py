"""
Main Chatbot Application
Integrates PDF Knowledge Base, Audio I/O, and LLM for conversational AI
"""

from pdf_loader import PDFKnowledgeBase
from audio_handler import AudioHandler
from llm_handler import LLMHandler
import sys


class Chatbot:
    def __init__(self, kb_folder="knowledge_base", use_audio=True):
        """
        Initialize Chatbot
        
        Args:
            kb_folder: Path to knowledge base folder
            use_audio: Enable speech-to-text and text-to-speech
        """
        print("=" * 60)
        print("🤖 INITIALIZING AI CHATBOT")
        print("=" * 60)
        
        # Load PDF Knowledge Base
        print("\n1️⃣  Loading PDF Knowledge Base...")
        self.kb = PDFKnowledgeBase(kb_folder)
        if not self.kb.load_knowledge_base():
            print("❌ Failed to load knowledge base. Please add PDFs to 'knowledge_base' folder.")
            self.kb_loaded = False
        else:
            print("✅ Knowledge base loaded successfully!")
            self.kb_loaded = True
        
        # Initialize Audio Handler
        print("\n2️⃣  Initializing Audio Handler...")
        self.audio = AudioHandler()
        self.use_audio = use_audio
        print("✅ Audio handler ready!")
        
        # Initialize LLM Handler
        print("\n3️⃣  Initializing Language Model...")
        self.llm = LLMHandler()
        if self.llm.use_ollama:
            print("✅ Connected to Ollama (Local LLM)")
        else:
            print("⚠️  Ollama not available. Using template-based responses.")
            print("   (To use Ollama: Install it from https://ollama.ai)")
        
        print("\n" + "=" * 60)
        print("✅ CHATBOT READY!")
        print("=" * 60)
    
    def process_query(self, user_input=None):
        """
        Process user query and generate response
        
        Args:
            user_input: Text query (if None, will try to get from speech)
        
        Returns:
            Response text
        """
        if not self.kb_loaded:
            return "Knowledge base not loaded. Cannot answer questions."
        
        # Get input (text or speech)
        if user_input is None:
            if self.use_audio:
                user_input = self.audio.speech_to_text(use_microphone=True)
            else:
                user_input = input("\n👤 You: ").strip()
        
        if not user_input:
            return None
        
        print(f"\n📝 Query: {user_input}")
        
        # Retrieve relevant documents
        print("🔍 Searching knowledge base...")
        context = self.kb.search(user_input, top_k=3)
        
        if not context:
            response = f"I don't have information about '{user_input}' in my knowledge base."
        else:
            # Show relevance scores
            print("\n📚 Retrieved Documents:")
            for i, doc in enumerate(context, 1):
                print(f"   {i}. {doc['file']} (relevance: {doc['similarity']:.2f})")
            
            # Generate response
            print("\n🤔 Generating response...")
            response = self.llm.generate_response(user_input, context)
        
        return response
    
    def chat_loop(self):
        """Main chat loop - interactive conversation"""
        print("\n" + "=" * 60)
        print("💬 CHAT MODE")
        print("Type 'quit' or 'exit' to end conversation")
        print("Type 'help' for commands")
        print("=" * 60 + "\n")
        
        while True:
            try:
                # Get user input
                print("\n🎤 Say something or type your question:")
                user_input = self.audio.speech_to_text(use_microphone=self.use_audio)
                
                if not user_input:
                    if not self.use_audio:
                        user_input = input("👤 You: ").strip()
                    else:
                        continue
                
                # Check for commands
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print("\n👋 Goodbye! Thank you for chatting.")
                    break
                
                if user_input.lower() == 'help':
                    print("\n📋 Commands:")
                    print("   - 'audio on/off' : Toggle audio")
                    print("   - 'reload' : Reload knowledge base")
                    print("   - 'quit' : Exit chatbot")
                    continue
                
                if user_input.lower() == 'audio off':
                    self.use_audio = False
                    print("🔇 Audio disabled. Type your questions instead.")
                    continue
                
                if user_input.lower() == 'audio on':
                    self.use_audio = True
                    print("🔊 Audio enabled.")
                    continue
                
                # Process query
                response = self.process_query(user_input)
                
                if response:
                    print(f"\n🤖 Bot: {response}\n")
                    
                    # Speak response
                    if self.use_audio:
                        self.audio.text_to_speech(response, play=True)
            
            except KeyboardInterrupt:
                print("\n\n👋 Chatbot interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
                continue
    
    def single_query_mode(self, query):
        """Process a single query and return response"""
        response = self.process_query(query)
        
        if response:
            print(f"\n🤖 Bot: {response}\n")
            
            if self.use_audio:
                self.audio.text_to_speech(response, play=True)
        
        return response
    
    def close(self):
        """Clean up resources"""
        self.audio.close()


def main():
    """Main entry point"""
    print("\n")
    print("╔═══════════════════════════════════════════════════╗")
    print("║     AI CHATBOT WITH PDF KNOWLEDGE BASE            ║")
    print("║     STT + LLM + TTS                               ║")
    print("╚═══════════════════════════════════════════════════╝")
    
    # Check if running in audio mode or text mode
    use_audio = '--no-audio' not in sys.argv
    
    # Initialize chatbot
    bot = Chatbot(kb_folder="knowledge_base", use_audio=use_audio)
    
    # Check if query provided as argument
    if len(sys.argv) > 1 and not sys.argv[1].startswith('--'):
        # Single query mode
        query = " ".join(sys.argv[1:])
        print(f"\n🔄 Processing query: {query}")
        bot.single_query_mode(query)
    else:
        # Interactive chat mode
        bot.chat_loop()
    
    # Cleanup
    bot.close()


if __name__ == "__main__":
    main()
