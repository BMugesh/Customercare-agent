import requests
import socket
import ssl
import os
from dotenv import load_dotenv

load_dotenv()

def test_dns_resolution():
    try:
        ip = socket.gethostbyname('api.groq.com')
        print(f"✅ DNS Resolution successful: api.groq.com -> {ip}")
        return True
    except socket.gaierror as e:
        print(f"❌ DNS Resolution failed: {e}")
        return False

def test_ssl_connection():
    try:
        context = ssl.create_default_context()
        with socket.create_connection(('api.groq.com', 443), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname='api.groq.com') as ssock:
                print(f"✅ SSL Connection successful")
                return True
    except Exception as e:
        print(f"❌ SSL Connection failed: {e}")
        return False

def test_http_request():
    try:
        response = requests.get('https://api.groq.com', timeout=10)
        print(f"✅ HTTP Request successful: Status {response.status_code}")
        return True
    except requests.exceptions.ConnectionError as e:
        print(f"❌ HTTP Request failed (ConnectionError): {e}")
        return False
    except Exception as e:
        print(f"❌ HTTP Request failed: {e}")
        return False

def test_groq_api():
    try:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            print("❌ GROQ_API_KEY not found in environment")
            return False

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        body = {
            "model": "llama3-8b-8192",
            "messages": [
                {"role": "user", "content": "Hello, this is a test"}
            ],
            "max_tokens": 10
        }

        response = requests.post('https://api.groq.com/openai/v1/chat/completions',
                               headers=headers,
                               json=body,
                               timeout=30)
        print(f"✅ Groq API endpoint reachable: Status {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"✅ API Response: {result.get('choices', [{}])[0].get('message', {}).get('content', 'No content')}")
        else:
            print(f"❌ API Error: {response.text}")
        return True
    except requests.exceptions.ConnectionError as e:
        print(f"❌ Groq API endpoint failed (ConnectionError): {e}")
        return False
    except Exception as e:
        print(f"❌ Groq API endpoint failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing network connectivity to Groq API...")
    print("=" * 50)

    test_dns_resolution()
    test_ssl_connection()
    test_http_request()
    test_groq_api()
