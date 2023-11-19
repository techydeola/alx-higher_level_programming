#!/usr/bin/python3
"""
    this module contains the class definition of a State
    and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base


mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
        A class that declares two attributes
            id: id of a table
            name: name of a state
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
