from fastapi import APIRouter, HTTPException

from src.routes.utils import EndpointSession, get_session, convert_row_to_list

from src.database.connect import ConnectDatabase
from src.database.models import DatabaseConnectionConfig
from src.database.query import get_db, query_db

from src.model.inspect_database import get_database_struct

from src.model.prompt import get_sql_prompt
from src.model.generative import generate_sql

from src.schemas.schemas import (GenerateSQLResponse, RequestGenerateSQLSchema, 
                                RequestGenerateSQLWithDatabaseConnectionSchema)

router = APIRouter(prefix="/generate", tags=["Generate"])

@router.post("/sql/", response_model=GenerateSQLResponse,
    summary="Create a generative SQL",
    description="""
        Receive the query and database connection data to generate a SQL.
    """,
)
def create_generated_sql(
    data: RequestGenerateSQLSchema,
):
    try:
        prompt_sql = get_sql_prompt(query=data.query, database_struct=data.database_struct)

        genarated_sql = generate_sql(prompt=prompt_sql)

        return GenerateSQLResponse(sql=genarated_sql)

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/sql/{database_connection_config_id}/", response_model=GenerateSQLResponse,
    summary="Create a generative SQL",
    description="""
        Receive the query and database connection data to generate a SQL.
    """,
)
def create_generated_sql_with_database_connection(
    database_connection_config_id: int,
    data: RequestGenerateSQLWithDatabaseConnectionSchema,
    session_db: EndpointSession
):
    try:
        database_connection_config: DatabaseConnectionConfig = get_db(
            table=DatabaseConnectionConfig,
            database_connection_config_id=database_connection_config_id,
            get_all=False,
            session=session_db,
        )

        if database_connection_config is None:
            raise HTTPException(status_code=404, detail="Database connection not found")

        connection_database = ConnectDatabase(
            dbms=database_connection_config.database_connection_config_dbms,
            username=database_connection_config.database_connection_config_username,
            password=database_connection_config.database_connection_config_password,
            host=database_connection_config.database_connection_config_host,
            port=database_connection_config.database_connection_config_port,
            database=database_connection_config.database_connection_config_database
        )
        user_database_engine = connection_database.get_engine()

        database_struct = data.database_struct
        if database_struct is None:
            database_struct = get_database_struct(engine=user_database_engine)

        prompt_sql = get_sql_prompt(query=data.query, database_struct=database_struct)

        genarated_sql = generate_sql(prompt=prompt_sql)

        if data.only_sql:
            return GenerateSQLResponse(sql=genarated_sql.sql)

        session_user_database_connection = get_session(engine=user_database_engine)
        result_db = query_db(query=genarated_sql.sql, session=session_user_database_connection)
        result = convert_row_to_list(rows=result_db.all())
        
        return GenerateSQLResponse(result=result, sql=genarated_sql)

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
