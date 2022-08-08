from sqlalchemy import Column, Integer, String, DateTime,Text, Boolean,func
from db.base_class import Base
from sqlalchemy.orm import relationship


class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name =Column(String, nullable=False)
    last_name =Column(String, nullable=False)
    email =Column(String, unique=True, nullable=False)
    created = Column(DateTime(timezone=True), server_default=func.now())
    
    todos = relationship("TodoModel", back_populates="user")
    
    