#!/usr/bin/python3

"""
    this module contains Base field and State class
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer

Base = declerative_base()


class State(Base):
    """
        State class , inherits the from Base class
        Attributes:
            id (int)
            name (string)
    """
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
