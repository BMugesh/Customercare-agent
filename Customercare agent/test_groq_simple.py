#!/usr/bin/env python3

import os
import sys
from dotenv import load_dotenv
from groq_handler import ask_groq

def main():
    print("Testing Groq API connection...")
    
    # Load environment variables
    load_dotenv()
    
    # Check if API key is loaded
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("❌ GROQ_API_KEY not found in .env file")
        return False
    
    print(f"✅ API Key loaded: {api_key[:10]}...")
    
    # Test simple query
    try:
        print("\n🔄 Testing simple query...")
        response = ask_groq("Hello, can you respond with just 'Hello back!'?")
        print(f"✅ Response received: {response}")
        return True
        
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        print(f"Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
