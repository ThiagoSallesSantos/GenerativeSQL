## Description: This file contains the query functions for the database

from functools import singledispatch

from sqlalchemy.orm import Session
from sqlalchemy import text, Result

from src.database.models import Base

from typing import List, Union, Dict, Any

@singledispatch
def add_db(data: Base, *, session: Session) -> None:
    session.add(data)
    session.commit()

@add_db.register(list)
def add_db_list(list_of_data: List[Base], *, session: Session) -> None:
    for data in list_of_data:
        session.add(data)
    session.commit()

def get_db(model: Base, *, session: Session, get_all: bool = True, **kwargs) -> Union[List[Base], Base, None]:
    if get_all:
        return session.query(model).filter_by(**kwargs).all()
    return session.query(model).filter_by(**kwargs).first()

def delete_db(model: Base, *, session: Session, **kwargs) -> None:
    session.query(model).filter_by(**kwargs).delete()
    session.commit()

def query_db(query: str, session: Session) -> Result:
    return session.execute(text(query))
