from pydantic import BaseModel
class ItemReport(BaseModel):
    agent:int
    terrorist:int
    reliability_level:int
    report:str