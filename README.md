# Expense Tracker App 🧾

**A full-stack Python backend application to track personal expenses, analyze spending patterns, and generate insights. Built with FastAPI, SQLAlchemy, and Python.**

# Table of Contents

    Features
    Tech Stack
    Installation
    Usage
    API Endpoints
    Analytics
    Contributing
    License
    Features
    Add, update, and delete expenses

Track expenses by category, payment mode, and date
Generate category-wise and monthly trend analytics
Clean and validated input data
Logging for backend operations
Ready for local or cloud deployment

Tech Stack
Layer	Technology
Backend	Python 3.11, FastAPI
Database	SQLite (default), MySQL (optional)
ORM	SQLAlchemy
Logging	Python logging module
API Docs	FastAPI Swagger (/docs)
Installation

### Clone the repository

git clone https://github.com/Rudra-Patwa/expense_tracker.git
cd expense-tracker

Create a virtual environment

python -m venv .venv


Activate the virtual environment

Windows (PowerShell)

.venv\Scripts\activate


macOS/Linux

source .venv/bin/activate


Install dependencies

pip install -r requirements.txt

Usage

Run the server

**uvicorn backend.app.main:app --reload**


Access the app
Open your browser and go to:

http://127.0.0.1:8000/docs


Swagger UI to interact with all endpoints

Test adding, viewing, and analyzing expenses

API Endpoints
Expenses
Method	Endpoint	Description
POST	/expenses/	Add a new expense
GET	/expenses/	List all expenses
PUT	/expenses/{id}	Update an expense
DELETE	/expenses/{id}	Delete an expense
Analytics
Method	Endpoint	Description
GET	/analytics/category-wise	Get total expenses per category
GET	/analytics/monthly-trend	Get monthly spending trends
GET	/analytics/summary	Get overall expense summary
Example Request

**Add an expense:**

POST /expenses/
{
  "amount": 500,
  "category": "Food",
  "description": "Lunch at cafe",
  "expense_date": "2026-01-24",
  "payment_mode": "Cash"
}


Response:

{
  "id": 1,
  "amount": 500,
  "category": "Food",
  "description": "Lunch at cafe",
  "expense_date": "2026-01-24",
  "payment_mode": "Cash"
}

Analytics Example

Category-wise expenses:

GET /analytics/category-wise


Response:

[
  {"category": "Food", "total_amount": 1500.0},
  {"category": "Transport", "total_amount": 800.0},
  {"category": "Shopping", "total_amount": 1200.0}
]

Contributing

Fork the repository

Create a new branch

git checkout -b feature/your-feature


Make changes & commit

git commit -m "Add feature"