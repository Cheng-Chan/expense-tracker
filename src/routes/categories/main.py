from fastapi import APIRouter, Depends

from src.utils.db_dependency import get_db
from . import schemas, controller

router = APIRouter(
  prefix="/categories",
  tags=["Categories"],
  responses={404: {"description": "Page not found"}},
)

@router.get("/", response_model=list[schemas.Category])
async def get_all_category(db: controller.Session = Depends(get_db)):
  return controller.get_categories(db=db)

@router.get("/{category_id}", response_model=schemas.Category)
def get_category(category_id: str, db: controller.Session = Depends(get_db)):
    return controller.get_categories_by_id(category_id=category_id, db=db)

@router.get("/user/{user_id}", response_model=list[schemas.Category])
def get_category_by_user(user_id: str, db: controller.Session = Depends(get_db)):
    return controller.get_categories_by_user_id(user_id=user_id, db=db)

@router.post("/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: controller.Session = Depends(get_db)):
    return controller.create_category_in_db(category=category, db=db)

@router.delete("/{category_id}", response_model=dict)
def delete_category(category_id: str, db: controller.Session = Depends(get_db)):
    return controller.delete_category_by_id(category_id=category_id, db=db)

@router.put("/{category_id}", response_model=schemas.Category)
def update_category(category_id: str, category: schemas.CategoryUpdate, db: controller.Session = Depends(get_db)):
    return controller.update_category_by_id(category_id=category_id, category=category, db=db)
