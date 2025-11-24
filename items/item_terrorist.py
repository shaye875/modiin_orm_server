from pydantic import BaseModel
class ItemTerrorist(BaseModel):
    name:str
    city:str
    wappens:str