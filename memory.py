from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
import os

embedding = HuggingFaceEmbeddings()
DB_DIR = "./memory"

if not os.path.exists(DB_DIR):
    os.makedirs(DB_DIR)

db = Chroma(persist_directory=DB_DIR, embedding_function=embedding)

def store_message(text):
    db.add_texts([text])

def get_memory(query):
    docs = db.similarity_search(query, k=1)
    return docs[0].page_content if docs else ""
