from sqlalchemy import Column, Integer, ForeignKey, Float, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from ..workout.workout import Workout
from ..exercise.exercise import Exercise

Base = declarative_base()


class WorkoutExercise(Base):
    __tablename__ = "workout_exercises"

    workout_id = Column(Integer, ForeignKey(Workout.workout_id), primary_key=True)
    exercise_id = Column(Integer, ForeignKey(Exercise.exercise_id), primary_key=True)
    sets = Column(Integer, nullable=False)
    reps = Column(Integer, nullable=False)
    weight_kg = Column(Float)
    notes = Column(Text)

    workout = relationship(Workout)
    exercise = relationship(Exercise)
