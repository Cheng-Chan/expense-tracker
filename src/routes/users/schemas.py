import uuid

from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    gender: str
    email: EmailStr

class User(UserBase):
    id: uuid.UUID | None = None

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    pass 

class UserUpdate(UserBase):
    pass