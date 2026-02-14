from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from models import User
from auth import register_user, login_user, get_current_user, update_user, delete_user
from schemas import UserCreate, UserLogin, UserUpdate, UserResponse

# инициализация FastAPI
app = FastAPI(title="Auth System")

# таблицы в базе данных
Base.metadata.create_all(bind=engine)


# эндпоинты

@app.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    """Регистрация нового пользователя"""
    return register_user(db, user.first_name, user.last_name, user.email, user.password)


@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    """Логин пользователя"""
    return login_user(db, user.email, user.password)


@app.get("/me", response_model=UserResponse)
def read_profile(current_user: User = Depends(get_current_user)):
    """Получить профиль текущего пользователя"""
    return current_user


@app.put("/update", response_model=UserResponse)
def update_profile(
    user_update: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    #обновление данных текущего пользователя
    return update_user(
        db,
        current_user,
        user_update.first_name,
        user_update.last_name,
        user_update.password
    )


@app.delete("/delete")
def delete_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    #мягкое удаление текущего пользователя
    return delete_user(db, current_user)

