from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import column, String, Integer, Nullable

engine = create_engine('mysql+mysqldb://omar:231003@localhost/school', echo = False)

#with engine.connect() as connection:
    # Now you can execute your SQL queries
    #result = connection.execute(text("""create table people(name VARCHAR(256) not null, age int not null, id int not null)"""))

Base = declarative_base()
class People(Base):
    __tablename__ = "people"


    id = column('id', Integer,not Nullable)
    name = column('name', String)
