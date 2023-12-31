from sqlalchemy.orm import Session
from app.models.muscle.muscle import Muscle
from app.models.muscle.schemas import ResponseMuscle, RequestMuscle


def get_all_muscles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Muscle).offset(skip).limit(limit).all()


def get_muscle_by_id(db: Session, muscle_id: int):
    return db.query(Muscle).filter(Muscle.muscle_id == muscle_id).first()


def create_muscle(db: Session, muscle: RequestMuscle):
    _muscle = Muscle(name=muscle.name)
    db.add(_muscle)
    db.commit()
    db.refresh(_muscle)
    muscle.muscle_id = _muscle.muscle_id
    return ResponseMuscle(is_success=True, message="Create success!", result=muscle)


def delete_muscle(db: Session, muscle_id: int):
    _muscle = db.query(Muscle).filter(Muscle.muscle_id == muscle_id).first()
    if _muscle:
        db.delete(_muscle)
        db.commit()
        return ResponseMuscle(is_success=True, message="Delete success!", result=muscle_id)
    else:
        return _muscle


def update_muscle(db: Session, muscle: RequestMuscle):
    _muscle = db.query(Muscle).filter(Muscle.muscle_id == muscle.muscle_id).first()
    if _muscle:
        _muscle.name = muscle.name
        db.commit()
        db.refresh(_muscle)
        return ResponseMuscle(is_success=True, message="Update success!", result = muscle)
    else:
        return _muscle
