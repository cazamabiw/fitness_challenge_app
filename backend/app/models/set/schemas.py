from typing import Optional, Generic, TypeVar
from pydantic import BaseModel

T = TypeVar('T')


class RequestSet(BaseModel):
    set_id: int
    workout_exercise_id: int
    reps: int
    weight_kg: float


class ResponseSet(BaseModel, Generic[T]):
    is_success: bool
    message: str
    result: Optional[T] = None
