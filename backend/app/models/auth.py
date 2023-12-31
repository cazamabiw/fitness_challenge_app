from pydantic import BaseModel, Field
class UserLoginToken(BaseModel):
    username: str = Field(...)
    password: str = Field(...)
