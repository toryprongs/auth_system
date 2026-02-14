from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
import jwt
from datetime import datetime, timedelta
from database import get_db
from models import User
from fastapi import Header

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# регистрация
def register_user(db: Session, first_name, last_name, email, password):
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Пользователь уже существует")
    hashed_password = bcrypt.hash(password)
    user = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=hashed_password
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# логин
def login_user(db: Session, email, password):
    user = db.query(User).filter(User.email == email, User.is_active==True).first()
    if not user or not bcrypt.verify(password, user.password):
        raise HTTPException(status_code=401, detail="Неверный email или пароль")
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"user_id": user.id, "exp": expire}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}

def get_current_user(
    db: Session = Depends(get_db),
    authorization: str = Header(None)
):
    if not authorization:
        raise HTTPException(status_code=401, detail="Токен не предоставлен")

    token = authorization.replace("Bearer ", "")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
    except:
        raise HTTPException(status_code=401, detail="Неверный токен")

    user = db.query(User).filter(User.id == user_id, User.is_active == True).first()
    if not user:
        raise HTTPException(status_code=401, detail="Пользователь не найден")

    return user


# обновление пользователя
def update_user(db: Session, user: User, first_name=None, last_name=None, password=None):
    if first_name: user.first_name = first_name
    if last_name: user.last_name = last_name
    if password: user.password = bcrypt.hash(password)
    db.commit()
    db.refresh(user)
    return user

# мягкое удаление
def delete_user(db: Session, user: User):
    user.is_active = False
    db.commit()
    return {"detail": "Пользователь удален"}

from fastapi import APIRouter

router = APIRouter()
