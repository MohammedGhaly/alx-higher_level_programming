#!/usr/bin/python3
'''class definition of a State and an instance Base = declarative_base()'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declerative_base()


class State(Base):
    '''a class that represents a state'''
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
