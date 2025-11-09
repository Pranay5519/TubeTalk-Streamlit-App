import streamlit as st
from app.sections import chatbot_ui, quiz_ui, summary_ui, topics_ui
from app.utils.utility_functions import get_embed_url
from app.utils.api_client import get_thread_ids , get_url_by_thread_id

# Page config
st.set_page_config(page_title="TubeTalk AI", layout="wide")

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_css("app/styles/home.css")
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

st.sidebar.title("TubeTalk.ai")

# --- SIDEBAR INPUT FORM ---
with st.sidebar.form("start_form"):
    video_url = st.text_input("🎥 Enter Video URL:", st.session_state.video_url)
    thread_id_input = st.text_input("🔗 Enter Thread ID:", st.session_state.thread_id)
    submitted = st.form_submit_button("🚀 Start")

# --- EXISTING THREAD IDS SECTION ---
thread_ids = [tid for tid in get_thread_ids() if tid.strip() != ""] if get_thread_ids() else []

print("Thread IDs:", thread_ids)

# if not session_state.api_key: ( Dont use these if here it will throw and error api key not defined)
st.sidebar.markdown("### 🔑 Google API Key ")
api_key_input = st.sidebar.text_input(
    "Enter your Google API Key", 
    type="password", 
    key="google_api_key_history"
)

st.sidebar.markdown("### 💾 Saved Thread IDs")

clicked_thread = None
for tid in thread_ids:
    if st.sidebar.button(f"📌 {str(tid)}"):
        clicked_thread = tid

# --- HANDLE START FORM SUBMISSION ---
if submitted:
    if video_url.strip() and thread_id_input.strip() and api_key_input.strip():
        st.session_state.thread_id = thread_id_input
        st.session_state.video_url = get_embed_url(video_url)
        st.session_state.api_key = api_key_input
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
    st.session_state.api_key = api_key_input or st.session_state.api_key 
    st.session_state.started = True
    st.session_state.history_loaded = False
    st.session_state.embeddings_created = False
    st.session_state.messages = []

# Main page
st.title("🎓 TubeTalk.ai")

if st.session_state.started:
    # Create two columns: 60% for video, 40% for content
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.subheader(f"📺 {st.session_state.thread_id}")
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
        if st.button("🔄 New Chat"):
            st.session_state.started = False 
            st.session_state.video_url = ""
            st.session_state.thread_id = ""
            st.session_state.video_timestamp = 0
            st.session_state.embeddings_created = False
            st.session_state.history_loaded = False
            st.session_state.messages = []
            st.rerun()
        st.text("Click aboave button for new chat")
    
    with col2:
        # Tabs for different features
        tab1, tab2, tab3, tab4 = st.tabs(["📝 Quiz", "🤖 Chatbot", "📄 Summary", "📌 Topics"])
        
        with tab1:
            quiz_ui.render(st.session_state.video_url, st.session_state.thread_id, st.session_state.api_key)
        
        with tab2:
            chatbot_ui.render(st.session_state.video_url, st.session_state.thread_id, st.session_state.api_key)
        
        with tab3:
            summary_ui.render(st.session_state.video_url, st.session_state.thread_id, st.session_state.api_key)
        
        with tab4:
            topics_ui.render(st.session_state.video_url, st.session_state.thread_id, st.session_state.api_key)

if not st.session_state.started:
    # Main Content
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        ## 🎯 Why TubeTalk.ai?
        
        **Transform hours of YouTube lectures into structured learning experiences!**
        
        Most students learn from YouTube lectures that are 1+ hours long with no structured notes or navigation. 
        TubeTalk.ai solves this by providing AI-powered learning tools that make video lectures interactive and efficient.
        
        ### 🚀 Core Features:
        """)
        
        # Feature Cards
        st.markdown("""
        <div class="feature-card">
            <h4>📝 SmartSummary</h4>
            <p>Get comprehensive lecture summaries and notes automatically generated from any YouTube lecture. 
            Perfect for quick review and study preparation.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h4>⏰ TimelineTopics</h4>
            <p>Navigate directly to specific topics with precise timestamps. 
            No more scrubbing through hour-long videos to find what you need!</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h4>💬 LectureChat</h4>
            <p>Ask questions about the lecture content and get detailed answers with exact timestamp references. 
            It's like having a teaching assistant available 24/7!</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h4>🧠 KnowledgeQuiz</h4>
            <p>Test your understanding with automatically generated quizzes based on lecture content. 
            Perfect for exam preparation and knowledge assessment.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h4>🎯 ConceptJump</h4>
            <p>Find exactly when specific concepts are introduced in the lecture. 
            Jump directly to "Machine Learning basics" or "Neural Networks" instantly!</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("### 🔧 Technology Stack")
        st.info("""
        **AI & ML:**
        - 🤖 Google Gemini 2.5 Flash
        - 🔗 LangChain/LangGraph
        - 📊 Vector Databases
        
        **Backend:**
        - 🐍 Python
        - ⚡ Flask/FastAPI
        - 🗄️ Database Storage
        
        **Features:**
        - 📋 Structured Output
        - 🎯 Precise Timestamps
        - 🔍 Semantic Search
        """)
        
    # How It Works Section
    st.markdown("---")
    st.markdown("## 🔄 How TubeTalk.ai Works")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        ### 1️⃣ Paste Link
        Simply paste any YouTube lecture URL into TubeTalk.ai
        """)

    with col2:
        st.markdown("""
        ### 2️⃣ AI Analysis
        Our AI processes the video transcript using advanced NLP
        """)

    with col3:
        st.markdown("""
        ### 3️⃣ Smart Features
        Get summaries, timelines, chat, and quizzes instantly
        """)

    with col4:
        st.markdown("""
        ### 4️⃣ Learn Better
        Navigate, understand, and test your knowledge efficiently
        """)

    # Footer
    st.markdown("---")
    st.markdown("### 🚀 Ready to Transform Your Learning?")
    st.markdown("""
    TubeTalk.ai makes YouTube lectures interactive, searchable, and much more effective for learning. 
    **👈 Select a feature from the sidebar** to see the magic in action!

    ### 💡 Perfect For:
    - 📚 **Students** preparing for exams
    - 🎓 **Researchers** reviewing conference talks  
    - 💼 **Professionals** learning new skills
    - 👨‍🏫 **Educators** creating course materials

    ### 🌟 Why Choose TubeTalk.ai?
    - ⚡ **Instant Processing** - Get results in seconds
    - 🎯 **Precise Timestamps** - Jump to exact moments  
    - 🧠 **AI-Powered** - Powered by Google Gemini 2.5 Flash
    - 📱 **Easy to Use** - Simple, intuitive interface

    ---
    *Built with ❤️ using LangChain, Google Gemini AI, and modern web technologies*
    """)