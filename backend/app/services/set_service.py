from sqlalchemy.orm import Session
from app.models.set.set import Set
from app.models.set.schemas import RequestSet,ResponseSet


def get_set(db: Session, set_id: int):
    return db.query(Set).filter(Set.set_id == set_id).first()


def get_sets_by_workout_exercise_id(db: Session, workout_exercise_id: int):
    return db.query(Set).filter(
        Set.workout_exercise_id == workout_exercise_id
    ).all()


def create_set(db: Session, set: RequestSet):
    _set = Set(workout_exercise_id=set.workout_exercise_id,reps=set.reps, weight_kg=set.weight_kg)
    db.add(_set)
    db.commit()
    db.refresh(_set)
    Set.set_id = _set.set_id
    return ResponseSet(is_success=True, message="Create success!", result=set)


def delete_set(db: Session, set_id: int):
    _set = get_set(db,set_id)
    if _set:
        db.delete(_set)
        db.commit()
        return ResponseSet(is_success=True, message="Delete success!", result=set_id)
    else:
        return _set


def update_set(db: Session, set: RequestSet):
    _set = get_set(db, set.set_id)

    if _set:
        for key, value in set.model_dump(exclude_unset=True).items():
            setattr(_set, key, value)

        db.commit()
        db.refresh(_set)

        return ResponseSet(is_success=True, message="Update success!", result=set)
    else:
        return _set


