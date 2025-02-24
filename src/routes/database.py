## Description: Database routes

from fastapi import APIRouter, HTTPException

from src.routes.utils import EndpointSession

from src.database.models import DatabaseConnectionConfig
from src.database.query import add_db, get_db, delete_db

from src.schemas.input import CreateConfigDatabaseConnection
from src.schemas.output import DatabaseConnectionConfigResponse

router = APIRouter(prefix="/database", tags=["Database"])

@router.post("/", response_model=DatabaseConnectionConfigResponse,
    summary="Create a connection to a database",
    description="""
        Receive the connection data to a database.
    """,
)
def create_connect_database(
    database_connection_config: CreateConfigDatabaseConnection,
    session: EndpointSession
):
    try:
        new_database_connection_config = DatabaseConnectionConfig(
            database_connection_config_dbms=database_connection_config.dbms.value,
            database_connection_config_username=database_connection_config.username,
            database_connection_config_password=database_connection_config.password.get_secret_value(),
            database_connection_config_host=database_connection_config.host,
            database_connection_config_port=database_connection_config.port,
            database_connection_config_database=database_connection_config.database
        )
        
        add_db(new_database_connection_config, session=session)

        return DatabaseConnectionConfigResponse.model_validate(new_database_connection_config) 

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{database_connection_config_id}/", response_model=DatabaseConnectionConfigResponse,
    summary="Get a connection to a database",
    description="""
        Recover a database connection config.
    """,
)
def get_connect_database(
    database_connection_config_id: int,
    session: EndpointSession
):
    try:
        database_connection_config = get_db(
            model=DatabaseConnectionConfig,
            database_connection_config_id=database_connection_config_id,
            get_all=False,
            session=session,
        )

        if database_connection_config is None:
            raise HTTPException(status_code=404, detail="Database connection not found")

        return DatabaseConnectionConfigResponse.model_validate(database_connection_config)

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{database_connection_config_id}/", response_model=DatabaseConnectionConfigResponse,
    summary="Delete a connection to a database",
    description="""
        Delete a database connection config.
    """,
)
def delete_connect_database(
    database_connection_config_id: int,
    session: EndpointSession
):
    try:
        database_connection_config = get_db(
            model=DatabaseConnectionConfig,
            database_connection_config_id=database_connection_config_id,
            get_all=False,
            session=session,
        )

        if database_connection_config is None:
            raise HTTPException(status_code=404, detail="Database connection not found")

        delete_db(
            model=DatabaseConnectionConfig,
            database_connection_config_id=database_connection_config_id,
            session=session,
        )

        return DatabaseConnectionConfigResponse.model_validate(database_connection_config)

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
