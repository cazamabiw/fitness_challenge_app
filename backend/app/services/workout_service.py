from sqlalchemy.orm import Session
from datetime import datetime
from app.models.workout.workout import Workout

from app.models.workout.schemas import ResponseWorkout, RequestWorkout


def get_workouts_by_user(db: Session, skip: int, limit: int, user_id: int):
    return db.query(Workout).filter(Workout.user_id == user_id).order_by(Workout.workout_date.desc()).offset(skip).limit(limit).all()


def get_workout(db: Session, workout_id: int):
    return db.query(Workout).filter(Workout.workout_id == workout_id).first()


def get_workouts_by_date_range_and_user(db: Session, user_id: int, start_date: datetime, end_date: datetime):
    return db.query(Workout).filter(
        Workout.user_id == user_id,
        Workout.workout_date >= start_date,
        Workout.workout_date <= end_date
    ).order_by(Workout.workout_date.desc()).all()


def create_workout(db: Session, workout: RequestWorkout):
    _workout = Workout(user_id=workout.user_id,workout_date=workout.workout_date,notes=workout.notes)
    db.add(_workout)
    db.commit()
    db.refresh(_workout)
    workout.workout_id = _workout.workout_id
    return ResponseWorkout(is_success=True, message="Create success!", result=workout)


def delete_workout(db: Session, workout_id: int):
    _workout = db.query(Workout).filter(Workout.workout_id == workout_id).first()
    if _workout:
        db.delete(_workout)
        db.commit()
        return ResponseWorkout(is_success=True, message="Delete success!", result=workout_id)
    else:
        return _workout


def update_workout(db: Session, workout: RequestWorkout):
    _workout = db.query(Workout).filter(Workout.workout_id == workout.workout_id).first()

    if _workout:
        for key, value in workout.model_dump(exclude_unset=True).items():
            setattr(_workout, key, value)

        db.commit()
        db.refresh(_workout)

        return ResponseWorkout(is_success=True, message="Update success!", result=workout)
    else:
        return _workout

