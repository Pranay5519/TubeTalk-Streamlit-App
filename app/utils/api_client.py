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
        response = requests.post(summary_url, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get("main_summary")
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None
    except requests.RequestException as e:
        print(f"Error calling /summary/get_summary: {e}")
        return None

if __name__ == "__main__":
    youtube_url = "https://youtu.be/s3KnSb9b4Pk"
    thread_id = "check1"

    summary_text = get_summary(thread_id, youtube_url)
    if summary_text:
        print("\nSummary Response:")
        print(summary_text)
    else:
        print("Failed to get summary.")