import streamlit as st
from app.utils.api_client import create_embeddings, chat_with_bot , get_chat_history
from app.utils.utility_functions import get_embed_url


def clean_history(message_history):
    """
    Remove unwanted system/debug messages from DB history
    and return cleaned messages.
    """
    cleaned = []
    for msg in message_history:
        content = msg.get("content", "")
        if "LOAD_HISTORY" in content:
            continue
        if "I am sorry, I cannot answer this question" in content:
            continue
        cleaned.append(msg)
    return cleaned


def render(video_url, thread_id,api_key_input):
    #st.header("🤖 Chatbot")
    st.markdown('<h1 class="custom-header">🤖 chatbot</h1>', unsafe_allow_html=True)
    # Custom CSS to keep chat input fixed at bottom
    def load_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    load_css("app/styles/chatbot.css")

    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []  # stores {"role": "user"/"ai", "content": "message"}
    if "embeddings_created" not in st.session_state:
        st.session_state.embeddings_created = False
    if "history_loaded" not in st.session_state:
        st.session_state.history_loaded = False
    if "video_timestamp" not in st.session_state:
        st.session_state.video_timestamp = 0.0
    

    # Step 1: Create embeddings only once
    if not st.session_state.embeddings_created:
        with st.spinner("🔄 Creating embeddings from the video transcript..."):
            embeddings = create_embeddings(thread_id, video_url)
            if embeddings:
                st.session_state.embeddings_created = True
                if embeddings['type'] == "created":
                    st.success("✅ Embeddings created successfully!")
                else:
                    st.success("✅ Embeddings loaded successfully!")
            else:
                st.error("❌ Failed to create embeddings. Please try again.")

    # Step 2: Load history from DB (only once)
    if not st.session_state.history_loaded:
        with st.spinner("📂 Loading chat history from DB..."):
            print("loading chat using: ",thread_id)
            messages = get_chat_history(thread_id=thread_id,api_key=api_key_input)
            print("Loaded messages:", messages)
            # Clean unwanted system/debug messages
            cleaned_history = clean_history(messages)
            print("Cleaned Messages" , cleaned_history)
            for msg in cleaned_history:
                role = "user" if msg["type"] == "human" else "ai"
                st.session_state.messages.append(
                    {"role": role, "content": msg["content"]}
                )
            st.session_state.history_loaded = True
    # Step 3: Show all messages
    for idx, message in enumerate(st.session_state["messages"]):
        with st.chat_message(message["role"]):
            if message["role"] == "ai":
                if "Timestamp:" in message["content"]:
                    response_text, timestamp = map(
                        str.strip, message["content"].split("Timestamp:")
                    )
                    st.text(response_text)
                    if st.button("▶️ Watch", key=f"watch_{idx}"):
                        # Update timestamp and refresh like Quiz UI
                        st.session_state.video_timestamp = int(float(timestamp))
                        st.rerun()
                else:
                    st.text(message["content"])
            else:
                st.text(message["content"])

    # Step 4: User input
    if prompt := st.chat_input("Ask something about the video..."):
        # Save user msg
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.text(prompt)
        # Call chatbot API
        with st.spinner("🤖 Thinking..."):
            response = chat_with_bot(thread_id=thread_id, question=prompt,api_key=api_key_input)
            if response:
                bot_reply = response.get("answer", "⚠️ No response from bot")

                # Also update message history from response
                if "message_history" in response:
                    st.session_state.messages = []
                    cleaned_history = clean_history(response["message_history"])
                    for msg in cleaned_history:
                        role = "user" if msg["type"] == "human" else "ai"
                        st.session_state.messages.append(
                            {"role": role, "content": msg["content"]}
                        )
            else:
                bot_reply = "❌ Error: Could not connect to chatbot API."
                st.session_state.messages.append({"role": "ai", "content": bot_reply})
        
        st.rerun()