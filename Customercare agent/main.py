import streamlit as st
from document_handler import read_pdf, read_excel, scrape_website
from vector_store import VectorStore
from groq_handler import ask_groq
import os

st.set_page_config(page_title=" Product Support Agent", layout="centered")
st.title(" Customer Support Chatbot")

# Load docs
if 'vs' not in st.session_state:
    vs = VectorStore()
    pdf_text = read_pdf("docs/product_faq.pdf")
    excel_text = read_excel("docs/product_specs.xlsx")
    website_text = open("docs/your_website_text.txt", "r").read()

    all_text = [pdf_text, excel_text, website_text]
    chunks = [t[i:i+500] for t in all_text for i in range(0, len(t), 500)]
    vs.add_texts(chunks)
    st.session_state.vs = vs

query = st.text_input("Ask about the product:")
if query:
    context = st.session_state.vs.search(query)
    prompt = f"""Answer the following question using the context below.
    
Context:
{context}

Question:
{query}
"""
    response = ask_groq(prompt)
    st.markdown(f"**🤖 Bot:** {response}")
