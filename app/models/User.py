from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = "users"


    # Define Primary Key
    id = Column(Integer, primary_key=True, index=True)


    # Authentication
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = ()
