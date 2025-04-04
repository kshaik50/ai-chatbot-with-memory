🧠 Ollama Chatbot – ChatGPT-Style Interface (Mac Local)

Welcome to the AI Chatbot with Memory, a local-first, privacy-friendly chatbot that mimics the ChatGPT experience — built with Streamlit, powered by Ollama, and running LLMs directly on your MacBook (M1/M2/M3) using models like phi, llama2, or mistral.

⚡️ No cloud needed. Fully local. Chat like ChatGPT – but it’s all yours.

⸻

🚀 Features
	•	🧩 Streamlit-based ChatGPT UI
	•	🧠 Conversational memory (chat history)
	•	🖥️ Runs locally via Ollama (optimized for macOS)
	•	⚙️ Plug-and-play with models like phi, mistral, llama2, etc.
	•	💬 Chat input at the bottom like ChatGPT
	•	🔒 100% private. No data leaves your machine.

⸻

📦 Requirements
	•	macOS (M1/M2/M3 preferred)
	•	Python 3.10+
	•	Ollama installed locally
	•	Streamlit 1.28+

⸻

🛠️ Installation

# Clone the repo
git clone https://github.com/yourusername/ai-chatbot-with-memory.git
cd ai-chatbot-with-memory

# (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt



⸻

⚡ Running the App

Make sure Ollama is installed and running.

Then launch:

streamlit run streamlit_ollama_chatgpt_style.py

📍 The app will open at http://localhost:8501

⸻

🤖 Switch Models Easily

To use a different Ollama model, update this line in your Python code:

response = ollama.chat(model="phi", messages=history)

Change "phi" to:
	•	"llama2"
	•	"mistral"
	•	"codellama" (for code)
	•	"gemma" (Google)
	•	etc.

⸻

📁 Project Structure

ai-chatbot-with-memory/
│
├── streamlit_ollama_chatgpt_style.py   # Main app
├── requirements.txt                    # Python dependencies
├── README.md                           # This file
└── ... (your project files)



⸻

🌟 Credits

Built with ❤️ by Kurshid Shaik
Powered by Ollama, Streamlit, and your local CPU/GPU.

⸻

📜 License

MIT License – Free to use, modify, and distribute.
