from tables.report import *
from tables.terorist import *
from tables.ageint import *
def get_reports_by_id(id = None):
    if id != None:
     with Session(engine) as session:

        result = session.exec(select(Report).where(Report.id == id)).all()
        return result
    with Session(engine) as session:
         statement = select(Report)
         result = session.exec(statement)
         reports = result.all()
         return reports

def get_report_by_report(word):
    with Session(engine) as session:
        statement = select(Report)
        result = session.exec(statement)
        reports = result.all()
        for r in reports:
             if word in r.report:
                    return r
    return None

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
        statement = select(Report.terrorist,func.count(Report.id)).group_by(Report.terrorist)
        result = session.exec(statement)
        reports = result.all()
        list = []
        for id in reports:
            if id[1] >= 5:
              list.append(id[0])
        list1 = []
        for l in list:
            list1.append(get_terrorist(l))
        return list1

def super_dangerous_terrorist():
        with Session(engine) as session:
            statement = select(Report.terrorist, func.count(Report.id)).group_by(Report.terrorist)
            result = session.exec(statement)
            reports = result.all()
            list = []
            for id in reports:
                if id[1] >= 10:
                    list.append(id[0])
        list1 = []
        for l in list:
            list1.append(get_terrorist(l))
        return list1

