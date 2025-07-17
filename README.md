# 🤖 Customer Care Agent

An intelligent customer support chatbot powered by Groq's LLaMA models, designed to provide instant, context-aware responses to customer inquiries using your product documentation.

## 🌟 Features

- **AI-Powered Responses**: Uses Groq's fast LLaMA 3 models for intelligent customer support
- **Document Integration**: Automatically processes PDFs, Excel files, and text documents
- **Context-Aware Search**: Finds relevant information from your knowledge base
- **Multiple Interfaces**: Both Streamlit web UI and command-line interface
- **Robust Error Handling**: Built-in retry mechanisms and connection fallbacks
- **Easy Setup**: Simple configuration with environment variables

## 📁 Project Structure

```
Customercare agent/
├── docs/                          # Knowledge base documents
│   ├── product_faq.pdf           # Product FAQ document
│   ├── product_specs.xlsx        # Product specifications
│   └── your_website_text.txt     # Website content
├── main.py                       # Main Streamlit application
├── main_simple.py               # Command-line interface version
├── groq_handler.py              # Groq API integration with retry logic
├── document_handler.py          # Document processing utilities
├── vector_store.py              # Simple keyword-based search engine
├── streamlit_test.py            # Streamlit connection test
├── test_*.py                    # Various test scripts
├── .env                         # Environment variables (API keys)
└── README.md                    # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Groq API key (get one at [console.groq.com](https://console.groq.com))

### Installation

1. **Clone or download this repository**

2. **Install required packages:**
   ```bash
   pip install requests python-dotenv streamlit PyPDF2 pandas beautifulsoup4 openpyxl
   ```

3. **Set up your API key:**
   - Copy your Groq API key
   - Make sure it's in the `.env` file:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Add your documents:**
   - Place your PDF files in the `docs/` folder
   - Update Excel files with your product specifications
   - Modify `your_website_text.txt` with your website content

### Running the Application

#### Option 1: Streamlit Web Interface
```bash
streamlit run main.py
```
Then open your browser to `http://localhost:8501`

#### Option 2: Command Line Interface
```bash
python main_simple.py
```

#### Option 3: Test Connection
```bash
python test_groq_simple.py
```

## 🔧 Configuration

### Environment Variables

Create or update the `.env` file with your API keys:

```env
GROQ_API_KEY=your_groq_api_key_here
SERP_API_KEY=your_serp_api_key_here (optional)
RAPIDAPI_KEY=your_rapidapi_key_here (optional)
EXCHANGE_API_KEY=your_exchange_api_key_here (optional)
```

### Document Setup

1. **PDF Documents**: Place FAQ and manual PDFs in the `docs/` folder
2. **Excel Files**: Add product specifications and data sheets
3. **Text Files**: Include website content and additional documentation

## 🛠️ Core Components

### Groq Handler (`groq_handler.py`)
- Manages API communication with Groq
- Implements retry logic with exponential backoff
- Handles various error scenarios (connection, timeout, API errors)

### Document Handler (`document_handler.py`)
- Processes PDF files using PyPDF2
- Reads Excel files with pandas
- Web scraping capabilities with BeautifulSoup

### Vector Store (`vector_store.py`)
- Simple keyword-based search engine
- Lightweight alternative to complex vector databases
- Efficient text chunking and retrieval

### Main Application (`main.py`)
- Streamlit web interface
- Session state management
- Real-time chat interface

## 🧪 Testing

The project includes several test scripts:

- `test_groq_simple.py` - Test Groq API connection
- `test_connection.py` - Comprehensive network connectivity test
- `streamlit_test.py` - Streamlit-specific API test

Run any test:
```bash
python test_groq_simple.py
```

## 🔍 Troubleshooting

### Common Issues

1. **Connection Errors**
   - Check your internet connection
   - Verify your Groq API key is correct
   - Run `python test_connection.py` for detailed diagnostics

2. **Missing Dependencies**
   ```bash
   pip install requests python-dotenv streamlit PyPDF2 pandas beautifulsoup4 openpyxl
   ```

3. **Document Loading Issues**
   - Ensure documents are in the `docs/` folder
   - Check file permissions
   - Verify file formats (PDF, XLSX, TXT)

4. **API Rate Limits**
   - The system includes automatic retry with backoff
   - Consider upgrading your Groq plan for higher limits

### Debug Mode

For detailed error information, check the console output when running the applications.

## 📝 Customization

### Adding New Document Types
Extend `document_handler.py` to support additional file formats.

### Improving Search
Replace the simple keyword search in `vector_store.py` with more advanced methods like:
- TF-IDF scoring
- Semantic embeddings
- Full-text search engines

### UI Customization
Modify `main.py` to change the Streamlit interface:
- Add custom CSS
- Include additional input fields
- Implement conversation history

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source. Feel free to use and modify according to your needs.

## 🆘 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Run the test scripts to diagnose problems
3. Review the console output for error messages
4. Ensure all dependencies are properly installed

## 🔮 Future Enhancements

- [ ] Advanced vector search with embeddings
- [ ] Multi-language support
- [ ] Conversation history and context
- [ ] Admin dashboard for document management
- [ ] Integration with popular helpdesk systems
- [ ] Voice interface support
- [ ] Analytics and reporting features

---

**Built with ❤️ using Groq's lightning-fast LLaMA models**
