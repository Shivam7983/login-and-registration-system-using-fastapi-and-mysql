from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import Base, engine, SessionLocal
from schemas import UserSchema, UserUpdateSchema
from crud import create_user, get_user_by_id, update_user, delete_user
from typing import List

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users", response_model=UserSchema)
def create_user_in_db(user: UserSchema, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

@app.get("/users/{user_id}", response_model=UserSchema)
def get_user_by_userid(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db=db, user_id=user_id)
    return user

@app.put("/users/{user_id}", response_model=UserSchema)
def update_user_in_db(user_id: int, user_data: UserUpdateSchema, db: Session = Depends(get_db)):
    user = get_user_by_id(db=db, user_id=user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    updated_user = update_user(db=db, user=user, user_data=user_data)
    return updated_user

@app.delete("/users/{user_id}")
def delete_user_in_db(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db=db, user_id=user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    delete_user(db=db, user=user)

    return {"message": f"User with id {user_id} deleted successfully"}