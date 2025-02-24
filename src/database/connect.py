## Description: This file is responsible for connecting to the database

from sqlalchemy import create_engine, URL, Engine

from src.database.utils import DriverDatabase

class ConnectDatabase:

    def __init__(
        self,
        dbms: str,
        username: str,
        password: str,
        host: str,
        port: int,
        database: str
    ) -> None:
        self.engine = create_engine(url=URL.create(
            drivername=DriverDatabase[dbms].value,
            username=username,
            password=password,
            host=host,
            port=port,
            database=database,
        ))

    def get_engine(self) -> Engine:
        return self.engine
