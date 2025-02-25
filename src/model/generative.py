import ollama

from src.model.utils import GeneratedSQL

def generate_sql(prompt: str) -> GeneratedSQL:
    response = ollama.generate(
        model="llama3.2",
        prompt=prompt,
        format=GeneratedSQL.model_json_schema(),
        options=ollama.Options(
            temperature=0.0
        ),
        keep_alive=0
    )

    generated_sql = GeneratedSQL.model_validate_json(response.response)

    return generated_sql