import streamlit as st
from app.utils.api_client import generate_quiz
from app.utils.utility_functions import get_embed_url

def render(video_url, thread_id):
    st.header("📝 Quiz Section")
    
    if "quiz_generated" not in st.session_state:
        st.session_state.quiz_generated = False
    if "quiz_data" not in st.session_state:
        st.session_state.quiz_data = None
    if "video_timestamp" not in st.session_state:
        st.session_state.video_timestamp = 0
        
    if not st.session_state.quiz_generated:
        if st.button("Generate Quiz"):
            quiz_response = generate_quiz(thread_id=thread_id, youtube_url=video_url)
            if quiz_response:
                print("Quiz Generated Successfully")
                print(quiz_response)
                st.session_state.quiz_data = quiz_response['quizzes']
                st.session_state.quiz_generated = True
            else:
                st.error("Failed to generate quiz. Please try again.")
    
    if st.session_state.quiz_generated and st.session_state.quiz_data:
        st.subheader("Generated Quiz")

        for i, quiz in enumerate(st.session_state.quiz_data, 1):
            col1, col2 = st.columns([4, 1])
            
            with col1:
                st.text(f"Question {i}: {quiz['question']}")

                # Radio button for options with no preselection
                user_answer = st.radio(
                    f" ",
                    quiz['options'],
                    key=f"q{i}",
                    index=None
                )

                # Show correctness only after selection
                if user_answer is not None:
                    if user_answer == quiz['correct_answer']:
                        st.success("✅ Correct!")
                    else:
                        st.error(f"❌ Wrong! Correct answer is: {quiz['correct_answer']}")

            with col2:
                if st.button("▶️ Play", key=f"play_q_{i}"):
                    # Update the timestamp in session state
                    st.session_state.video_timestamp = int(float(quiz.get('timestamp', 0)))
                    st.rerun()  # Refresh to update the video in col1

            st.markdown("---")