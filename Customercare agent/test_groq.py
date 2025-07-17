import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

try:
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    print("✅ Groq client initialized successfully!")
    
    # Test with a simple completion
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": "Hello!"}],
        model="llama3-8b-8192"
    )
    print("✅ API connection working!")
    
except Exception as e:
    print(f"❌ Error: {e}")