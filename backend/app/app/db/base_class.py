from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Table

# declarative base class
Base = declarative_base()
"""
class Base(Bse):
    id: int = Column(Integer, primary_key=True, index=True)
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
"""