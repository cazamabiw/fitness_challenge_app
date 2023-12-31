from typing import Optional, Generic, TypeVar
from pydantic import BaseModel, Field

T = TypeVar('T')

class MuscleSchema(BaseModel):
    muscle_id: Optional[int] = None
    name: Optional[str] = None

    class Config:
        from_attributes = True

class RequestMuscle(BaseModel):
    muscle_id: str
    name: str

class ResponseMuscle(BaseModel, Generic[T]):
    is_success: bool
    message: str
    result: Optional[T] = None

