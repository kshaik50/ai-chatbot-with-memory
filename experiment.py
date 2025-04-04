import streamlit as st
import ollama

# Set the page config for a wide, polished layout
st.set_page_config(page_title="💬 Ollama Chatbot", layout="wide")

# Inject custom CSS for enhanced styling
st.markdown(
    """
    <style>
    /* Light gray background */
    body {
      background-color: #f5f5f5;
    }
    /* Chat message styling */
    .stChatMessage {
      font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
      font-size: 1rem;
    }
    /* Chat bubble style */
    .chat-bubble {
      border-radius: 15px;
      padding: 12px;
      margin: 5px 0;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    /* User messages: light green bubble, aligned right */
    .stChatMessage.user .chat-bubble {
      background-color: #dcf8c6;
      align-self: flex-end;
    }
    /* Assistant messages: white bubble, aligned left */
    .stChatMessage.assistant .chat-bubble {
      background-color: #ffffff;
      align-self: flex-start;
    }
    </style>
    """, unsafe_allow_html=True
)

# Display the title
st.title("💬 Ollama Chatbot (ChatGPT-Style)")

# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! How can I help you today?"}]

# Display chat messages in order
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(f'<div class="chat-bubble">{msg["content"]}</div>', unsafe_allow_html=True)

# Chat input box at the bottom (like ChatGPT)
user_input = st.chat_input("Type your message here...")

if user_input:
    # Append user's message to the conversation history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Call Ollama with the full conversation as context
    response = ollama.chat(model="phi", messages=st.session_state.messages)
    assistant_message = response["message"]["content"]
    
    # Append the assistant's reply
    st.session_state.messages.append({"role": "assistant", "content": assistant_message})
    
    # The app will naturally re-run on new input; no experimental_rerun call is needed.
