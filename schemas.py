from datetime import datetime
from pydantic import BaseModel
from typing import Optional,List
import itertools


# id_iter = itertools.count()
#(next(id_iter))

class TodoBase(BaseModel): 
    title:str
    description:str
   
   
class TodoCreate(TodoBase):
    user_id:int
   

class TodoPut(BaseModel):
    title:Optional[str]
    description:Optional[str]
    completed:Optional[bool]
    

class Todos(TodoBase):
    id:int
    completed:bool
    created:datetime
    
    class Config:
        orm_mode = True
    
    
#users schema sasa

class UserBase(BaseModel):  
    first_name:str
    last_name:str
    email:str
    

class UserCreate(UserBase):
    pass
   

class UserPut(BaseModel):
    first_name:Optional[str]
    last_name:Optional[str]
    email:Optional[str]
    

class Users(UserBase):
    id:int
    created:datetime
    
    class Config:
        orm_mode = True
    
class UsersInDb(UserBase):
    id:int
    created:datetime
    todos:List[Todos]
    
    class Config:
        orm_mode = True

class TodosInDb(TodoBase):
    id:int
    completed:bool
    created:datetime
    user:Users
    class Config:
        orm_mode = True