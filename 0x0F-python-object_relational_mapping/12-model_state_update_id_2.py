#!/usr/bin/python3
"""
    a script that changes the name of a State object
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

    obj = session.query(State).filter_by(id=2).first()
    if obj is not None:
        obj.name = 'New Mexico'
        session.commit()

    session.close()
