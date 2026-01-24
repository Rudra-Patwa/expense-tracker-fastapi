# Pydantic Schemas (Data Validation)
from pydantic import BaseModel
from typing import Optional
from datetime import date

class ExpenseBase(BaseModel):
    amount: float
    category : str
    description: Optional[str] =None
    expense_date: date
    payment_mode : Optional[str]=None

class ExpenseCreate(ExpenseBase):
    pass

class ExpenseResponse(ExpenseBase):
    pass

    class Config: # it tells pydantic ,I will give you SQLAlchemy objects, not dicts.
        from_attributes=True


