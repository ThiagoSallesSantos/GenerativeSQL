from pydantic import BaseModel, Field, ConfigDict

from src.services.models.schemas.schemas import GeneratedSQLSchema

from typing import List, Dict, Any

class ConfiguredDatabaseConnectionSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(alias='database_connection_config_id')
    dbms: str = Field(alias='database_connection_config_dbms')
    username: str = Field(alias='database_connection_config_username')
    host: str = Field(alias='database_connection_config_host')
    port: int = Field(alias='database_connection_config_port')
    database: str = Field(alias='database_connection_config_database')


class GeneratedSQLResultSchema(BaseModel):
    result: List[Dict[str, Any]] = Field(default=[])
    sql: GeneratedSQLSchema

