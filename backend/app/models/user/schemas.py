from typing import Optional, Generic, TypeVar
from pydantic import BaseModel

T = TypeVar('T')

class UserSchema(BaseModel):
    user_id: Optional[int] = None
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

    class Config:
        from_attributes = True

class RequestUser(BaseModel):
    user_id: int
    username: str
    password: str
    email: str

class ResponseUser(BaseModel, Generic[T]):
    is_success: bool
    message: str
    result: Optional[T] = None

class RequestUserLogin(BaseModel):
    username: str
    password: str


