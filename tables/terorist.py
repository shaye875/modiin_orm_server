from typing import Optional
from sqlmodel import SQLModel, Field, create_engine, Session, select,func
from tables.report import *

class Terrorist(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    city: str
    wappens: str

def add_terrorist(name, city, wappens):
        terrorist = Terrorist(name=name,city = city, wappens = wappens)
        with Session(engine) as session:
            session.add(terrorist)
            session.commit()
            session.refresh(terrorist)
            return terrorist.id


def get_terrorist(id = None):
     if id == None:
      with Session(engine) as session:
        stamete = select(Terrorist)
        result = session.exec(stamete)
        terrorist = result.all()
        return terrorist
     with Session(engine) as session:
          stamete = select(Terrorist).where(Terrorist.id == id)
          result = session.exec(stamete)
          terrorist = result.all()
          return terrorist

def name_by_id1(id):
    with Session(engine) as session:
        statement = select(Terrorist.name).where(Terrorist.id == id)
        result = session.exec(statement)
        terrorist = result.one()
        return terrorist
