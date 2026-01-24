from datetime import date
from backend.app.crud import (
    create_expense,
    get_all_expenses,
    get_expense_by_id,
    delete_expense,
)

def test_create_expense(db):
    expense = create_expense(
        db=db,
        amount=100.0,
        category="Food",
        description="Test lunch",
        expense_date=date.today(),
        payment_mode="Cash"
    )

    assert expense.id is not None
    assert expense.amount == 100.0
    assert expense.category == "Food"


def test_get_all_expenses(db):
    create_expense(
        db=db,
        amount=50.0,
        category="Travel",
        description="Bus ticket",
        expense_date=date.today(),
        payment_mode="UPI"
    )

    expenses = get_all_expenses(db)
    assert len(expenses) == 1


def test_get_expense_by_id(db):
    expense = create_expense(
        db=db,
        amount=200.0,
        category="Shopping",
        description="Shoes",
        expense_date=date.today(),
        payment_mode="Card"
    )

    fetched = get_expense_by_id(db, expense.id)
    assert fetched is not None
    assert fetched.id == expense.id


def test_delete_expense(db):
    expense = create_expense(
        db=db,
        amount=75.0,
        category="Snacks",
        description="Chips",
        expense_date=date.today(),
        payment_mode="Cash"
    )

    deleted = delete_expense(db, expense.id)
    assert deleted is not None

    remaining = get_all_expenses(db)
    assert len(remaining) == 0
