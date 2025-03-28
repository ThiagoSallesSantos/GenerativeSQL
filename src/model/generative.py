import ollama

from src.schemas.schemas import ModelGeneratedSQLSchema

def generate_sql(prompt: str) -> ModelGeneratedSQLSchema:
    response = ollama.generate(
        model="llama3.2",
        prompt=prompt,
        format=ModelGeneratedSQLSchema.model_json_schema(),
        options=ollama.Options(
            temperature=0.0,
            num_ctx=8192
        ),
        keep_alive=0
    )

    generated_sql = ModelGeneratedSQLSchema.model_validate_json(response.response)

    return generated_sql
