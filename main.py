from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from src.config.database import engine
from src.config.config import APP_NAME, VERSION

from src.routes import users, categories, transactions, reports

from src.routes.users import models, main
from src.routes.categories import models, main
from src.routes.transactions import models, main
from src.routes.reports import main

users.models.Base.metadata.create_all(bind=engine)
categories.models.Base.metadata.create_all(bind=engine)
transactions.models.Base.metadata.create_all(bind=engine)

app = FastAPI(
  title=APP_NAME,
  version=VERSION
)

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_methods=["*"],
  allow_headers=["*"],
  allow_credentials=True,
)

app.include_router(users.main.router)
app.include_router(categories.main.router)
app.include_router(transactions.main.router)
app.include_router(reports.main.router)

@app.get("/")
def docs():
  """
  Redirect to documentation (`/docs/`)
  """
  return RedirectResponse(url="/docs/")