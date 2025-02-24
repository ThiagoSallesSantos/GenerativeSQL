## Description: Routes utilities.

from fastapi import Depends

from sqlalchemy import Engine, Row
from sqlalchemy.orm import Session
from src.database.connect import ConnectDatabase

from src.settings import Settings

from typing import Annotated, List, Sequence, Dict, Any

def get_session(engine: Engine) -> Session:
    return Session(engine)

def get_endpoint_session() -> Session:
    settings = Settings()
    connection_dabatabase = ConnectDatabase(
        dbms=settings.database.db_dbms,
        username=settings.database.db_username,
        password=settings.database.db_password.get_secret_value(),
        host=settings.database.db_host,
        port=settings.database.db_port,
        database=settings.database.db_database
    )
    return get_session(engine=connection_dabatabase.get_engine())

EndpointSession = Annotated[Session, Depends(get_endpoint_session)]

def convert_row_to_list(rows: Sequence[Row]) -> List:
    result: List[Dict[str, Any]] = list([])
    for row in rows:
        result.append(row._asdict())
    return result