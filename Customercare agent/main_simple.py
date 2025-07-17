#!/usr/bin/env python3

import os
import sys
from dotenv import load_dotenv
from groq_handler import ask_groq

# Simple fallback vector store
class SimpleVectorStore:
    def __init__(self):
        self.texts = []

    def add_texts(self, text_chunks):
        self.texts.extend(text_chunks)

    def search(self, query, k=3):
        """Simple keyword-based search"""
        import re
        query_words = set(re.findall(r'\w+', query.lower()))
        
        scores = []
        for i, text in enumerate(self.texts):
            text_words = set(re.findall(r'\w+', text.lower()))
            overlap = len(query_words.intersection(text_words))
            scores.append((overlap, i))
        
        scores.sort(reverse=True)
        top_indices = [idx for _, idx in scores[:k]]
        
        return [self.texts[i] for i in top_indices if i < len(self.texts)]

def read_text_file(path):
    """Simple text file reader"""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading {path}: {e}"

def main():
    print("🚀 Starting Customer Support Chatbot (Simple Version)")
    
    # Load environment variables
    load_dotenv()
    
    # Initialize vector store
    vs = SimpleVectorStore()
    
    # Load documents (simplified)
    print("📚 Loading documents...")
    try:
        # Try to read the text file
        website_text = read_text_file("docs/your_website_text.txt")
        
        # Create chunks
        chunks = [website_text[i:i+500] for i in range(0, len(website_text), 500)]
        vs.add_texts(chunks)
        print(f"✅ Loaded {len(chunks)} text chunks")
        
    except Exception as e:
        print(f"⚠️ Error loading documents: {e}")
        # Add some default content
        default_content = [
            "Welcome to our customer support. We offer various products and services.",
            "For technical support, please contact our technical team.",
            "Our business hours are Monday to Friday, 9 AM to 5 PM.",
            "We provide warranty support for all our products.",
            "For billing inquiries, please contact our billing department."
        ]
        vs.add_texts(default_content)
        print("✅ Loaded default content")
    
    # Interactive chat loop
    print("\n💬 Chat started! Type 'quit' to exit.")
    print("=" * 50)
    
    while True:
        try:
            query = input("\n🤔 You: ").strip()
            
            if query.lower() in ['quit', 'exit', 'bye']:
                print("👋 Goodbye!")
                break
                
            if not query:
                continue
            
            # Search for relevant context
            context = vs.search(query)
            context_text = "\n".join(context)
            
            # Create prompt
            prompt = f"""Answer the following question using the context below.
            
Context:
{context_text}

Question:
{query}

Please provide a helpful and concise answer based on the context provided."""

            print("\n🤖 Bot: ", end="", flush=True)
            
            # Get response from Groq
            response = ask_groq(prompt)
            print(response)
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()
