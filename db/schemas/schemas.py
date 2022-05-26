from typing import Optional
from pydantic import BaseModel,EmailStr

class Manufacture( BaseModel ):
    company_name : str

    class Config:  # to convert non dict obj to json
        orm_mode = True
 


class Equipment_Type(BaseModel):

           equipment_type : str

           class Config:  # to convert non dict obj to json
             orm_mode = True
    



class Location(BaseModel):

    loc_name : str
    building : str
    contact_number : str

    class Config:  # to convert non dict obj to json
        orm_mode = True

class Equipment(BaseModel):
    pass
   
class UserCreate(BaseModel):
    staffno:int
    staffname:str
    password:str

    class Config:
        orm_mode=True