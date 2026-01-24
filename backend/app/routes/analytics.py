from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from backend.app.database import get_db
from backend.app.models import Expense
import logging

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

@router.get("/category-wise")
def category_wise_expense(db: Session = Depends(get_db)):
    logger.info("Calculating category-wise expense")

    results = (
        db.query(
            Expense.category,
            func.sum(Expense.amount).label("total_amount")
        )
        .group_by(Expense.category)
        .all()
    )

    return [
        {"category": r.category, "total_amount": float(r.total_amount)}
        for r in results
    ]
from sqlalchemy import extract
@router.get("/monthly-trend")
def monthly_trend(db: Session = Depends(get_db)):
    logger.info("Calculating monthly expense trend")

    month_expr = func.extract("month", Expense.expense_date)

    results = (
        db.query(
            month_expr.label("month"),
            func.sum(Expense.amount).label("total_amount")
        )
        .group_by(month_expr)
        .order_by(month_expr)
        .all()
    )

    return [
        {
            "month": int(r.month),
            "total_amount": float(r.total_amount)
        }
        for r in results
    ]


@router.get("/summary")
def expense_summary(db: Session = Depends(get_db)):
    logger.info("Calculating expense summary")

    total = db.query(func.sum(Expense.amount)).scalar() or 0

    count = db.query(func.count(Expense.id)).scalar()

    return {
        "total_expense": float(total),
        "total_transactions": count
    }
