import streamlit as st
from app.utils.api_client import get_topics

def render(video_url, thread_id):
    st.header("📌 Key Topics Section")

    if "topics_generated" not in st.session_state:
        st.session_state.topics_generated = False
    if "topics_data" not in st.session_state:
        st.session_state.topics_data = None
    if "video_timestamp" not in st.session_state:
        st.session_state.video_timestamp = 0
        
    # 👇 This is the missing button
    if not st.session_state.topics_generated:
        if st.button("Generate Topics"):
            topics_response = get_topics(thread_id=thread_id, youtube_url=video_url)
            if topics_response:
                print("topics Generated")
                #print("Topics : " , topics_response)
                st.session_state.topics_data = topics_response
                st.session_state.topics_generated = True
            else:
                st.error("Failed to generate topics. Please try again.")

    if st.session_state.topics_generated and st.session_state.topics_data:
        st.subheader("Generated Topics")

        output = st.session_state.topics_data  # alias for readability

        for i, topic in enumerate(output["main_topics"], 1):
            col1, col2 = st.columns([4, 1])
            
            with col1:
                st.markdown(f"🎯 **Main Topic {i}: {topic['topic']}**")
                if "content" in topic:
                    st.caption(topic["content"])

            with col2:
                if st.button("▶️ Play", key=f"play_main_{i}_{thread_id}"):
                    st.session_state.video_timestamp = int(float(topic.get("timestamp", 0)))
                    st.rerun()

            # Subtopics
            for j, sub in enumerate(topic.get("subtopics", []), 1):
                sub_col1, sub_col2 = st.columns([4, 1])

                with sub_col1:
                    st.markdown(f"   🔹 **Subtopic {i}.{j}:** {sub['subtopic']}")
                    if "content" in sub:
                        st.caption(sub["content"])

                with sub_col2:
                    if st.button("▶️ Play", key=f"play_sub_{i}_{j}_{thread_id}"):
                        st.session_state.video_timestamp = int(float(sub.get("timestamp", 0)))
                        st.rerun()

            st.markdown("---")