import uuid

from src.config.database import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

class User(Base):
  __tablename__ = "users"
  __table_args__ = {"schema": "expense"}

  id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False, index=True)
  name = Column(String(length=50), index=True)
  gender = Column(String(length=1))
  email = Column(String(length=75), index=True, unique=True)

  categories = relationship("Category", back_populates="user")
  transactions = relationship("Transaction", back_populates="user")