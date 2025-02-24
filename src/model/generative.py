import ollama
from ollama import GenerateResponse

def generate(prompt: str) -> GenerateResponse:
    response = ollama.generate(
        model="llama3.2",
        prompt=prompt
    )

    return response
