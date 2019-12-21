#!/usr/bin/python3
"""
first State object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import Base, State

if __name__ == "__main__":
    """Prints a query from a table mapped using SQLAlchemy
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/\
{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
