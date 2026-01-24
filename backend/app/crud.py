from sqlalchemy.orm import Session
from .models import Expense
from datetime import date
import logging
logger = logging.getLogger(__name__)

def create_expense(
    db: Session,
    amount: float,
    category: str,
    description: str,
    expense_date: date,
    payment_mode: str
):

    expense = Expense(
        amount=amount,
        category=category,
        description=description,
        expense_date=expense_date,
        payment_mode=payment_mode
    )
    db.add(expense)
    db.commit()
    db.refresh(expense)
    logger.info("Expense saved to database")
    return expense


def get_all_expenses(db: Session):
    return db.query(Expense).all()


def get_expense_by_id(db: Session, expense_id: int):
    return db.query(Expense).filter(Expense.id == expense_id).first()


def delete_expense(db: Session, expense_id: int):
    expense = get_expense_by_id(db, expense_id)
    if expense:
        db.delete(expense)
        db.commit()
    logger.info("Expense deleted from database")
    return expense
