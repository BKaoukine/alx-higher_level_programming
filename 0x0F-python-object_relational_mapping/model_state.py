#!/usr/bin/python3
"""
A module to define the State class and connect to
a MySQL database using SQLAlchemy.

This module demonstrates how to use SQLAlchemy to define
a class representing a state and connect to a MySQL database.

Usage:
    The module can be imported and used to interact with a MySQL database.

Classes:
    State: A class representing a state with attributes id and name.
"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# Create an instance of Base
Base = declarative_base()


class State(Base):
    """
    A class representing a state.

    Attributes:
        id (int): The unique identifier for the state.
        name (str): The name of the state.
    """

    __tablename__ = "states"

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)


# Create an engine to connect to the MySQL database
engine = create_engine(
    "mysql://username:password@localhost:3306/database_name"
    )

# Create the table in the database
Base.metadata.create_all(engine)
