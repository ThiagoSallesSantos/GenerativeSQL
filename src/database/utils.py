## Description: Database utilities.

from enum import Enum

class DriverDatabase(str, Enum):
    postgresql = "postgresql+psycopg2"
    mysql = "mysql+pymysql"
