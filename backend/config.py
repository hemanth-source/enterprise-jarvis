import os
from dotenv import load_dotenv

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")

OLLAMA_URL = "http://localhost:11434/api/generate"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
