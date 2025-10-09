import streamlit as st
from app.utils.api_client import get_summary  # Make sure this imports your API function

def render(video_url, thread_id,api_key_input):
    st.markdown('<h1 class="custom-header">📄 Summary</h1>', unsafe_allow_html=True)
    def load_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    load_css("app/styles/summary.css")
    # Session state flags 
    if "summary_generated" not in st.session_state:
        st.session_state.summary_generated = False
    if "summary_data" not in st.session_state:
        st.session_state.summary_data = None
        
    if "video_timestamp" not in st.session_state:
        st.session_state.video_timestamp = 0
    
    # Button to generate summary
    if not st.session_state.summary_generated:
        if st.button("Generate Summary"):
            summary_response = get_summary(thread_id=thread_id, youtube_url=video_url,api_key=api_key_input)
            if summary_response:
                st.session_state.summary_data = summary_response
                st.session_state.summary_generated = True
            else:
                st.error("❌ Failed to generate summary. Please try again.")
                
    if st.session_state.summary_generated and st.session_state.summary_data:
        st.subheader("Generated Summary")

        for i, topic in enumerate(st.session_state.summary_data, 1):
            # Topic text and play button
            col1, col2 = st.columns([4, 1])
            with col1:
                st.markdown(f"**{i}: {topic['topic']}**")
                if "summary" in topic:
                    st.write(topic["summary"])
            with col2:
                if st.button("▶", key=f"play_topic_{i}"):
                    st.session_state.video_timestamp = int(float(topic.get("timestamp", 0)))
                    st.rerun()

            # Subtopics displayed directly
            for j, sub in enumerate(topic.get("subtopics", []), 1):
                sub_col1, sub_col2 = st.columns([4, 1])
                with sub_col1:
                    st.markdown(f"**{i}.{j}: {sub['subtopic']}**")
                    if "summary" in sub:
                        st.text(sub["summary"])
                with sub_col2:
                    if st.button("▶", key=f"play_sub_{i}_{j}"):
                        st.session_state.video_timestamp = int(float(sub.get("timestamp", 0)))
                        st.rerun()

            st.markdown("---")