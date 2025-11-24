from typing import Optional
from sqlmodel import SQLModel, Field, create_engine, Session, select,func
from datetime import datetime

class Report(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    agent:Optional[int]= Field(foreign_key="agent.id")
    terrorist:Optional[int] = Field(default=None,foreign_key="terrorist.id")
    time:str = datetime.now()
    reliability_level:int
    report:str


engine = create_engine("sqlite:///reporters.db")


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def add_report(agent,terrorist,level,report):
    report = Report(agent = agent,terrorist = terrorist,reliability_level = level,report = report)
    with Session(engine) as session:
        session.add(report)
        session.commit()
        session.refresh(report)
        print(f"add repore id = {report.id}")




