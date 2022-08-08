from sqlalchemy import Column, Integer, String, DateTime,Text, Boolean,func,ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base


class TodoModel(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title =Column(String, unique=True, nullable=False)
    description = Column(Text, nullable=False )
    completed = Column(Boolean,default=False )
    created = Column(DateTime(timezone=True), server_default=func.now())
    
    user = relationship("UserModel", back_populates="todos")