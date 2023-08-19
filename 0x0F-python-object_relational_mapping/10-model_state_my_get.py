#!/usr/bin/python3
"""
    prints the State object with the name passed as argument
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
    obj = session.query(State).filter(State.name.in_([argv[4]])) \
                              .order_by(State.id).first()

    if obj is not None:
        print(f'{obj.id}')
    else:
        print('Not found')

    session.close()
