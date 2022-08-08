from fastapi import APIRouter,Depends, HTTPException
from typing import List,Dict,Generator
from sqlalchemy.orm import Session


from db.session import SessionLocal
from models.todos import TodoModel
from models.user import UserModel
from schemas import TodoCreate, TodoPut, Todos, TodosInDb


todo_router = APIRouter()

#dependency function
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()




@todo_router.get("", 
tags=["TODOS"],
summary="get a list of all todo items",
status_code=200,
response_model=List[Todos]
)
def todos(db:Session = Depends(get_db)):
   
    return db.query(TodoModel).all()



@todo_router.get("/{todoID}", 
tags=["TODOS"],
response_model=TodosInDb,
summary="get a todo item",
status_code=200
)
def todo(todoID:int, db:Session = Depends(get_db)):
    
    tod = db.query(TodoModel).filter(TodoModel.id == todoID).first()
    userID = db.query(UserModel).filter(UserModel.id == tod.user_id).first()
    
    if not userID:
        raise HTTPException(status_code=401, detail=f"{userID} :user id doesn't exists ")
    
    return tod


@todo_router.post("", 
tags=["TODOS"],
response_model=Todos,
summary="add a todo item",
status_code=201
)
def  post_todo( payload:TodoCreate, db:Session = Depends(get_db)):
    
    userID = db.query(UserModel).filter(UserModel.id == payload.user_id).first()
    
    if not userID:
        raise HTTPException(status_code=401, detail=f"{userID} :user id doesn't exists ")
    
    res:Todos = TodoModel(title=payload.title, description=payload.description, user_id =payload.user_id)
    db.add(res)
    db.commit()
    return res


@todo_router.put("/{todoID}", 
tags=["TODOS"],
response_model=Todos,
summary="update a todo item",
status_code=200
)
def  update_todo(todoID:int, payload:TodoPut, db:Session = Depends(get_db)):
    item = db.query(TodoModel).filter(TodoModel.id == todoID).first()
    
    if not item:
        raise HTTPException(status_code=401, detail=f"{todoID} doesn't exists ")
    
    item.title = payload.title
    item.description = payload.description
    item.completed = payload.completed
    
    db.add(item)
    db.commit()
    
    return item


@todo_router.delete("/{todoID}", 
status_code=200,
summary="delete item",
response_model=Dict[str,str],
tags=["TODOS"]
)
def  delete_todo(todoID:int, db:Session = Depends(get_db)):
    item = db.query(TodoModel).filter(TodoModel.id == todoID).first()
    db.delete(item)
    db.commit()
    
    return {"message":"TodoID deleted"}