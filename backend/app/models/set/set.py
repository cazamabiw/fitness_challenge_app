from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from ..workout_exercise.workout_exercise import WorkoutExercise

Base = declarative_base()


class Set(Base):
    __tablename__ = "sets"

    set_id = Column(Integer, primary_key=True, index=True)
    workout_exercise_id = Column(Integer, ForeignKey(WorkoutExercise.workout_exercise_id), nullable=False)
    reps = Column(Integer, nullable=False)
    weight_kg = Column(Float)

    workout_exercise = relationship(WorkoutExercise)
