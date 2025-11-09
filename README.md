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

Built with Streamlit for rapid prototyping and seamless user experience, featuring custom CSS styling for an enhanced visual experience.

---

## 🏗️ Project Structure
```
tubetalk.ai_api/
│
├── .gitignore                  # Git ignore configuration
├── folder_structure.txt        # Project structure documentation
├── get_folder_structure.py     # Script to generate folder structure
├── how_to_run.txt             # Quick start guide
├── README.md                   # This file
├── test.py                     # Testing utilities
├── test_notebook.ipynb         # Jupyter notebook for testing
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
    ├── styles/                 # Custom CSS styling
    │   ├── chatbot.css         # Chatbot page styles
    │   ├── home.css            # Home page styles
    │   ├── quiz.css            # Quiz page styles
    │   ├── summary.css         # Summary page styles
    │   └── topic.css           # Topic page styles
    │
    └── utils/                  # Utility modules
        ├── api_client.py       # API communication layer
        ├── config.py           # Configuration management
        └── utility_functions.py # Helper functions
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

### 4. Configure Environment Variables

Create a `.env` file in the root directory:
```env
# API Configuration
API_BASE_URL=http://localhost:8000
API_TIMEOUT=30

# Application Settings
DEBUG_MODE=False
ENABLE_CACHING=True

# Optional: API Keys
OPENAI_API_KEY=your_api_key_here
```

### 5. Quick Start

For detailed instructions, see `how_to_run.txt`:
```bash
streamlit run app/Home.py
```

### 6. Access the Application

The app will automatically open in your browser at:
- **Local URL:** [http://localhost:8501](http://localhost:8501)
- **Network URL:** Your network IP on port 8501

---

## 🚀 Usage

### 🏠 Home Page

The landing page provides navigation to all features and an overview of the application with custom styling for a modern look.

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
- Custom CSS styling for chat bubbles

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
- Interactive UI with custom styling

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

### Utility Functions (`app/utils/utility_functions.py`)

Common helper functions:
```python
# String formatting
# Date/time utilities
# File handling
# Data validation
# Session helpers
```

---

## 🎨 Styling

### Custom CSS

Each section has dedicated CSS files in `app/styles/`:

- **`home.css`** - Landing page styling, hero sections, cards
- **`chatbot.css`** - Chat bubbles, message containers, input styling
- **`summary.css`** - Summary cards, content display, buttons
- **`quiz.css`** - Question cards, answer options, results display
- **`topic.css`** - Topic tags, keyword clouds, visualization

### Loading Custom Styles
```python
def load_css(file_name):
    """Load CSS file into Streamlit app"""
    with open(f"app/styles/{file_name}") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
```

### Customizing Themes

Modify CSS files to match your brand:
```css
/* app/styles/home.css */
:root {
    --primary-color: #FF4B4B;
    --secondary-color: #0068C9;
    --background-color: #FFFFFF;
    --text-color: #262730;
}
```

---

## 🎨 Features

### 🖥️ User Interface

- **Custom Styling** - Polished UI with dedicated CSS for each section
- **Responsive Design** - Works seamlessly on desktop and mobile
- **Dark/Light Mode** - Theme customization
- **Intuitive Navigation** - Easy access to all features
- **Real-time Updates** - Live feedback and status indicators

### 🔄 API Integration

- **RESTful Communication** - Clean API client architecture
- **Error Handling** - Graceful error management and user feedback
- **Request Caching** - Optimized performance with smart caching
- **Session Management** - Persistent user sessions
- **Retry Logic** - Automatic retry on failed requests

### 📊 Advanced Functionality

- **Export Options** - Download results in multiple formats
- **History Tracking** - Access previous queries and results
- **Batch Processing** - Handle multiple requests efficiently
- **Customization** - Adjustable parameters for all features
- **Analytics** - Track usage and performance metrics

---

## 🛠️ Development

### Running Tests
```bash
# Run unit tests
python test.py

# Run interactive notebook
jupyter notebook test_notebook.ipynb
```

### Generate Folder Structure
```bash
python get_folder_structure.py
```

This will update `folder_structure.txt` with the current project structure.

### Development Mode

Enable debug mode in `.env`:
```env
DEBUG_MODE=True
```

This enables:
- Detailed error messages
- API request logging
- Performance metrics
- Hot reloading

### Adding New Features

1. Create a new UI module in `app/sections/`
2. Create corresponding CSS file in `app/styles/`
3. Add API endpoints in the backend
4. Update `api_client.py` with new API methods
5. Add navigation in `Home.py`
6. Update documentation

---

## 📦 Dependencies
```txt
streamlit>=1.28.0
requests>=2.31.0
python-dotenv>=1.0.0
pandas>=2.0.0
plotly>=5.17.0
streamlit-extras>=0.3.0
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
- Check `API_BASE_URL` in `.env`
- Verify no firewall blocking the connection
- Check backend logs for errors

### CSS Not Loading

**Problem:** Custom styles not applied  
**Solution:**
- Verify CSS files exist in `app/styles/`
- Check file paths in UI modules
- Clear browser cache (`Ctrl + F5`)
- Restart Streamlit app

### Environment Variable Issues

**Problem:** Config values not loading  
**Solution:**
```bash
# Verify .env file exists
ls -la .env

# Check environment variables
python -c "from app.utils.config import Config; print(Config.API_BASE_URL)"
```

### Import Errors

**Problem:** Module import failures  
**Solution:**
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

# Verify Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

---

## 🚀 Deployment

### Deploy to Streamlit Cloud

1. Push your code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Configure secrets (Settings → Secrets):
```toml
   [secrets]
   API_BASE_URL = "https://your-api-url.com"
   API_TIMEOUT = "30"
```
5. Deploy!

### Deploy with Docker
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app/Home.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Build and run:
```bash
docker build -t tubetalk-streamlit .
docker run -p 8501:8501 --env-file .env tubetalk-streamlit
```

### Deploy with Docker Compose
```yaml
version: '3.8'

services:
  streamlit:
    build: .
    ports:
      - "8501:8501"
    environment:
      - API_BASE_URL=http://fastapi:8000
    depends_on:
      - fastapi
    volumes:
      - ./app:/app/app
```

Run:
```bash
docker-compose up -d
```

---

## 📚 Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [TubeTalk.ai API Documentation](https://github.com/<your-username>/tubetalk-ai-api)
- [Python Requests Library](https://requests.readthedocs.io)
- [CSS Styling Guide](https://docs.streamlit.io/library/api-reference/utilities/st.markdown)

---


## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [TubeTalk.ai FastAPI Backend](https://github.com/<your-username>/tubetalk-ai-api)
- Icons from [Streamlit Emoji Shortcodes](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/)
- CSS inspiration from modern web design trends

---

## 📬 Contact

**Pranay**  
Student AI Engineer | Machine Learning Enthusiast

[![GitHub](https://img.shields.io/badge/GitHub-@pranay5519-181717?style=for-the-badge&logo=github)](https://github.com/pranay5519)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/pranay)

---


<div align="center">

Made with ❤️ and ☕ by [Pranay](https://github.com/pranay5519)

⭐ Star this repo if you find it useful!

**[Backend Repository](https://github.com/Pranay5519>/tubetalk-ai-api)** | **[Report Bug](https://github.com/Pranay5519/tubetalk-ai-streamlit/issues)** | **[Request Feature](https://github.com/Pranay5519/tubetalk-ai-streamlit/issues)**

</div>