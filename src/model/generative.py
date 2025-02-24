from google import genai
from google.genai.types import GenerateContentResponse

from src.settings import Settings

def generate(prompt: str) -> GenerateContentResponse:
    settings = Settings()

    client = genai.Client(api_key=settings.generative_models.genai_api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )

    return response
