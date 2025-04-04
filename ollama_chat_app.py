import gradio as gr
import ollama

def convert_history(hist):
    """
    Convert incoming history to OpenAI-style message format (list of dicts).
    If history is empty, initialize with a system prompt.
    If history items are tuples, convert them to dicts.
    """
    if not hist:
        return [{"role": "system", "content": "You are a helpful assistant."}]
    
    # If every item is already a dict, assume it's correctly formatted.
    if all(isinstance(x, dict) for x in hist):
        return hist
    
    # Otherwise, assume it's a list of tuples in (user_message, assistant_message) format.
    new_hist = [{"role": "system", "content": "You are a helpful assistant."}]
    for item in hist:
        if isinstance(item, tuple) and len(item) == 2:
            new_hist.append({"role": "user", "content": item[0]})
            new_hist.append({"role": "assistant", "content": item[1]})
    return new_hist

def chat_with_ollama(user_message, history):
    # Convert history to proper message format.
    new_history = convert_history(history)
    
    # Append the new user message.
    new_history.append({"role": "user", "content": user_message})
    
    # Call Ollama with the updated history.
    response = ollama.chat(model="phi", messages=new_history)
    assistant_message = response['message']['content']
    
    # Append assistant's response.
    new_history.append({"role": "assistant", "content": assistant_message})
    
    # Return the updated history twice, as required by ChatInterface.
    return new_history, new_history

# Create the ChatInterface with type set to "messages"
gr.ChatInterface(
    fn=chat_with_ollama,
    title="💬 Ollama Chatbot (Mac Native)",
    description="Chat with a blazing-fast local LLM using Ollama + Gradio.",
    theme="default",  # Using default theme to avoid the 'compact' 404 error
    type="messages"   # Use OpenAI-style message dictionaries
).launch()
