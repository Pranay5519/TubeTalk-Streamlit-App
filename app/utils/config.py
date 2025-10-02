from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Read keys from environment variables
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")  # fallback default
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")