import PyPDF2
import pandas as pd
from bs4 import BeautifulSoup
import requests

def read_pdf(path):
    with open(path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def read_excel(path):
    df = pd.read_excel(path)
    return df.to_string()

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()
