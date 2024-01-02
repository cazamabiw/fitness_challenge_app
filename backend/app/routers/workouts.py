from fastapi import APIRouter, HTTPException, Depends
from ..auth.auth_bearer import JWTBearer
from ..config import SessionLocal
from sqlalchemy.orm import Session
from datetime import datetime
from ..models.workout.schemas import RequestWorkout
from ..services.workout_service import (
    get_workouts_by_date_range_and_user,
    get_workouts_by_user,
    update_workout,
    create_workout,
    delete_workout
)
router = APIRouter(
    prefix="/workouts",
    tags=["workouts"],
    dependencies=[Depends(JWTBearer())],
    responses={404: {"description": "Not found"}},
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/get_workouts_by_user/")
def get_workouts_by_user_endpoint(skip: int, limit: int, user_id: int, db: Session = Depends(get_db)):
    _workouts = get_workouts_by_user(db, skip=skip, limit=limit, user_id=user_id)
    if len(_workouts) == 0:
        raise HTTPException(status_code=404, detail="Workout not found")
    return _workouts


@router.get("/get_workouts_by_date_range_and_user/")
def get_workouts_by_date_range_and_user_endpoint(user_id: int, start_date: datetime, end_date: datetime, db: Session = Depends(get_db)):
    _workouts = get_workouts_by_date_range_and_user(db, user_id=user_id, start_date=start_date, end_date=end_date)
    if len(_workouts) == 0:
        raise HTTPException(status_code=404, detail="Workout not found")
    return _workouts


@router.post("/")
async def create_workout_endpoint(request: RequestWorkout, db: Session = Depends(get_db)):
    _workout = create_workout(db, workout=request)
    return _workout


@router.put("/{workout_id}")
def update_workout_endpoint(request: RequestWorkout, db: Session = Depends(get_db)):
    _workout = update_workout(db, workout=request)
    if _workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    return _workout


@router.delete("/{workout_id}")
def delete_workout_endpoint(workout_id: int, db: Session = Depends(get_db)):
    _workout = delete_workout(db, workout_id)
    if _workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    return _workout
