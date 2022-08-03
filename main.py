from fastapi import FastAPI
import requests
from typing import List,Dict
from datetime import datetime
import json

from schemas import TodoCreate, TodoPut, Todos

app = FastAPI(
    title="Todo API",
    description = "A basic todo api",
    version = "0.1.0",
)



@app.get("/", 
summary="Home route",
status_code=200,
)
def home():
    
   return "Hello you!"



@app.get("/todos", 
tags=["TODOS"],
summary="get a list of all todo items",
status_code=200,
responses={200: {"description": "Ok"}, 201:{"description": "Accepted"}},
response_model=List[Todos],
)
def todos():
    
    with open('db.json', 'r') as f:
       payload = json.load(f)
   
    return payload


@app.get("/todos/{todoID}", 
tags=["TODOS"],
response_model=Todos,
summary="get a todo item",
status_code=200,
responses={200: {"description": "Ok"}, 201:{"description": "Accepted"}}
)
def todo(todoID:int):
    
    with open('db.json', 'r') as f:
       payload = json.load(f)
   
    return payload[todoID]


@app.post("/todos", 
tags=["TODOS"],
response_model=Todos,
summary="add a todo item",
status_code=200,
responses={200: {"description": "Ok"}, 201:{"description": "Accepted"}}
)
def  post_todo( payload: TodoCreate):
    
    pay = dict(payload)
    spay = str( pay["created"]  )
    pay["created"] = spay
    
    with open('db.json', 'r') as f:
       data = json.load(f)
    
    data.append(pay)
    
    with open('db.json', 'w') as f:
        json.dump(data, f)

    return payload


@app.put("/todos/{todoID}", 
tags=["TODOS"],
summary="update a todo item",
status_code=200,
responses={200: {"description": "Ok"}, 201:{"description": "Accepted"}}
)
def  update_todo(todoID:int, payload:TodoPut):
    with open('db.json', 'r') as f:
       data = json.load(f)
   
   #update some 
    pay = data[todoID] 
    payloadz = dict(payload)
    pay["title"] = payloadz["title"]
    pay["description"] =payloadz["description"]
    pay["completed"] = payloadz["completed"]
    
    #update the file
    with open('db.json', 'w') as f:
        json.dump(data, f)

    return {"message":"TodoID updated"}


@app.delete("/todos/{todoID}", 
status_code=200,
summary="delete item",
response_model=Dict[str,str],
tags=["TODOS"],
responses={200: {"summary": "Ok"}, 201:{"summary": "Accepted"}}
)
def  delete_todo(todoID:int):
    #read the file
    with open('db.json', 'r') as f:
       payload = json.load(f)
   
   #delete some 
    payload.remove(payload[todoID])
    
    #update the file
    with open('db.json', 'w') as f:
        json.dump(payload, f)

    
    return {"message":"TodoID deleted"}