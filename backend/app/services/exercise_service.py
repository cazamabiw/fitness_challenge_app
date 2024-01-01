from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.exercise.exercise import Exercise

from app.models.exercise.schemas import RequestExercise, ResponseExercise


def get_all_exercises(db: Session, skip: int, limit: int):
    return db.query(Exercise).offset(skip).limit(limit).all()


def get_exercise(db: Session, exercise_id: int):
    return db.query(Exercise).filter(Exercise.exercise_id == exercise_id).first()


def get_exercise_by_muscle_id(db: Session, muscle_id: int):
    return db.query(Exercise).filter(Exercise.muscle_id == muscle_id).all()


def search_exercises_by_name(db: Session, search_term: str):
    return db.query(Exercise).filter(func.lower(Exercise.name).contains(func.lower(search_term))).all()


def create_exercise(db: Session, exercise: RequestExercise):
    _exercise = Exercise(name=exercise.name,description=exercise.description,muscle_id=exercise.muscle_id)
    db.add(_exercise)
    db.commit()
    db.refresh(_exercise)
    exercise.exercise_id = _exercise.exercise_id
    return ResponseExercise(is_success=True, message="Create success!", result=exercise)


def delete_exercise(db: Session, exercise_id: int):
    _exercise = db.query(Exercise).filter(Exercise.exercise_id == exercise_id).first()
    if _exercise:
        db.delete(_exercise)
        db.commit()
        return ResponseExercise(is_success=True, message="Delete success!", result=exercise_id)
    else:
        return _exercise


def update_exercise(db: Session, exercise: RequestExercise):
    _exercise = db.query(Exercise).filter(Exercise.exercise_id == exercise.exercise_id).first()

    if _exercise:
        for key, value in exercise.model_dump(exclude_unset=True).items():
            setattr(_exercise, key, value)

        db.commit()
        db.refresh(_exercise)

        return ResponseExercise(is_success=True, message="Update success!", result=exercise)
    else:
        return _exercise


