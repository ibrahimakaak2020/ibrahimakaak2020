from core.hashing import Hasher
from db.models.models import User
from db.schemas.schemas import UserCreate
from sqlalchemy.orm import Session


def create_new_user(user: UserCreate, db: Session):
    user = User(
        staffno=user.staffno,
        staffname=user.staffname,
        password=Hasher.get_password_hash(user.password),
        admin_role=1
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_staffno(staffno: str, db: Session):
    user = db.query(User).filter(User.staffno == staffno).first()
    return user


def get_users( db: Session):
    users = db.query(User).all()
    return users