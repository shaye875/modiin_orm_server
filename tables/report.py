from typing import Optional
from sqlmodel import SQLModel, Field, create_engine, Session, select,func
from datetime import datetime
from tables.terorist import *
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

def get_reports_by_id(id = None):
    if id != None:
     with Session(engine) as session:
        statement = select(Report).where(Report.id == id)
        result = session.exec(statement)
        reports = result.all()
        return reports
    with Session(engine) as session:
         statement = select(Report)
         result = session.exec(statement)
         reports = result.all()
         return reports

def get_report_by_word(word):
    with Session(engine) as session:
        statement = select(Report).where(Report.report == word)
        result = session.exec(statement)
        reports = result.all()
        return reports

def del_report(id):
    with Session(engine) as session:
        statement = select(Report).where(Report.id == id)
        result = session.exec(statement)
        reports = result.one()
        session.delete(reports)
        session.commit()

def get_by_terrorist(terrorist):
    with Session(engine) as session:
        statement = select(Report).where(Report.terrorist == terrorist)
        result = session.exec(statement)
        terrorist = result.all()
        return terrorist

def dangerous_terrorist():
    with Session(engine) as session:
        statement = select(func.count(Report))
        result = session.exec(statement)
        reports = result.all()
        return reports


