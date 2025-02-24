## Description: Database models for the application.

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String

class Base(DeclarativeBase):
    pass

class DatabaseConnectionConfig(Base):
    """
    DatabaseConnection model.
    """
    __tablename__ = "database_connection_config"

    database_connection_config_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True,)
    database_connection_config_dbms: Mapped[int] = mapped_column(String(length=50))
    database_connection_config_username: Mapped[str] = mapped_column(String(length=50))
    database_connection_config_password: Mapped[str] = mapped_column(String)
    database_connection_config_host: Mapped[str] = mapped_column(String(length=50))
    database_connection_config_port: Mapped[int] = mapped_column(Integer)
    database_connection_config_database: Mapped[str] = mapped_column(String(length=100))

    def __repr__(self) -> str:
        return f"<DatabaseConnection(dbms={self.database_connection_config_dbms}, username={self.database_connection_config_username}, host={self.database_connection_config_host}, port={self.database_connection_config_port}, database={self.database_connection_config_database})>"
    