## Description: Input schemas for the API

from pydantic import BaseModel, SecretStr, Field

from enum import Enum

from typing import Optional

class DatabaseDBMS(str, Enum):
    POSTGRESQL = "postgresql"
    MYSQL = "mysql"

class CreateConfigDatabaseConnection(BaseModel):
    dbms: DatabaseDBMS
    username: str
    password: SecretStr
    host: str
    port: int
    database: str

class GenerateSQL(BaseModel):
    query: str
    database_connection_config_id: int
    only_sql: bool = Field(default=False)
