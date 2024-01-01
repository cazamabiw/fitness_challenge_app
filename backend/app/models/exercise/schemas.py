from typing import Optional, Generic, TypeVar
from pydantic import BaseModel

T = TypeVar('T')


class RequestExercise(BaseModel):
    exercise_id: int
    name: str
    description: str
    muscle_id: int


class ResponseExercise(BaseModel, Generic[T]):
    is_success: bool
    message: str
    result: Optional[T] = None
