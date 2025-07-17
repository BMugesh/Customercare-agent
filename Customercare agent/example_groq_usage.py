import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.environ.get("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set")

client = Groq(api_key=api_key)