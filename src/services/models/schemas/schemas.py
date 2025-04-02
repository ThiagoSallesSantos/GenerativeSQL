from pydantic import BaseModel

class GeneratedSQLSchema(BaseModel):
    sql: str