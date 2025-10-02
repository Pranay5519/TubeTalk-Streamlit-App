import re
def get_embed_url(url: str) -> str:
    """Convert any YouTube URL into an embeddable format."""
    match = re.search(r"v=([^&]+)", url)
    if match:
        return f"https://www.youtube.com/embed/{match.group(1)}"
    match = re.search(r"youtu\.be/([^?&]+)", url)
    if match:
        return f"https://www.youtube.com/embed/{match.group(1)}"
    if "embed" in url:
        return url
    return url