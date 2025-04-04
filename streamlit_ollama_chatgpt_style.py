import streamlit as st
import ollama

# Set the page config for a centered layout
st.set_page_config(page_title="Ollama Chatbot", layout="centered")

# Display the title
st.title("Ollama Chatbot (ChatGPT-Style)")

# Initialize message history if not already in session state
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! How can I help you today?"}]

# Display the chat history using ChatGPT-like bubbles
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Get user input from the chat input box
user_input = st.chat_input("Type your message here...")

if user_input:
    # Append the user's message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Call Ollama with the current conversation history
    response = ollama.chat(model="phi", messages=st.session_state.messages)
    assistant_message = response["message"]["content"]
    
    # Append the assistant's response
    st.session_state.messages.append({"role": "assistant", "content": assistant_message})
    
    # The script will re-run automatically, updating the UI.
