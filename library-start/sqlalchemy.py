from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Person(Base):
    __tablename__ = "people"
    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, ssn, first, last, gender, age):
        self.ssn = ssn
        self.firstname = first
        self.lastname = last
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"({self.ssn} {self.firstname} {self.lastname} {self.gender} {self.age})"

class Thing(Base):
    __tablename__ = "things"

    tid = Column("tid", Integer, primary_key=True)
    description = Column("description", String)
    owner = Column(Integer, ForeignKey("people.ssn"))

    def __init__(self, tid, description, owner):
        self.tid = tid
        self.description = description
        self.owner = owner

    def __repr__(self):
        return f"({self.tid} {self.description} owned by {self.owner})"


engine = create_engine("sqlite:///D:\library-start\mydb2.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
person = Person(3243542, "Mike", "Smith", "m", 35)
session.add(person)
session.commit()
p1 = Person(2342543, "Anna", "Blue", "f", 40)
p2 = Person(4353453, "Angela", "Cold", "f", 24)
session.add(p1)
session.add(p2)
session.commit()

t1 = Thing(20, "Car", p1.ssn)
t2 = Thing(30, "Laptop", p1.ssn)
t3 = Thing(40, "Smartphone", p2.ssn)
t4 = Thing(50, "Desktop", p1.ssn)
t5 = Thing(60, "Airplane", p2.ssn)
session.add(t1)
session.add(t2)
session.add(t3)
session.add(t4)
session.add(t5)
session.commit()

results = session.query(Thing, Person).filter(Thing.owner == Person.ssn).filter(Person.firstname == "Anna")

for r in results:
    print(r)