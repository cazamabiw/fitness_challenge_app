from fastapi import APIRouter, HTTPException, Depends
from ..auth.auth_bearer import JWTBearer
from ..config import SessionLocal
from sqlalchemy.orm import Session
from ..models.user.schemas import RequestUser, RequestUserLogin
from ..services.user_service import (
    create_user,
    login_user,
    get_user_by_username,
    update_user,
    delete_user,
    get_user
)
router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(JWTBearer())],
    responses={404: {"description": "Not found"}},
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_user_endpoint(request: RequestUser, db: Session = Depends(get_db)):
    user = get_user_by_username(db, request.username)
    if user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_user(db, user=request)

@router.get("/{user_id}")
def read_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}")
def update_user_endpoint(request: RequestUser, db: Session = Depends(get_db)):
    user = update_user(db,request)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}")
def delete_muscle_endpoint(user_id: int, db: Session = Depends(get_db)):
    _muscle = delete_user(db, user_id)
    if _muscle is None:
        raise HTTPException(status_code=404, detail="User not found")
    return _muscle

@router.post("/login/")
def login_user_endpoint(request: RequestUserLogin, db: Session = Depends(get_db)):
    user = login_user(db, user=request)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid username or password!")
    return user
