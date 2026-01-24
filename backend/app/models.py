from sqlalchemy import Column, Integer, String, Date, DECIMAL, TIMESTAMP
from sqlalchemy.sql import func
from backend.app.database import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(DECIMAL(10, 2), nullable=False)
    category = Column(String(50), nullable=False)
    description = Column(String(255))
    expense_date = Column(Date, nullable=False)
    payment_mode = Column(String(30))
    created_at = Column(TIMESTAMP, server_default=func.now())
