import streamlit as st
from app.utils.api_client import generate_quiz
from app.utils.utility_functions import get_embed_url
st.set_page_config(page_title="Quiz", layout="wide")

def render(video_url, thread_id):
    st.header("📝 Quiz Section")
    
    if "quiz_generated" not in st.session_state:
        st.session_state.quiz_generated = False
    if "quiz_data" not in st.session_state:
        st.session_state.quiz_data = None
    if "play_index" not in st.session_state:
        st.session_state.play_index = None
        
    if not st.session_state.quiz_generated:
        if st.button("Generate Quiz"):
            quiz_response = generate_quiz(thread_id=thread_id , youtube_url=video_url)
            if quiz_response:
                print("Quiz Genrated Successfully")
                print(quiz_response)
                st.session_state.quiz_data = quiz_response['quizzes']
                st.session_state.quiz_generated = True
            else:
                st.error("Failed to generate quiz. Please try again.")
    
    if st.session_state.quiz_generated and st.session_state.quiz_data:
        st.subheader("Generated Quiz")
        embed_url = video_url.replace("watch?v=", "embed/")  # YouTube embed URL

        for i, quiz in enumerate(st.session_state.quiz_data, 1):
            col1, col2 = st.columns([4, 1])
            
            with col1:
                st.markdown(f"### Question {i}: {quiz['question']}")

                # Radio button for options with no preselection
                user_answer = st.radio(
                    f"Choose your answer for Question {i}",
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
                    st.session_state.play_index = (f"quiz-{i}", quiz.get('timestamp', 0))

            st.markdown("---")
         # Step 3: Embed YouTube video at selected timestamp
        if st.session_state.play_index:
            label, timestamp = st.session_state.play_index
            start_time = int(float(timestamp))
            embed_url = get_embed_url(video_url)
            play_video_url = f"{embed_url}?start={start_time}&autoplay=0"
            st.markdown(f"""
                <iframe width="800" height="450"
                src="{play_video_url}"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write;
                encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
                </iframe>
            """, unsafe_allow_html=True)