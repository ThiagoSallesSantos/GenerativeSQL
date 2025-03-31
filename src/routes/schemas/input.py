from pydantic import BaseModel, SecretStr, Field

from enum import Enum

from typing import Optional, List, Dict, Tuple, Sequence, Union

class ChoiceDatabaseDBMS(str, Enum):
    POSTGRESQL = "postgresql"
    MYSQL = "mysql"

class ConfigDatabaseConnectionSchema(BaseModel):
    dbms: ChoiceDatabaseDBMS
    username: str
    password: SecretStr
    host: str
    port: int
    database: str

class GenerateSQLDatabaseConnectionSchema(BaseModel):
    query: str
    database_struct: Optional[Union[List, Dict, Tuple, Sequence, str]] = Field(default=None)
    only_sql: bool = Field(default=True)

class GenerateSQLSchema(BaseModel):
    query: str
    database_struct: Union[List, Dict, Tuple, Sequence, str]
