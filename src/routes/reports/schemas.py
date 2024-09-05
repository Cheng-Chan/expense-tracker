import uuid

from typing import Optional
from decimal import Decimal
from datetime import datetime
from pydantic import BaseModel

from src.routes.users.schemas import User
from src.routes.categories.schemas import Category

class TransactionBase(BaseModel):
    amount: Decimal
    currency: str
    description: Optional[str] = None
    transaction_date: datetime

class Transaction(TransactionBase):
    id: uuid.UUID
    user: User
    categories: Category

    class Config:
        orm_mode = True