## Description: Input schemas for the API

from pydantic import BaseModel, SecretStr, Field, ConfigDict

from enum import Enum

from typing import Optional, List, Dict, Tuple, Sequence, Union, Any

class ChoiceDatabaseDBMS(str, Enum):
    POSTGRESQL = "postgresql"
    MYSQL = "mysql"

class CreateConfigDatabaseConnectionSchema(BaseModel):
    dbms: ChoiceDatabaseDBMS
    username: str
    password: SecretStr
    host: str
    port: int
    database: str

class ConfigDatabaseConnectionSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(alias='database_connection_config_id')
    dbms: str = Field(alias='database_connection_config_dbms')
    username: str = Field(alias='database_connection_config_username')
    host: str = Field(alias='database_connection_config_host')
    port: int = Field(alias='database_connection_config_port')
    database: str = Field(alias='database_connection_config_database')

class ModelGeneratedSQLSchema(BaseModel):
    sql: str

class RequestGenerateSQLWithDatabaseConnectionSchema(BaseModel):
    query: str
    database_struct: Optional[Union[List, Dict, Tuple, Sequence, str]] = Field(default=None)
    only_sql: bool = Field(default=True)

class RequestGenerateSQLSchema(BaseModel):
    query: str
    database_struct: Union[List, Dict, Tuple, Sequence, str]

class GenerateSQLResponse(BaseModel):
    result: List[Dict[str, Any]] = Field(default=[])
    sql: ModelGeneratedSQLSchema

