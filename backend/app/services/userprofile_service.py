from sqlalchemy.orm import Session
from app.models.user_profile.user_profile import UserProfile
from app.models.user_profile.schemas import RequestUserProfile, ResponseUserProfile
def create_user_profile(db: Session, user_profile: RequestUserProfile):
    _user_profile = UserProfile(user_id=user_profile.user_id,age=user_profile.age,weight_kg=user_profile.weight_kg,height_cm=user_profile.height_cm,fitness_goals=user_profile.fitness_goals,experience_level=user_profile.experience_level)
    db.add(_user_profile)
    db.commit()
    db.refresh(_user_profile)
    return ResponseUserProfile(is_success=True, message="Create success!", result=user_profile)


def get_user_profile(db: Session, user_id: int):
    return db.query(UserProfile).filter(UserProfile.user_id == user_id).first()


def update_user_profile(db: Session, user_profile: RequestUserProfile):
    _user_profile = db.query(UserProfile).filter(UserProfile.user_id == user_profile.user_id).first()

    if _user_profile:
        for key, value in user_profile.model_dump(exclude_unset=True).items():
            setattr(_user_profile, key, value)

        db.commit()
        db.refresh(_user_profile)

    return ResponseUserProfile(is_success=True, message="Update success!", result=user_profile)
