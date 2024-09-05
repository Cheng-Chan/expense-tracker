from fastapi import HTTPException
from pydantic import EmailStr
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from . import models, schemas

def get_users(db: Session):
  users = db.query(models.User).all()
  return users

def get_user_by_id(user_id: str, db: Session):
  user = db.query(models.User).\
    filter(models.User.id == user_id).first()
  
  if not user:
    raise HTTPException(
      status_code=404,
      detail="User id not found"
    )
  
  return user

def create_user_in_db(user: schemas.UserCreate, db: Session):
  db_user = models.User(name=user.name, email=user.email, gender=user.gender)
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  return db_user

def delete_user_by_id(user_id: str, db: Session):
  user = db.query(models.User).filter(models.User.id == user_id).first()

  if user is None:
    raise HTTPException(status_code=404, detail="User not found")
  
  try:
    db.delete(user)
    db.commit()
    return {"detail": "User deleted"}
  except SQLAlchemyError as e:
    db.rollback()
    raise HTTPException(status_code=500, detail=str(e))
  
def update_user_by_id(user_id: str, user: schemas.UserUpdate, db: Session):
  user_db = db.query(models.User).filter(models.User.id == user_id).first()

  if not user_db:
    raise HTTPException(status_code=404, detail="User not found")
  
  user_db.name = user.name
  user_db.email = user.email
  user_db.gender = user.gender

  try:
    db.commit()
    db.refresh(user_db)
    return user_db
  except SQLAlchemyError as e:
    db.rollback()
    raise HTTPException(status_code=500, detail=str(e))