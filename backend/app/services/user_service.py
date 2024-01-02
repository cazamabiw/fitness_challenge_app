from sqlalchemy.orm import Session
from app.models.user.user import User
from app.models.user.schemas import RequestUser, ResponseUser, RequestUserLogin
import bcrypt


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.user_id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: RequestUser):
    hashed_password = hash_password(user.password)
    _user = User(username=user.username, email=user.email, password_hash=hashed_password)
    db.add(_user)
    db.commit()
    db.refresh(_user)
    user.user_id = _user.user_id
    user.password = hashed_password
    return ResponseUser(is_success=True, message="Create success!", result=user)


def update_user(db: Session, user: RequestUser):
    _user = db.query(User).filter(User.user_id == user.user_id).first()
    if _user is None:
        return None
    _user.username = user.username
    _user.email = user.email

    if user.password:
        hashed_password = hash_password(user.password)
        _user.password_hash = hashed_password

    db.commit()
    db.refresh(_user)
    user.password = _user.password_hash
    return ResponseUser(is_success=True, message="Create success!", result=user)


def delete_user(db: Session, user_id: int):
    _user = db.query(User).filter(User.user_id == user_id).first()
    if _user:
        db.delete(_user)
        db.commit()
        return ResponseUser(is_success=True, message="Delete success!", result=user_id)
    else:
        return _user


def login_user(db: Session, user: RequestUserLogin):
    _current_user = get_user_by_username(db, user.username)
    if _current_user and verify_password(user.password, _current_user.password_hash):
        return _current_user
    return None


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


