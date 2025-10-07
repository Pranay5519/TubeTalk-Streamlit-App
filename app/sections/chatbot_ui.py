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


def render(video_url, thread_id):
    st.header("🤖 Chatbot")

    # Custom CSS to keep chat input fixed at bottom
    st.markdown("""
        <style>
        .stChatInput {
        position: fixed;
        bottom: 0;
        right: 1px;        /* distance from right edge */
        width: 400px;       /* set your desired width */
        background-color: white;
        padding: 1rem;
        z-index: 999;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
        border-radius: 8px;
    }

        .stChatInputContainer {
            position: fixed;
            bottom: 0;
            left: 10;
            right: 0;
            background-color: white;
            padding: 1rem;
            z-index: 999;
            box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
        }
        section[data-testid="stChatInput"] {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: white;
            padding: 1rem;
            z-index: 999;
            box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
        }
        /* Add padding to main content to prevent overlap */
        .main .block-container {
            padding-bottom: 100px;
        }
        </style>
    """, unsafe_allow_html=True)

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
            print(thread_id)
            messages = get_chat_history(thread_id)
            # Clean unwanted system/debug messages
            cleaned_history = clean_history(messages)
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
            response = chat_with_bot(thread_id, prompt)
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