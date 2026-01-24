from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from backend.app import crud, schemas
from backend.app.database import get_db

import logging
logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)


@router.post(
    "",
    response_model=schemas.ExpenseResponse,
    status_code=status.HTTP_201_CREATED
)
@router.post("", response_model=schemas.ExpenseResponse)
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    logger.info(f"Creating expense: {expense.category} - {expense.amount}")
    return crud.create_expense(
        db=db,
        amount=expense.amount,
        category=expense.category,
        description=expense.description,
        expense_date=expense.expense_date,
        payment_mode=expense.payment_mode
    )

@router.get("")
def get_expenses(db: Session = Depends(get_db)):
    logger.info("Fetching all expenses")
    return crud.get_all_expenses(db)


@router.get("/{expense_id}")
def get_expense(expense_id: int, db: Session = Depends(get_db)):
    logger.info(f"Fetching expense id={expense_id}")
    expense = crud.get_expense_by_id(db, expense_id)
    if not expense:
        logger.warning(f"Expense not found: id={expense_id}")
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense



@router.delete("/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    logger.info(f"Deleting expense id={expense_id}")
    expense = crud.delete_expense(db, expense_id)
    if not expense:
        logger.warning(f"Attempted delete of non-existent expense id={expense_id}")
        raise HTTPException(status_code=404, detail="Expense not found")
