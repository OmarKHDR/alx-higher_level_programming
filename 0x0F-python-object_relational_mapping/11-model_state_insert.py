#!/usr/bin/python3
"""more comments cafew"""

import sys
from sqlalchemy import Integer, String, Nullable
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    ses = Session()
    obj = State(name='Louisiana')
    ses.add(obj)
    ses.commit()
    st = ses.query(State).order_by(State.id).filter(State.name == 'Louisiana')
    if st is not None:
        print("{}".format(st.id))
