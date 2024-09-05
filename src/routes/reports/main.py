from fastapi import APIRouter, Depends

from src.utils.db_dependency import get_db
from . import schemas, controller

router = APIRouter(
  prefix="/reports",
  tags=["reports"],
  responses={404: {"description": "Page not found"}},
)

@router.get("/transactions", response_model=list[schemas.Transaction])
async def get_transactions(db: controller.Session = Depends(get_db)):
  return controller.get_transactions(db=db)