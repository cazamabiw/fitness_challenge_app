from sqlalchemy import Column, Integer, ForeignKey, Float, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from ..workout.workout import Workout
from ..exercise.exercise import Exercise

Base = declarative_base()


class WorkoutExercise(Base):
    __tablename__ = "workout_exercises"

    workout_exercise_id = Column(Integer, primary_key=True, index=True)
    workout_id = Column(Integer, ForeignKey(Workout.workout_id), nullable=False)
    exercise_id = Column(Integer, ForeignKey(Exercise.exercise_id), nullable=False)
    notes = Column(Text)

    workout = relationship(Workout)
    exercise = relationship(Exercise)
