import uuid

from datetime import datetime
from sqlalchemy import Column, String, DECIMAL, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.config.database import Base

class Transaction(Base):
  __tablename__ = "transactions"
  __tableargs__ = {"schema": "expense"}

  id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False, index=True)
  amount = Column(DECIMAL(10,2), nullable=False)
  currency = Column(String(length=3), nullable=False, index=True)
  transaction_date = Column(TIMESTAMP, nullable=False, default=datetime.utcnow, index=True)
  description = Column(String(length=225))
  category_id = Column(UUID(as_uuid=True), ForeignKey("expense.categories.id"), nullable=False)
  user_id = Column(UUID(as_uuid=True), ForeignKey("expense.users.id"), nullable=False)

  user = relationship("User", back_populates="transactions")
  categories = relationship("Category", back_populates="transactions")