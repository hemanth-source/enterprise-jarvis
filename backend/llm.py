import requests
from config import OLLAMA_URL

def generate_answer(prompt):
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json()["response"]
