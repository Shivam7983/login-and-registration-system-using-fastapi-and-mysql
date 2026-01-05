from sqlalchemy.orm import Session
from model import User
from schemas import UserSchema
from fastapi import HTTPException
# from sqlalchemy.exc import SQLAlchemyError
 
 
# Create a new user
def create_user(db: Session, user: UserSchema):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")
 
    new_user = User(name=user.name, email=user.email, password=user.password, age=user.age)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
 
 
def get_user_by_id(db: Session, user_id:int):
    return db.query(User).filter(User.id==user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def update_user(db: Session, user_id: int, user_data: UserSchema):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Update values
    user.name = user_data.name
    user.email = user_data.email
    user.password = user_data.password
    user.age = user_data.age

    db.commit()
    db.refresh(user)
    return user
def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}
