import gradio as gr
from chatbot import chat
from memory import get_memory, store_message

chat_history = []

def respond(user_input, history):
    context = get_memory(user_input)
    prompt = context + "\nUser: " + user_input + "\nAI:"
    answer = chat(prompt)
    store_message(user_input + "\n" + answer)
    history.append((user_input, answer))
    return history, history

gr.ChatInterface(fn=respond).launch()
