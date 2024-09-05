from fastapi import APIRouter, Depends

from src.utils.db_dependency import get_db
from . import schemas, controller

router = APIRouter(
  prefix="/transactions",
  tags=["Transaction"],
  responses={404: {"description": "Page not found"}},
)

@router.get("/", response_model=list[schemas.Transaction])
async def get_all_transactions(db: controller.Session = Depends(get_db)):
  return controller.get_transactions(db=db)

@router.get("/{transaction_id}", response_model=schemas.Transaction)
def get_transaction(transaction_id: str, db: controller.Session = Depends(get_db)):
    return controller.get_transaction_by_id(transaction_id=transaction_id, db=db)

@router.get("/user/{user_id}", response_model=list[schemas.Transaction])
def get_transactions_by_user(user_id: str, db: controller.Session = Depends(get_db)):
    return controller.get_transactions_by_user_id(user_id=user_id, db=db)

@router.get("/category/{category_id}", response_model=list[schemas.Transaction])
def get_transaction_by_category_id(category_id: str, db: controller.Session = Depends(get_db)):
    return controller.get_transactions_by_category_id(category_id=category_id, db=db)

@router.post("/", response_model=schemas.Transaction)
def create_transaction(transaction: schemas.TransactionCreate, db: controller.Session = Depends(get_db)):
    return controller.create_transaction_in_db(transaction=transaction, db=db)

@router.delete("/{transaction_id}", response_model=dict)
def delete_category(transaction_id: str, db: controller.Session = Depends(get_db)):
    return controller.delete_transaction_by_id(transaction_id=transaction_id, db=db)

@router.put("/{transaction_id}", response_model=schemas.Transaction)
def update_category(transaction_id: str, transaction: schemas.TransactionUpdate, db: controller.Session = Depends(get_db)):
    return controller.update_transaction_by_id(transaction_id=transaction_id, transaction=transaction, db=db)