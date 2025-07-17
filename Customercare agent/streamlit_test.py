import streamlit as st
import os
from dotenv import load_dotenv
from groq_handler import ask_groq

# Load environment variables
load_dotenv()

st.set_page_config(page_title="Groq API Test", layout="centered")
st.title("🤖 Groq API Connection Test")

# Test API key
api_key = os.getenv("GROQ_API_KEY")
if api_key:
    st.success(f"✅ API Key loaded: {api_key[:10]}...")
else:
    st.error("❌ GROQ_API_KEY not found in environment")
    st.stop()

# Simple test
st.subheader("Simple API Test")
if st.button("Test Connection"):
    with st.spinner("Testing connection..."):
        try:
            response = ask_groq("Say 'Hello from Streamlit!'")
            st.success(f"✅ Response: {response}")
        except Exception as e:
            st.error(f"❌ Error: {e}")

# Interactive chat
st.subheader("Interactive Chat")
query = st.text_input("Ask something:")
if query:
    with st.spinner("Getting response..."):
        try:
            response = ask_groq(query)
            st.markdown(f"**🤖 Bot:** {response}")
        except Exception as e:
            st.error(f"❌ Error: {e}")
