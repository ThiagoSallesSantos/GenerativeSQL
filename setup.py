from src.settings import Settings
from src.database.connect import ConnectDatabase

from src.database.models import Base

settings = Settings()

connection_dabatabase = ConnectDatabase(
    dbms=settings.database.db_dbms,
    username=settings.database.db_username,
    password=settings.database.db_password.get_secret_value(),
    host=settings.database.db_host,
    port=settings.database.db_port,
    database=settings.database.db_database
)

engine = connection_dabatabase.get_engine()

Base.metadata.create_all(bind=engine)
