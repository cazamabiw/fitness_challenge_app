from fastapi import APIRouter, HTTPException, Depends

from ..auth.auth_bearer import JWTBearer
from ..config import SessionLocal
from sqlalchemy.orm import Session
from ..models.muscle.schemas import RequestMuscle
from ..services.muscle_service import (
    get_all_muscles,
    get_muscle_by_id,
    create_muscle,
    delete_muscle,
    update_muscle
)
router = APIRouter(
    prefix="/muscles",
    tags=["muscles"],
    dependencies=[Depends(JWTBearer())],
    responses={404: {"description": "Not found"}},
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_muscles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_muscles(db, skip=skip, limit=limit)

@router.get("/{muscle_id}")
def get_muscle(muscle_id: int, db: Session = Depends(get_db)):
    muscle = get_muscle_by_id(db, muscle_id)
    if muscle is None:
        raise HTTPException(status_code=404, detail="Muscle not found")
    return muscle

@router.post("/")
async def create_muscle_endpoint(request: RequestMuscle, db: Session = Depends(get_db)):
    _muscle = create_muscle(db, muscle=request)
    return _muscle


@router.put("/{muscle_id}")
def update_muscle_endpoint(request: RequestMuscle, db: Session = Depends(get_db)):
    _muscle = update_muscle(db, muscle=request)
    if _muscle is None:
        raise HTTPException(status_code=404, detail="Muscle not found")
    return _muscle


@router.delete("/{muscle_id}")
def delete_muscle_endpoint(muscle_id: int, db: Session = Depends(get_db)):
    _muscle = delete_muscle(db, muscle_id)
    if _muscle is None:
        raise HTTPException(status_code=404, detail="Muscle not found")
    return _muscle
