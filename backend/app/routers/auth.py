from fastapi import APIRouter, Body

from app.auth.auth_handler import signJWT
from app.models.auth import UserLoginToken

router = APIRouter()

def check_user(data: UserLoginToken):
    if data.username == "testuser" and data.password == "testpassword":
        return True
    return False

@router.post("/token")
def user_login(user: UserLoginToken = Body(...)):
    if check_user(user):
        return signJWT(user.username)
    return {
        "error": "Wrong login details!"
    }