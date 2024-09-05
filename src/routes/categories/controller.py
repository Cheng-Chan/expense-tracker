from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from . import models, schemas

def get_categories(db: Session):
  categories = db.query(models.Category).all()
  return categories

def get_categories_by_id(category_id: str, db: Session):
  category = db.query(models.Category).\
    filter(models.Category.id == category_id).first()
  
  if not category:
    raise HTTPException(
      status_code=404,
      detail="Category id not found"
    )
  
  return category

def get_categories_by_user_id(user_id: str, db: Session):
  categories = db.query(models.Category).\
    filter(models.Category.user_id == user_id).all()
  
  if not categories:
    raise HTTPException(
      status_code=404,
      detail="User id not found"
    )
  
  return categories

def create_category_in_db(category: schemas.CategoryCreate, db: Session):
  category = models.Category(
    user_id=category.user_id, 
    category_name=category.category_name, 
    description=category.description
  )
  db.add(category)
  db.commit()
  db.refresh(category)
  return category

def delete_category_by_id(category_id: str, db: Session):
  category = db.query(models.Category).filter(models.Category.id == category_id).first()

  if category is None:
    raise HTTPException(status_code=404, detail="Category not found")
  
  try:
    db.delete(category)
    db.commit()
    return {"detail": "Category deleted"}
  except SQLAlchemyError as e:
    db.rollback()
    raise HTTPException(status_code=500, detail=str(e))
  
def update_category_by_id(category_id: str, category: schemas.CategoryUpdate, db: Session):
  category_db = db.query(models.Category).filter(models.Category.id == category_id).first()

  if not category_db:
    raise HTTPException(status_code=404, detail="User not found")
  
  category_db.category_name = category.category_name
  category_db.description = category.description

  try:
    db.commit()
    db.refresh(category_db)
    return category_db
  except SQLAlchemyError as e:
    db.rollback()
    raise HTTPException(status_code=500, detail=str(e))