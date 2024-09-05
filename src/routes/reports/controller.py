from sqlalchemy import select
from sqlalchemy.orm import selectinload, Session

from src.routes.categories import models as category_models
from src.routes.users import models as user_models
from src.routes.transactions import models as transaction_models


def get_transactions(db: Session):
  query = (
    select(transaction_models.Transaction)
    .join(user_models.User)
    .join(category_models.Category)
    .options(selectinload(transaction_models.Transaction.user))
    .options(selectinload(transaction_models.Transaction.categories))
  )
  result = db.execute(query).scalars().all()
  return result