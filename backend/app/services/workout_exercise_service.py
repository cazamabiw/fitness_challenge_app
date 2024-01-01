from sqlalchemy.orm import Session
from app.models.workout_exercise.workout_exercise import WorkoutExercise
from app.models.workout_exercise.schemas import ResponseWorkoutExercise, RequestWorkoutExercise


def get_workout_exercise(db: Session, workout_id: int, exercise_id: int):
    return db.query(WorkoutExercise).filter(
        WorkoutExercise.workout_id == workout_id,
        WorkoutExercise.exercise_id == exercise_id
    ).first()


def get_workout_exercise_by_workout_id(db: Session, workout_id: int):
    return db.query(WorkoutExercise).filter(WorkoutExercise.workout_id == workout_id).all()


def create_workout_exercise(db: Session, workout_exercise: RequestWorkoutExercise):
    _workout_exercise = WorkoutExercise(workout_id=workout_exercise.workout_id,exercise_id=workout_exercise.exercise_id,sets=workout_exercise.sets,reps=workout_exercise.reps,weight_kg=workout_exercise.weight_kg,notes=workout_exercise.notes)
    db.add(_workout_exercise)
    db.commit()
    db.refresh(_workout_exercise)
    return ResponseWorkoutExercise(is_success=True, message="Create success!", result=workout_exercise)


def delete_workout_exercise(db: Session, workout_id: int,exercise_id: int):
    _workout_exercise = get_workout_exercise(db,workout_id,exercise_id)
    if _workout_exercise:
        db.delete(_workout_exercise)
        db.commit()
        return ResponseWorkoutExercise(is_success=True, message="Delete success!", result=f"Workout ID: {workout_id}, Exercise ID: {exercise_id}")
    else:
        return _workout_exercise


def update_workout_exercise(db: Session, workout_exercise: RequestWorkoutExercise):
    _workout_exercise = get_workout_exercise(db,workout_exercise.workout_id,workout_exercise.exercise_id)

    if _workout_exercise:
        for key, value in workout_exercise.model_dump(exclude_unset=True).items():
            setattr(_workout_exercise, key, value)

        db.commit()
        db.refresh(_workout_exercise)

        return ResponseWorkoutExercise(is_success=True, message="Update success!", result=workout_exercise)
    else:
        return _workout_exercise
