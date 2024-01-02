from fastapi import APIRouter, HTTPException, Depends
from ..auth.auth_bearer import JWTBearer
from ..config import SessionLocal
from sqlalchemy.orm import Session
from ..models.workout_exercise.schemas import RequestWorkoutExercise
from ..services.workout_exercise_service import (
    get_workout_exercises_by_workout_id,
    create_workout_exercise,
    delete_workout_exercise,
    update_workout_exercise
)
router = APIRouter(
    prefix="/workout_exercises",
    tags=["workout_exercises"],
    #dependencies=[Depends(JWTBearer())],
    responses={404: {"description": "Not found"}},
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/get_workout_exercise_by_workout_id/{workout_id}")
def get_workout_exercise_by_workout_id_endpoint(workout_id: int, db: Session = Depends(get_db)):
    _workout_exercises = get_workout_exercises_by_workout_id(db, workout_id)
    if len(_workout_exercises) == 0:
        raise HTTPException(status_code=404, detail="Workout Exercise not found")
    return _workout_exercises


@router.post("/")
async def create_workout_exercise_endpoint(request: RequestWorkoutExercise, db: Session = Depends(get_db)):
    _workout_exercise = create_workout_exercise(db, workout_exercise=request)
    return _workout_exercise


@router.put("/{workout_exercise_id}")
def update_workout_exercise_endpoint(request: RequestWorkoutExercise, db: Session = Depends(get_db)):
    _workout_exercise = update_workout_exercise(db, workout_exercise=request)
    if _workout_exercise is None:
        raise HTTPException(status_code=404, detail="Workout Exercise not found")
    return _workout_exercise


@router.delete("/{workout_exercise_id}")
def delete_workout_exercise_endpoint(workout_exercise_id: int, db: Session = Depends(get_db)):
    _workout_exercise = delete_workout_exercise(db, workout_exercise_id)
    if _workout_exercise is None:
        raise HTTPException(status_code=404, detail="Workout Exercise not found")
    return _workout_exercise
