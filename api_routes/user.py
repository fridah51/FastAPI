from fastapi import APIRouter,Depends, HTTPException
from typing import List,Dict,Generator
from sqlalchemy.orm import Session


from schemas import Users, UsersInDb, UserCreate,UserPut
from db.session import  SessionLocal
from models.user import UserModel


user_router = APIRouter()


#dependency function
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()




#get all users
@user_router.get("",
response_model=List[Users],
summary="all users",
status_code=200
)
def users(db:Session= Depends(get_db)):
    return db.query(UserModel).all()


#get single user
@user_router.get("/{userID}",
response_model=UsersInDb,
summary="single user",
status_code=200
)
def users(userID:int, db:Session= Depends(get_db)):
    return db.query(UserModel).filter(UserModel.id == userID).first()


@user_router.post("",
response_model=UsersInDb,
summary="create new user",
status_code=201
)
def users_post(payload: UserCreate, db: Session= Depends(get_db)):
    # print ("payload", payload.dict())
    
    email = db.query(UserModel).filter(UserModel.email == payload.email).first()
    
    if email:
        raise HTTPException(status_code=400, detail=f"{payload.email} already exists ")
    # res:UsersInDb = UserModel(**dict())
    
    res:UsersInDb = UserModel(first_name=payload.first_name, last_name=payload.last_name, email=payload.email)
    db.add(res)
    db.commit()
    return res


@user_router.put("/{userID}",
summary="update a user",
status_code=200
)
def users_put(userID:int, payload:UserPut,  db:Session= Depends(get_db)):
    item = db.query(UserModel).filter(UserModel.id == userID).first()
    
    if not item:
        raise HTTPException(status_code=401, detail=f"{userID} doesn't exists ")
    
    item.first_name = payload.first_name
    item.last_name= payload.last_name,
    item.email= payload.email
    
    db.add(item)
    db.commit()
    return {"message":"item updated successfully"}



@user_router.delete("/{userID}",
response_model=Dict[str,str],
summary="delete a user",
status_code=200
)
def user_delete(userID:int,  db:Session= Depends(get_db)):
    pay = db.query(UserModel).filter(UserModel.id == userID).first()
    db.delete(pay)
    db.commit()
    return {"response":"item deleted successfully from db"}