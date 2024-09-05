import uuid

from src.config.database import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

class Category(Base):
  __tablename__ = "categories"
  __table_args__ = {"schema": "expense"}

  id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False, index=True)
  category_name = Column(String(length=50))
  description = Column(String(length=225))
  user_id = Column(UUID(as_uuid=True), ForeignKey("expense.users.id"), nullable=False)

  user = relationship("User", back_populates="categories")
  transactions = relationship("Transaction", back_populates="categories")