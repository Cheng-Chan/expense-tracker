from fastapi import APIRouter, Depends

from src.utils.db_dependency import get_db
from . import schemas, controller

router = APIRouter(
  prefix="/users",
  tags=["Users"],
  responses={404: {"description": "Page not found"}},
)

@router.get("/", response_model=list[schemas.User])
async def get_all_user(db: controller.Session = Depends(get_db)):
  return controller.get_users(db=db)

@router.get("/{user_id}", response_model=schemas.User)
def get_user(user_id: str, db: controller.Session = Depends(get_db)):
    return controller.get_user_by_id(user_id=user_id, db=db)

@router.post("/", response_model=schemas.User)
def add_user(user: schemas.UserCreate, db: controller.Session = Depends(get_db)):
    return controller.create_user_in_db(user=user, db=db)

@router.delete("/{user_id}", response_model=dict)
def delete_user(user_id: str, db: controller.Session = Depends(get_db)):
    return controller.delete_user_by_id(user_id=user_id, db=db)

@router.put("/{user_id}", response_model=schemas.User)
def update_user(user_id: str, user: schemas.UserUpdate, db: controller.Session = Depends(get_db)):
    return controller.update_user_by_id(user_id=user_id, user=user, db=db)