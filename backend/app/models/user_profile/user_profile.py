from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserProfile(Base):
    __tablename__ = "user_profiles"

    profile_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), unique=True)
    age = Column(Integer)
    weight_kg = Column(Float)
    height_cm = Column(Float)
    fitness_goals = Column(String)
    experience_level = Column(String)

    user = relationship("User", back_populates="profile")
