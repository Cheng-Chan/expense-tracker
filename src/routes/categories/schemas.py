from pydantic import BaseModel
import uuid

class CategoryBase(BaseModel):
  category_name: str
  description: str
  user_id: uuid.UUID

class Category(CategoryBase):
  id: uuid.UUID

  class Config:
    orm_mode = True

class CategoryCreate(CategoryBase):
  pass

class CategoryUpdate(CategoryBase):
  pass