from sqlalchemy import Column,Boolean,ForeignKey,Integer,String,DateTime
from sqlalchemy.orm import relationship
from database.session import Base
from datetime import datetime


class Notes(Base):
    __tablename__ = "notes"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String,nullable=False)
    created_At = Column(DateTime,default=datetime.now)
    
    