from fastapi import APIRouter, HTTPException, Depends
from ..auth.auth_bearer import JWTBearer
from ..config import SessionLocal
from sqlalchemy.orm import Session
from ..models.set.schemas import RequestSet
from ..services.set_service import (
    get_sets_by_workout_exercise_id,
    create_set,
    delete_set,
    update_set
)
router = APIRouter(
    prefix="/sets",
    tags=["sets"],
    #dependencies=[Depends(JWTBearer())],
    responses={404: {"description": "Not found"}},
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/get_sets_by_workout_exercise_id/{workout_exercise_id}")
def get_sets_by_workout_exercise_id_endpoint(workout_exercise_id: int, db: Session = Depends(get_db)):
    _sets = get_sets_by_workout_exercise_id(db, workout_exercise_id)
    if len(_sets) == 0:
        raise HTTPException(status_code=404, detail="Sets not found")
    return _sets


@router.post("/")
async def create_set_endpoint(request: RequestSet, db: Session = Depends(get_db)):
    _set = create_set(db, set=request)
    return _set


@router.put("/{set_id}")
def update_set_endpoint(request: RequestSet, db: Session = Depends(get_db)):
    _set = update_set(db, set=request)
    if _set is None:
        raise HTTPException(status_code=404, detail="Set not found")
    return _set


@router.delete("/{set_id}")
def delete_set_endpoint(set_id: int, db: Session = Depends(get_db)):
    _set = delete_set(db, set_id)
    if _set is None:
        raise HTTPException(status_code=404, detail="Set not found")
    return _set
