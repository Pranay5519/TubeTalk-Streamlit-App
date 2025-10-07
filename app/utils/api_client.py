import requests
from app.utils.config import API_BASE_URL, GOOGLE_API_KEY

def generate_quiz(thread_id: str, youtube_url: str):
    """
    Calls the /quiz/generate_quiz endpoint with the given thread_id and youtube_url.
    """
    quiz_url = f"{API_BASE_URL.rstrip('/')}/quiz/generate_quiz"

    # Query parameters
    params = {
        "url": youtube_url,
        "thread_id": thread_id
    }

    # Headers
    headers = {
        "gemini-api-key": GOOGLE_API_KEY
    }

    try:
        response = requests.post(quiz_url, params=params, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None
    except requests.RequestException as e:
        print(f"Error calling /quiz/generate_quiz: {e}")
        return None


def get_topics(thread_id: str, youtube_url: str):
    """
    Calls the /topics/get_topics endpoint with the given thread_id and youtube_url.
    """
    topics_url = f"{API_BASE_URL.rstrip('/')}/topics/get_topics"

    # Query parameters
    params = {
        "url": youtube_url,
        "thread_id": thread_id
    }

    # Headers
    headers = {
        "gemini-api-key": GOOGLE_API_KEY
    }

    try:
        response = requests.post(topics_url, params=params, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None
    except requests.RequestException as e:
        print(f"Error calling /topics/get_topics: {e}")
        return None

def get_summary(thread_id: str, youtube_url: str):
    """
    Calls the /summary/get_summary endpoint with the given thread_id and youtube_url.
    Returns the main_summary from the response.
    """
    summary_url = f"{API_BASE_URL.rstrip('/')}/summary/get_summary"

    # Query parameters
    params = {
        "url": youtube_url,
        "thread_id": thread_id
    }

    # Headers (API key for authentication)
    
    headers = {
        "gemini-api-key": GOOGLE_API_KEY
    }
    try:
        response = requests.post(summary_url, params=params,headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get("main_summary")
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None
    except requests.RequestException as e:
        print(f"Error calling /summary/get_summary: {e}")
        return None

def create_embeddings(thread_id: str, youtube_url: str):
    """
    Calls /chatbot/create_embeddings to generate embeddings from a YouTube transcript.
    """
    url = f"{API_BASE_URL}/chatbot/create_embeddings"

    payload = {
        "youtube_url": youtube_url,
        "thread_id": thread_id
    }
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None
    except requests.RequestException as e:
        print("Error calling create_embeddings:", e)
        return None
    
def chat_with_bot(thread_id: str, question: str):
    """
    Calls /chatbot/chat to ask questions about the video.
    """
    url = f"{API_BASE_URL}/chatbot/chat"

    payload = {
        "thread_id": thread_id,
        "question": question
    }
    headers = {
        "gemini-api-key": GOOGLE_API_KEY
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None
    except requests.RequestException as e:
        print("Error calling chat:", e)
        return None

def get_chat_history(thread_id: str):
    """
    Fetch chat history for a given thread_id from the FastAPI /get_message_history endpoint.
    """
    history_url = f"{API_BASE_URL}/chatbot/get_message_history"

    # Query parameters
    params = {
        "thread_id": thread_id
    }

    # Headers (API key for authentication)
    headers = {
        "gemini-api-key": "AIzaSyCuSbrEpqerOdAo4JVlZ3n7rr14mPMwRFM",
        "Content-Type": "application/json"
    }

    try:
        # Make the POST request
        response = requests.post(history_url, params=params, headers=headers)
        
        # Check HTTP status code
        if response.status_code == 200:
            return response.json()  # Return the chat history
        else:
            print(f"Error {response.status_code}: {response.text}")
            return []
    except Exception as e:
        print("Error calling /get_message_history:", e)
        return []


def get_thread_ids():
    """
    Calls /thread_ids/all_conversations to fetch all saved thread IDs from the database.
    """
    url = f"{API_BASE_URL}/thread_ids/all_conversations"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print("✅ All thread_ids Retrieved Successfully!")
            return data["conversations"]
        else:
            print(f"❌ Error {response.status_code}: {response.text}")
            return None
    except requests.RequestException as e:
        print("Error calling /thread_ids/all_conversations:", e)
        return None
    

def get_url_by_thread_id(thread_id: str):
    """
    Calls /url/{thread_id} to fetch the YouTube URL linked with a specific thread_id.
    """
    url = f"{API_BASE_URL}/url/{thread_id}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ URL Retrieved for Thread ID '{thread_id}'")
            return data
        elif response.status_code == 404:
            print(f"⚠️ No URL found for Thread ID '{thread_id}'")
            return None
        else:
            print(f"❌ Error {response.status_code}: {response.text}")
            return None
    except requests.RequestException as e:
        print("Error calling /url/{thread_id}:", e)
        return None
    