from datetime import datetime
from pydantic import BaseModel
from typing import Optional
import itertools


id_iter = itertools.count()
#(next(id_iter))

class TodoBase(BaseModel):
    id:int   
    title:str
    description:str
    completed:bool
    created:Optional[datetime]

class TodoCreate(TodoBase):
    pass
   

class TodoPut(BaseModel):
    title:Optional[str]
    description:Optional[str]
    completed:Optional[bool]
    

class Todos(TodoBase):
    id:int
    completed:bool
    created:datetime