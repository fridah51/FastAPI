from fastapi import FastAPI
from datetime import datetime
from typing import Dict, Generator, List



from db.base_class import Base
from db.session import SessionLocal, engine
from models.todos import TodoModel
from models.user import UserModel

#create tables
Base.metadata.create_all(bind=engine)


#router
from api_routes.api import router

app = FastAPI(
    title="Todo API",
    description = "A basic todo api",
    version = "0.2.0",
)

app.include_router(router, responses={200:{"description":"Ok"}})


#dependency function
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()



@app.get("/", 
summary="Home route",
status_code=200,
)
def home():
    
   return "Hello you!"


