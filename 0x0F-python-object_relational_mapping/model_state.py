#!/usr/bin/python3
""" 
    python is lame
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import column, Integer, String
from sqlalchemy import UniqueConstraint, Nullable, VARCHAR
""" docs is docs
"""


Base = declarative_base()
class State(Base):
    """my class
    """
    __tablename__ = 'states'
    id = column('id', Integer, UniqueConstraint, not Nullable)
    name = column('name', VARCHAR(128), not Nullable)
