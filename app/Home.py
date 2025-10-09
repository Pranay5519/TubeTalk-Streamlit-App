import streamlit as st
from app.sections import chatbot_ui, quiz_ui, summary_ui, topics_ui
from app.utils.utility_functions import get_embed_url
from app.utils.api_client import get_thread_ids , get_url_by_thread_id
# Page config
st.set_page_config(page_title="TubeTalk AI", layout="wide")

# Initialize session_state
if "started" not in st.session_state:
    st.session_state.started = False
if "video_url" not in st.session_state:
    st.session_state.video_url = ""
if "thread_id" not in st.session_state:
    st.session_state.thread_id = ""
if "video_timestamp" not in st.session_state:
    st.session_state.video_timestamp = 0
if "embeddings_created" not in st.session_state:
    st.session_state.embeddings_created = False
if "history_loaded" not in st.session_state:
    st.session_state.history_loaded = False
if "messages" not in st.session_state:
    st.session_state.messages = []
if "api_key" not in st.session_state:
    st.session_state.api_key = ""    
st.sidebar.title("TubeTalk AI Settings")

st.sidebar.title("TubeTalk AI Settings")

# --- SIDEBAR INPUT FORM ---
with st.sidebar.form("start_form"):
    video_url = st.text_input("Enter Video URL:", st.session_state.video_url)
    thread_id_input = st.text_input("Enter Thread ID:", st.session_state.thread_id)
    #api_key_input = st.text_input("Enter Google Gen API Key", st.session_state.api_key , type = "password")
    submitted = st.form_submit_button("Start")

# --- EXISTING THREAD IDS SECTION ---
thread_ids = [tid for tid in get_thread_ids() if tid.strip() != ""]
print("Thread IDs:", thread_ids)

st.sidebar.markdown("### 🔑 Google API Key ")
api_key_input = st.sidebar.text_input(
    "Enter your Google API Key", 
    type="password", 
    key="google_api_key_history"
)

st.sidebar.markdown("### 💾 Saved Thread IDs")

clicked_thread = None  # Temporary variable to store which thread button was clicked
for tid in thread_ids:
    if st.sidebar.button(str(tid)):
        clicked_thread = tid

# --- HANDLE START FORM SUBMISSION ---
if submitted:
    if video_url.strip() and thread_id_input.strip():
        st.session_state.thread_id = thread_id_input
        st.session_state.video_url = get_embed_url(video_url)
        st.session_state.api_key = api_key_input  # ✅ store API key in session
        st.session_state.started = True
        st.session_state.history_loaded = False
        st.session_state.embeddings_created = False
        st.session_state.messages = []
        st.session_state.quiz_data = None
        st.session_state.summary_data = None
        st.session_state.topics_data = None
    else:
        st.warning("⚠️ Please fill in both fields!")

# --- HANDLE EXISTING THREAD BUTTON CLICK ---
if clicked_thread:
    st.session_state.thread_id = clicked_thread
    st.session_state.video_url = get_embed_url(get_url_by_thread_id(clicked_thread)['url'])
    st.session_state.api_key = api_key_input  or st.session_state.api_key  # ✅ use input if provided, else keep old key
    st.session_state.started = True
    st.session_state.history_loaded = False
    st.session_state.embeddings_created = False
    st.session_state.messages = []

# Main page
st.title("TubeTalk AI")

if st.session_state.started:
    # Custom CSS to make col2 (tabs section) sticky and hide scrollbars
    st.markdown("""
        <style>
        /* Make the main content area have fixed height */
        .main .block-container {
            max-width: 100%;
            padding-top: 1rem;
        }
        
        /* Make col2 (second column with tabs) sticky */
        div[data-testid="stHorizontalBlock"] > div:last-child {
            position: sticky;
            top: 80px;
            height: fit-content;
            z-index: 10;
        }
        
        /* Allow col1 (video column) to scroll normally */
        div[data-testid="stHorizontalBlock"] > div:first-child {
            overflow-y: auto;
        }
        
        /* Ensure tabs content area is scrollable if needed */
        div[data-testid="stHorizontalBlock"] > div:last-child [data-testid="stVerticalBlock"] {
            max-height: calc(100vh - 150px);
            overflow-y: auto;
        }
        
        /* Hide scrollbars but keep functionality */
        div[data-testid="stHorizontalBlock"] > div:first-child::-webkit-scrollbar,
        div[data-testid="stHorizontalBlock"] > div:last-child [data-testid="stVerticalBlock"]::-webkit-scrollbar {
            display: none;
        }
        
        div[data-testid="stHorizontalBlock"] > div:first-child,
        div[data-testid="stHorizontalBlock"] > div:last-child [data-testid="stVerticalBlock"] {
            -ms-overflow-style: none;  /* IE and Edge */
            scrollbar-width: none;  /* Firefox */
        }
        
        /* Ensure video container doesn't overflow */
        div[data-testid="stHorizontalBlock"] > div:first-child iframe {
            max-width: 100%;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Create two columns: 60% for video, 40% for content
    col1, col2 = st.columns([3, 2])  # 3:2 ratio = 60%:40%
    
    with col1:
        st.subheader("📺 Video")
        # Get embed URL with timestamp
        embed_url = get_embed_url(st.session_state.video_url)
        video_url_with_time = f"{embed_url}?start={st.session_state.video_timestamp}&autoplay=1"
        print(video_url_with_time)
        # Display YouTube video with iframe for timestamp control
        st.markdown(f"""
            <div style="width: 100%;">
                <iframe width="100%" height="500"
                style="max-width: 100%;"
                src="{video_url_with_time}"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write;
                encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
                </iframe>
            </div>
        """, unsafe_allow_html=True)
        if st.button("New Chat"):
            st.session_state.started = False 
            st.session_state.video_url = ""
            st.session_state.thread_id = ""
            st.session_state.video_timestamp = 0
            st.session_state.embeddings_created = False
            st.session_state.history_loaded = False
            st.session_state.messages = []
            #st.session_state.api_key = ""
            st.rerun()
    with col2:
        # Tabs for different features
        tab1, tab2, tab3, tab4 = st.tabs(["📝 Quiz", "🤖 Chatbot", "📄 Summary", "📌 Topics"])
        
        with tab1:
            quiz_ui.render(st.session_state.video_url, st.session_state.thread_id,st.session_state.api_key)
        
        with tab2:
            chatbot_ui.render(st.session_state.video_url, st.session_state.thread_id,st.session_state.api_key)
        
        with tab3:
            summary_ui.render(st.session_state.video_url, st.session_state.thread_id,st.session_state.api_key)
        
        with tab4:
            topics_ui.render(st.session_state.video_url, st.session_state.thread_id,st.session_state.api_key)
            
        