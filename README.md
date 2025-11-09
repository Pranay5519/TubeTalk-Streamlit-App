<div align="center">

# 🎨 TubeTalk.ai - Streamlit UI

**Interactive Frontend for TubeTalk.ai API**

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)

[Features](#-features) •
[Installation](#️-installation) •
[Usage](#-usage) •
[Configuration](#-configuration)

</div>

---

## 📋 Overview

TubeTalk.ai Streamlit UI is a beautiful, user-friendly frontend application built on top of the TubeTalk.ai FastAPI backend. It provides an intuitive interface for:

- 💬 **AI Chatbot** - Interactive conversational AI with context awareness
- 📝 **Smart Summarization** - Generate concise summaries from long content
- 🎯 **Quiz Generation** - Create custom quizzes from any content
- 🏷️ **Topic Extraction** - Automatically identify key topics and concepts

Built with Streamlit for rapid prototyping and seamless user experience.

---

## 🏗️ Project Structure
```
tubetalk.ai_api/
│
├── .gitignore                  # Git ignore configuration
├── folder_structure.txt        # Project structure documentation
├── get_folder_structure.py     # Script to generate folder structure
├── test.py                     # Testing utilities
├── __init__.py
│
└── app/                        # Main Streamlit application
    ├── Home.py                 # Main entry point & home page
    ├── __init__.py
    │
    ├── sections/               # UI sections for each feature
    │   ├── chatbot_ui.py       # Chatbot interface
    │   ├── quiz_ui.py          # Quiz generation interface
    │   ├── summary_ui.py       # Summary generation interface
    │   └── topics_ui.py        # Topic extraction interface
    │
    └── utils/                  # Utility modules
        ├── api_client.py       # API communication layer
        ├── config.py           # Configuration management
        └── sessioin_manager.py # Session state management
```

---

## ⚙️ Installation

### Prerequisites

- Python 3.9+
- TubeTalk.ai FastAPI backend running (see [backend repository](https://github.com/<your-username>/tubetalk-ai-api))
- pip package manager

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/tubetalk-ai-streamlit.git
cd tubetalk-ai-streamlit
```

### 2. Create a Virtual Environment

**Mac/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Endpoint

Update the API endpoint in `app/utils/config.py`:
```python
API_BASE_URL = "http://localhost:8000"  # Your FastAPI backend URL
```

### 5. Run the Application
```bash
streamlit run app/Home.py
```

### 6. Access the Application

The app will automatically open in your browser at:
- **Local URL:** [http://localhost:8501](http://localhost:8501)

---

## 🚀 Usage

### 🏠 Home Page

The landing page provides navigation to all features and an overview of the application.

### 💬 Chatbot Interface

1. Navigate to the **Chatbot** section
2. Enter your query in the input field
3. Receive AI-powered responses with context awareness
4. Continue the conversation with maintained context

**Features:**
- Session-based conversations
- Context retention across messages
- Real-time streaming responses
- Chat history management

### 📝 Summary Generator

1. Go to the **Summary** section
2. Input or paste your content
3. Select summary length (short/medium/long)
4. Click "Generate Summary"
5. View and copy the generated summary

**Supported Inputs:**
- Plain text
- URLs (fetches content automatically)
- Video transcripts
- Articles and documents

### 🎯 Quiz Generator

1. Navigate to the **Quiz** section
2. Provide source content or topic
3. Configure quiz settings:
   - Number of questions
   - Difficulty level
   - Question types (MCQ, True/False, etc.)
4. Generate and review the quiz
5. Export quiz as JSON or PDF

**Features:**
- Multiple question formats
- Adjustable difficulty levels
- Answer key generation
- Quiz history tracking

### 🏷️ Topic Extractor

1. Visit the **Topics** section
2. Input your content
3. Set the number of topics to extract
4. View extracted topics with relevance scores
5. Export topics as keywords or tags

**Use Cases:**
- Content categorization
- SEO keyword extraction
- Document indexing
- Research topic identification

---

## 🔧 Configuration

### API Client (`app/utils/api_client.py`)

Handles all communication with the FastAPI backend:
```python
class APIClient:
    """
    Manages HTTP requests to TubeTalk.ai API
    - GET/POST/DELETE methods
    - Error handling
    - Response parsing
    """
```

### Session Manager (`app/utils/sessioin_manager.py`)

Manages Streamlit session state:
```python
class SessionManager:
    """
    Handles session state management
    - User sessions
    - Chat history
    - Thread IDs
    - Cache management
    """
```

### Config (`app/utils/config.py`)

Central configuration file:
```python
# API Configuration
API_BASE_URL = "http://localhost:8000"
API_TIMEOUT = 30

# UI Configuration
PAGE_TITLE = "TubeTalk.ai"
PAGE_ICON = "🚀"
LAYOUT = "wide"

# Feature Flags
ENABLE_CACHING = True
DEBUG_MODE = False
```

---

## 🎨 Features

### 🖥️ User Interface

- **Responsive Design** - Works seamlessly on desktop and mobile
- **Dark/Light Mode** - Theme customization
- **Intuitive Navigation** - Easy access to all features
- **Real-time Updates** - Live feedback and status indicators

### 🔄 API Integration

- **RESTful Communication** - Clean API client architecture
- **Error Handling** - Graceful error management and user feedback
- **Request Caching** - Optimized performance with smart caching
- **Session Management** - Persistent user sessions

### 📊 Advanced Functionality

- **Export Options** - Download results in multiple formats
- **History Tracking** - Access previous queries and results
- **Batch Processing** - Handle multiple requests efficiently
- **Customization** - Adjustable parameters for all features

---

## 🛠️ Development

### Running Tests
```bash
python test.py
```

### Generate Folder Structure
```bash
python get_folder_structure.py
```

This will update `folder_structure.txt` with the current project structure.

### Adding New Features

1. Create a new UI module in `app/sections/`
2. Add API endpoints in the backend
3. Update `api_client.py` with new API methods
4. Add navigation in `Home.py`
5. Update documentation

---

## 📦 Dependencies
```txt
streamlit>=1.28.0
requests>=2.31.0
python-dotenv>=1.0.0
pandas>=2.0.0
plotly>=5.17.0
```

Install all dependencies:
```bash
pip install -r requirements.txt
```

---

## 🐛 Troubleshooting

### Connection Issues

**Problem:** Cannot connect to API
**Solution:** 
- Ensure FastAPI backend is running
- Check `API_BASE_URL` in `config.py`
- Verify no firewall blocking the connection

### Session State Issues

**Problem:** Session data not persisting
**Solution:**
- Clear browser cache
- Restart Streamlit app
- Check `sessioin_manager.py` configuration

### Import Errors

**Problem:** Module import failures
**Solution:**
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

---

## 🚀 Deployment

### Deploy to Streamlit Cloud

1. Push your code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Set environment variables:
   - `API_BASE_URL`
   - Any API keys or secrets
5. Deploy!

### Deploy with Docker
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ ./app/

EXPOSE 8501

CMD ["streamlit", "run", "app/Home.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Build and run:
```bash
docker build -t tubetalk-streamlit .
docker run -p 8501:8501 tubetalk-streamlit
```

---

## 📚 Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [TubeTalk.ai API Documentation](https://github.com/<your-username>/tubetalk-ai-api)
- [Python Requests Library](https://requests.readthedocs.io)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Guidelines

- Follow PEP 8 style guide
- Add docstrings to all functions
- Update documentation for new features
- Test thoroughly before submitting PR

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [TubeTalk.ai FastAPI Backend](https://github.com/<your-username>/tubetalk-ai-api)
- Icons from [Streamlit Emoji Shortcodes](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/)

---

## 📬 Contact

**Pranay**  
Student AI Engineer | Machine Learning Enthusiast

[![GitHub](https://img.shields.io/badge/GitHub-@pranay5519-181717?style=for-the-badge&logo=github)](https://github.com/pranay5519)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/pranay)

---

## 🗺️ Roadmap

- [ ] Add user authentication
- [ ] Implement result export (PDF, CSV)
- [ ] Add data visualization for topics
- [ ] Multi-language support
- [ ] Voice input for chatbot
- [ ] Mobile app version
- [ ] Offline mode support
- [ ] Advanced analytics dashboard

---

<div align="center">

Made with ❤️ and ☕ by [Pranay](https://github.com/pranay5519)

⭐ Star this repo if you find it useful!

**[Backend Repository](https://github.com/<your-username>/tubetalk-ai-api)** | **[Report Bug](https://github.com/<your-username>/tubetalk-ai-streamlit/issues)** | **[Request Feature](https://github.com/<your-username>/tubetalk-ai-streamlit/issues)**

</div>