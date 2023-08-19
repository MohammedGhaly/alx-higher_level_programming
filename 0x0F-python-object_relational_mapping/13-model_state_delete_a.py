#!/usr/bin/python3
"""
    a script that deletes all State objects with name containing the letter a
"""


from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State).filter(State.name.ilike('%a%')).all()
    for obj in data:
        session.delete(obj)
    session.commit()

    session.close()
