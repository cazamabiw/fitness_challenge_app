from fastapi import APIRouter, HTTPException, Depends
from ..auth.auth_bearer import JWTBearer
from ..config import SessionLocal
from sqlalchemy.orm import Session
from ..models.user_profile.schemas import ResponseUserProfile, RequestUserProfile
from ..services.userprofile_service import (
    create_user_profile,
    update_user_profile,
    get_user_profile
)
from ..services.user_service import (
    get_user
)
router = APIRouter(
    prefix="/userprofiles",
    tags=["userprofiles"],
    #dependencies=[Depends(JWTBearer())],
    responses={404: {"description": "Not found"}},
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_userprofile_endpoint(request:RequestUserProfile , db: Session = Depends(get_db)):
    _user = get_user(db,request.user_id)
    if _user is None:
        raise HTTPException(status_code=404, detail="User not found")

    existing_profile = get_user_profile(db, request.user_id)
    if existing_profile:
        raise HTTPException(status_code=400, detail="User profile already exists")

    return create_user_profile(db, request)

@router.get("/{user_id}")
def read_userprofile_endpoint(user_id: int, db: Session = Depends(get_db)):
    _user = get_user_profile(db, user_id)
    if _user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return _user

@router.put("/{user_id}")
def update_userprofile_endpoint(request: RequestUserProfile, db: Session = Depends(get_db)):
    _user = update_user_profile(db, request)
    if _user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return _user
