import uuid

from typing import Optional
from decimal import Decimal
from datetime import datetime
from pydantic import BaseModel

class TransactionBase(BaseModel):
  amount: Decimal
  currency: str
  transaction_date: datetime
  description: str
  user_id: uuid.UUID
  category_id: uuid.UUID

class Transaction(TransactionBase):
  id: uuid.UUID

  class Config:
    orm_mode = True

class TransactionCreate(TransactionBase):
  pass

class TransactionUpdate(BaseModel):
  amount: Optional[Decimal] = None
  currency: Optional[str] = None
  description: Optional[str] = None