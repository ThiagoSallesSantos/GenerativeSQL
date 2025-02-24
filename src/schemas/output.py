## Description: Output schemas for the API
from pydantic import BaseModel, ConfigDict, Field
from typing import List, Dict, Any

class DatabaseConnectionConfigResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(alias='database_connection_config_id')
    dbms: str = Field(alias='database_connection_config_dbms')
    username: str = Field(alias='database_connection_config_username')
    host: str = Field(alias='database_connection_config_host')
    port: int = Field(alias='database_connection_config_port')
    database: str = Field(alias='database_connection_config_database')

class GenerateSQLResponse(BaseModel):
    result: List[Dict[str, Any]] = Field(default=[])
    sql: str
