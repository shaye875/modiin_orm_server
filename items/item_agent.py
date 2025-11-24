from pydantic import *
class ItemAgent(BaseModel):
    name:str
    expertise:str
    unit:str