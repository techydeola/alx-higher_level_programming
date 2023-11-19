#!/usr/bin/python3
"""
    this module is a script that lists all State
    objects from the database hbtn_0e_6_usa
"""
import sys
import sqlalchemy
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for items in session.query(State).order_by(State.id):
        print(items.id, items.name, sep=": ")
