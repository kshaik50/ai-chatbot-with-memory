import streamlit as st
import ollama

# Set the page title
st.title("Ollama Chatbot (Streamlit)")

# Initialize chat history if not already set
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = [{"role": "system", "content": "You are a helpful assistant."}]

def get_response(user_message):
    # Get the current history from session state
    history = st.session_state["chat_history"]
    
    # Append the user's message to the history
    history.append({"role": "user", "content": user_message})
    
    # Call Ollama to get a response using the updated history
    response = ollama.chat(model="phi", messages=history)
    assistant_message = response['message']['content']
    
    # Append the assistant's message to the history
    history.append({"role": "assistant", "content": assistant_message})
    
    # Save the updated history in session state
    st.session_state["chat_history"] = history

# Input area for user message
user_input = st.text_input("Your message:")

# When the Send button is pressed and there's input, get a response.
if st.button("Send") and user_input:
    get_response(user_input)
    # Note: We are not using st.experimental_rerun() here.
    # Streamlit will naturally re-run the script after the button is pressed.

# Display the chat history
st.markdown("### Chat History")
for message in st.session_state["chat_history"]:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    elif message["role"] == "assistant":
        st.markdown(f"**Assistant:** {message['content']}")
