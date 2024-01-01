from sqlalchemy import Column, Integer, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from ..user.user import User
Base = declarative_base()


class Workout(Base):

    __tablename__ = "workouts"

    workout_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.user_id))
    workout_date = Column(DateTime, nullable=False)
    notes = Column(Text)

    user = relationship(User)

