from tables.report import *
from tables.ageint import *
from datetime import datetime
from tables.terorist import *
from get_reportes import *
from fastapi import FastAPI,Depends
import uvicorn
from items.item_agent import *
from items.item_report import *
from items.item_terrorist import *
create_db_and_tables()
add_agent("shaye","g","87")
app = FastAPI()

@app.get("/")
def get():
    return "hii"

@app.get("/reports")
def reports():
    return get_reports_by_id()

@app.get("/reports/{id}")
def reports_id(id:int):
    return get_reports_by_id(id)

@app.get("/reports/by_terrorist/{id}")
def teror(id:int):
    return get_by_terrorist(id)

@app.get("/report_by_word/{word}")
def word(word:str):
    return get_report_by_report(word)

@app.get("/dangers")
def dengers():
    return dangerous_terrorist()

@app.get("/super_dangers")
def super():
    return super_dangerous_terrorist()

@app.get("/true_agent/{id}/{name}")
def agent(id:int,name:str):
    bool = true_agent(id,name)
    if bool == True:
        return "exxist"
    return "not exxist"

@app.put("/agent")
def agent_add(item:ItemAgent):
    create_db_and_tables()

    name = item.name
    expertise = item.expertise
    unit = item.unit

    id = add_agent(name,expertise, unit)

    return {"id":id,"name":name,"expertise":expertise,"unit":unit}


@app.put("/terrorist")
def terrorist_add(item:ItemTerrorist):
    create_db_and_tables()
    id = add_terrorist(item.name,item.city,item.wappens)
    return {"id":id,"name":item.name,"city":item.city,"wappents":item.wappens}

@app.put("/report")
def report_add(item:ItemReport):
    create_db_and_tables()
    id = add_report(item.agent,item.terrorist,item.reliability_level,item.report)
    return {"id":id,"agent":item.agent,"terrorist":item.terrorist,"level":item.reliability_level,"report":item.report}


if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port = 800)