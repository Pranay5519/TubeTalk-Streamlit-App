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


import os
import streamlit as st

def load_css(file_path):
    """Load CSS from a file and inject it into Streamlit"""
    try:
        with open(file_path, 'r') as f:
            css = f.read()
        st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"CSS file not found: {file_path}")
    except Exception as e:
        st.error(f"Error loading CSS: {str(e)}")

def get_css_path(filename):
    """Get the absolute path to a CSS file"""
    # Get the directory where this utility file is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to app directory, then into styles
    css_path = os.path.join(current_dir, '..', 'styles', filename)
    return os.path.abspath(css_path)