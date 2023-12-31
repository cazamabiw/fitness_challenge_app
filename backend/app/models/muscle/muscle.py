from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Muscle(Base):
    __tablename__ = "muscles"

    muscle_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
