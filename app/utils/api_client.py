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

# -------------------------
# Example usage
# -------------------------
"""if __name__ == "__main__":
    thread_id = "roadmap"
    youtube_url = "https://youtu.be/s3KnSb9b4Pk"

    result = generate_quiz(thread_id, youtube_url)
    print("Quiz Response:")
    print(result)
"""