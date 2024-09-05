from decimal import Decimal

from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from . import models, schemas

def get_transactions(db: Session):
  transactions = db.query(models.Transaction).all()
  return transactions

def get_transaction(transaction_id: str, db: Session):
  transaction = db.query(models.Transaction).\
    filter(models.Transaction.id == transaction_id).first()
  
  if not transaction:
    raise HTTPException(
      status_code=404,
      detail="Category id not found"
    )
  
  return transaction

def get_transaction_by_id(transaction_id: str, db: Session):
  transaction = db.query(models.Transaction).\
    filter(models.Transaction.id == transaction_id).first()
  
  if not transaction:
    raise HTTPException(
      status_code=404,
      detail="Transaction id not found"
    )
  
  return transaction

def get_transactions_by_user_id(user_id: str, db: Session):
  transactions = db.query(models.Transaction).\
    filter(models.Transaction.user_id == user_id).all()
  
  if not transactions:
    raise HTTPException(
      status_code=404,
      detail="User id not found"
    )
  
  return transactions

def get_transactions_by_category_id(category_id: str, db: Session):
  transactions = db.query(models.Transaction).\
    filter(models.Transaction.category_id == category_id).all()
  
  if not transactions:
    raise HTTPException(
      status_code=404,
      detail="Category id not found"
    )
  
  return transactions

def create_transaction_in_db(transaction: schemas.TransactionCreate, db: Session):
  transaction = models.Transaction(
    user_id=transaction.user_id, 
    category_id=transaction.category_id, 
    description=transaction.description,
    currency=transaction.currency,
    amount=Decimal(transaction.amount)
  )
  db.add(transaction)
  db.commit()
  db.refresh(transaction)
  return transaction

def delete_transaction_by_id(transaction_id: str, db: Session):
  transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()

  if transaction is None:
    raise HTTPException(status_code=404, detail="Category not found")
  
  try:
    db.delete(transaction)
    db.commit()
    return {"detail": "Transaction deleted"}
  except SQLAlchemyError as e:
    db.rollback()
    raise HTTPException(status_code=500, detail=str(e))
  
def update_transaction_by_id(transaction_id: str, transaction: schemas.TransactionUpdate, db: Session):
  transaction_db = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()

  if not transaction_db:
    raise HTTPException(status_code=404, detail="Transaction not found")
  
  transaction_db.amount = Decimal(transaction.amount)
  transaction_db.description = transaction.description
  transaction_db.currency = transaction.currency

  try:
    db.commit()
    db.refresh(transaction_db)
    return transaction_db
  except SQLAlchemyError as e:
    db.rollback()
    raise HTTPException(status_code=500, detail=str(e))