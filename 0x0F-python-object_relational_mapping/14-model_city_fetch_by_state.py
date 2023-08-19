#!/usr/bin/python3
"""
    a script 14-model_city_fetch_by_state.py that prints all City objects
"""


from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).all()
    cities = session.query(City).all()

    states_ids = {}
    for city in cities:
        if city.state_id not in states_ids.keys():
            for s in states:
                if s.id == city.state_id:
                    states_ids[city.state_id] = s.name
                    break
        print(f'{states_ids[city.state_id]}: ({city.id}) {city.name}')

    session.close()
