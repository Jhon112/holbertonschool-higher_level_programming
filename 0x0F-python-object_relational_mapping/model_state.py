#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
"""
create a new table states
"""
Base = declarative_base()


class State(Base):
    """ Popertys of clas State: id and name """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
