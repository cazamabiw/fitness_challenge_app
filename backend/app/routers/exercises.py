from fastapi import APIRouter, HTTPException, Depends
from ..auth.auth_bearer import JWTBearer
from ..config import SessionLocal
from sqlalchemy.orm import Session
from ..models.exercise.schemas import RequestExercise
from ..services.exercise_service import (
    get_exercise,
    get_all_exercises,
    get_exercise_by_muscle_id,
    update_exercise,
    create_exercise,
    delete_exercise,
    search_exercises_by_name
)
router = APIRouter(
    prefix="/exercises",
    tags=["exercises"],
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
def get_exercises_endpoint(skip: int, limit: int, db: Session = Depends(get_db)):
    _exercises = get_all_exercises(db, skip=skip, limit=limit)
    if len(_exercises) == 0:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return _exercises


@router.get("/{exercise_id}")
def get_exercise_endpoint(exercise_id: int, db: Session = Depends(get_db)):
    _exercise = get_exercise(db, exercise_id)
    if _exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return _exercise


@router.get("/get_exercise_by_muscle_id/{muscle_id}")
def get_exercise_by_muscle_id_endpoint(muscle_id: int, db: Session = Depends(get_db)):
    _exercises = get_exercise_by_muscle_id(db, muscle_id)
    if len(_exercises) == 0:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return _exercises


@router.get("/search_exercises_by_name/{query}")
def search_exercises_by_name_endpoint(query: str, db: Session = Depends(get_db)):
    _exercises = search_exercises_by_name(db, query)
    if len(_exercises) == 0:
        raise HTTPException(status_code=404, detail="Exercise not found.")
    return _exercises


@router.post("/")
async def create_exercise_endpoint(request: RequestExercise, db: Session = Depends(get_db)):
    _exercise = create_exercise(db, exercise=request)
    return _exercise


@router.put("/{exercise_id}")
def update_exercise_endpoint(request: RequestExercise, db: Session = Depends(get_db)):
    _exercise = update_exercise(db, exercise=request)
    if _exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return _exercise


@router.delete("/{exercise_id}")
def delete_exercise_endpoint(exercise_id: int, db: Session = Depends(get_db)):
    _exercise = delete_exercise(db, exercise_id)
    if _exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return _exercise
