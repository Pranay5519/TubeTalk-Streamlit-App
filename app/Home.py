import streamlit as st
from app.sections import chatbot_ui, quiz_ui, summary_ui, topics_ui

# Page config
st.set_page_config(page_title="TubeTalk AI", layout="wide")

# Initialize session_state
if "started" not in st.session_state:
    st.session_state.started = False
if "video_url" not in st.session_state:
    st.session_state.video_url = ""
if "thread_id" not in st.session_state:
    st.session_state.thread_id = ""

st.sidebar.title("TubeTalk AI Settings")

# Sidebar inputs
with st.sidebar.form("start_form"):
    video_url = st.text_input("Enter Video URL:", st.session_state.video_url)
    thread_id = st.text_input("Enter Thread ID:", st.session_state.thread_id)
    submitted = st.form_submit_button("Start")

if submitted:
    if video_url.strip() != "" and thread_id.strip() != "":
        st.session_state.started = True
        st.session_state.video_url = video_url
        st.session_state.thread_id = thread_id
    else:
        st.warning("Please fill in both fields!")

# Main page
st.title("TubeTalk AI")

if st.session_state.started:
    # Create two columns: left for video, right for content
    col1, col2 = st.columns([1, 2])  # Video takes 1/3, content takes 2/3
    
    with col1:
        st.subheader("📺 Video")
        # Display YouTube video
        st.video(st.session_state.video_url)
    
    with col2:
        # Tabs for different features
        tab1, tab2, tab3, tab4 = st.tabs(["📝 Quiz", "🤖 Chatbot", "📄 Summary", "📌 Topics"])
        
        with tab1:
            quiz_ui.render(st.session_state.video_url, st.session_state.thread_id)
        
        with tab2:
            chatbot_ui.render(st.session_state.video_url, st.session_state.thread_id)
        
        with tab3:
            summary_ui.render(st.session_state.video_url, st.session_state.thread_id)
        
        with tab4:
            topics_ui.render(st.session_state.video_url, st.session_state.thread_id)

if not st.session_state.started :
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