from pydantic import BaseModel

class GeneratedSQL(BaseModel):
    sql: str