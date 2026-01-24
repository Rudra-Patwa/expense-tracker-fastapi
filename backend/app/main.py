from fastapi import FastAPI
from backend.app.database import engine
from backend.app.models import Base
from backend.app.routes import expenses
from backend.app.core.logging import setup_logging
from backend.app.routes import expenses, analytics
import logging

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title="Expense Tracker API")

Base.metadata.create_all(bind=engine)

app.include_router(expenses.router)
app.include_router(analytics.router)

@app.get("/")
def health_check():
    logger.info("Health check endpoint called")
    return {"status": "Expense Tracker API running"}
