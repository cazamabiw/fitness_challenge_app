from typing import Optional, Generic, TypeVar
from pydantic import BaseModel

T = TypeVar('T')


class RequestWorkoutExercise(BaseModel):
    workout_id: int
    exercise_id: int
    sets: int
    reps: int
    weight_kg: float
    notes: str


class ResponseWorkoutExercise(BaseModel, Generic[T]):
    is_success: bool
    message: str
    result: Optional[T] = None