import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL_NAME = "llama3"


def generate_email(prompt: str):

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code != 200:
        raise Exception("Failed to connect to Ollama")

    data = response.json()

    return data.get("response", "No response generated")