#!/usr/bin/python3

"""
A script to connect to a MySQL database using.

SQLAlchemy and retrieve data from the State table.

Usage:
    The script requires three command-line
    arguments: username, password, and database name.
    Example: ./script.py username password database_name
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys
from sqlalchemy import create_engine, func

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
        )
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)

    session_one = session()
    count = session_one.query(func.count()).select_from(State).scalar()
    if count == 0:
        print("Nothing")
    results = session_one.query(State).filter(State.id == 1)

    for state in results:
        print(state.id, state.name, sep=": ")

    session_one.close()
