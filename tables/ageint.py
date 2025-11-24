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
            return agent.id

def get_agents_by_id(id):
        with Session(engine) as session:
            statement = select(Agent).where(Agent.id == id)
            result = session.exec(statement)
            agents = result.all()
            return agents

def name_by_id(id):
    with Session(engine) as session:
        statement = select(Agent.name).where(Agent.id == id)
        result = session.exec(statement)
        agent = result.all()
        return agent

def true_agent(id,name):
    with Session(engine) as session:
        statement = select(Agent)
        result = session.exec(statement)
        agents = result.all()
        for r in agents:
            if id == r.id:
                if name == r.name:
                    return True
    return False