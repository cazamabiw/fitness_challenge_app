from typing import Optional, Generic, TypeVar
from pydantic import BaseModel

T = TypeVar('T')


class RequestUserProfile(BaseModel):
    user_id: int
    age: int
    weight_kg: float
    height_cm: float
    fitness_goals: str
    experience_level: str


class ResponseUserProfile(BaseModel, Generic[T]):
    is_success: bool
    message: str
    result: Optional[T] = None
