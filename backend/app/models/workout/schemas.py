from typing import Optional, Generic, TypeVar
from pydantic import BaseModel
from datetime import datetime
T = TypeVar('T')


class RequestWorkout(BaseModel):
    workout_id: int
    user_id: int
    workout_date: datetime
    notes: str



class ResponseWorkout(BaseModel, Generic[T]):
    is_success: bool
    message: str
    result: Optional[T] = None
