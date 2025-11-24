from typing import Optional
from sqlmodel import SQLModel, Field,create_engine,Session,select
from tables.report import *
class Agent(SQLModel,table = True):
    id:Optional[int] = Field(default=None,primary_key=True)
    name:str
    expertise:str
    unit:str

def add_agent(name,expertise, unit):
        agent = Agent(name=name,expertise =expertise,unit = unit)
        with Session(engine) as session:
            session.add(agent)
            session.commit()
            session.refresh(agent)
        print(f"added course with id = {agent.id}")

def get_agents_by_id(id):
        with Session(engine) as session:
            statement = select(Agent).where(Agent.id == id)
            result = session.exec(statement)
            agents = result.all()
            return agents