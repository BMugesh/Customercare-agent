import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def ask_groq(prompt, max_retries=3, timeout=30):
    """
    Ask Groq API with improved error handling and retries
    """
    if not GROQ_API_KEY:
        return "❌ Error: GROQ_API_KEY not found in environment variables"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful customer support assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 1000
    }

    for attempt in range(max_retries):
        try:
            response = requests.post(
                GROQ_API_URL,
                headers=headers,
                json=body,
                timeout=timeout
            )

            if response.status_code == 200:
                result = response.json()
                return result['choices'][0]['message']['content']
            else:
                error_msg = f"API Error {response.status_code}: {response.text}"
                if attempt == max_retries - 1:  # Last attempt
                    return f"❌ {error_msg}"
                print(f"Attempt {attempt + 1} failed: {error_msg}")

        except requests.exceptions.ConnectionError as e:
            error_msg = f"Connection Error: {str(e)}"
            if attempt == max_retries - 1:  # Last attempt
                return f"❌ {error_msg}"
            print(f"Attempt {attempt + 1} failed: {error_msg}")

        except requests.exceptions.Timeout as e:
            error_msg = f"Timeout Error: {str(e)}"
            if attempt == max_retries - 1:  # Last attempt
                return f"❌ {error_msg}"
            print(f"Attempt {attempt + 1} failed: {error_msg}")

        except requests.exceptions.RequestException as e:
            error_msg = f"Request Error: {str(e)}"
            if attempt == max_retries - 1:  # Last attempt
                return f"❌ {error_msg}"
            print(f"Attempt {attempt + 1} failed: {error_msg}")

        except Exception as e:
            error_msg = f"Unexpected Error: {str(e)}"
            if attempt == max_retries - 1:  # Last attempt
                return f"❌ {error_msg}"
            print(f"Attempt {attempt + 1} failed: {error_msg}")

        # Wait before retrying (exponential backoff)
        if attempt < max_retries - 1:
            wait_time = 2 ** attempt  # 1s, 2s, 4s...
            print(f"Retrying in {wait_time} seconds...")
            time.sleep(wait_time)

    return "❌ All retry attempts failed"
