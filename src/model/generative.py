import ollama

from src.model.schemas.schemas import GeneratedSQLSchema

def generate_sql(prompt: str) -> GeneratedSQLSchema:
    response = ollama.generate(
        model="llama3.2",
        prompt=prompt,
        format=GeneratedSQLSchema.model_json_schema(),
        options=ollama.Options(
            temperature=0.0,
            num_ctx=8192
        ),
        keep_alive=0
    )

    generated_sql = GeneratedSQLSchema.model_validate_json(response.response)

    return generated_sql
