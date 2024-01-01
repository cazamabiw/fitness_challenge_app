from sqlalchemy import Column, Integer, Float, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from ..muscle.muscle import Muscle
Base = declarative_base()


class Exercise(Base):
    __tablename__ = "exercises"

    exercise_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
    description = Column(Text)
    muscle_id = Column(Integer, ForeignKey(Muscle.muscle_id))
    muscle = relationship(Muscle)
