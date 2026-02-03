# Expense Tracker & Analytics App

A full-stack expense tracking and analytics application that allows users to record daily expenses, analyze spending patterns, and generate insights through APIs and interactive dashboards.

The backend is built using **FastAPI** with a clean REST architecture, while analytics and visual exploration are supported using **Pandas** and **Streamlit**. The project also includes automated testing with **Pytest** and structured logging for production readiness.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Architecture](#project-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Analytics & Dashboard](#analytics--dashboard)
- [Testing](#testing)
- [Logging](#logging)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

---

##Features

- Add, update, and delete expenses
- Track expenses by:
  - Category
  - Payment mode
  - Date
- RESTful API design using FastAPI
- Real-time analytics using Pandas
- Interactive expense dashboards using Streamlit
- Category-wise and monthly spending insights
- Input validation using Pydantic
- Structured logging for backend operations
- Automated API testing using Pytest
- Ready for local development and cloud deployment

---

##Tech Stack

| Layer | Technology |
|-----|-----------|
| Backend API | FastAPI |
| Server | Uvicorn |
| Database | SQLite (default), MySQL (optional) |
| ORM | SQLAlchemy |
| Data Analysis | Pandas |
| Dashboard | Streamlit |
| Validation | Pydantic |
| Testing | Pytest |
| Logging | Python `logging` |
| API Docs | Swagger UI (`/docs`) |

---

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Rudra-Patwa/expense_tracker.git
cd expense-tracker
```
Create a virtual environment
```
python -m venv .venv
```
Activate the virtual environment
Windows
```
.venv\Scripts\activate

```
macOS / Linux
```
source .venv/bin/activate
```
Install dependencies
```
pip install -r requirements.txt

```
Usage
## Start the FastAPI backend
```
uvicorn backend.app.main:app --reload

```
Open API documentation
Visit:
```
http://127.0.0.1:8000/docs

```
Use Swagger UI to interact with all API endpoints.
API Endpoints
| Method | Endpoint         | Description        |
| -----: | ---------------- | ------------------ |
|   POST | `/expenses/`     | Add a new expense  |
|    GET | `/expenses/`     | Fetch all expenses |
|    PUT | `/expenses/{id}` | Update an expense  |
| DELETE | `/expenses/{id}` | Delete an expense  |


Analytics
| Method | Endpoint                   | Description                |
| -----: | -------------------------- | -------------------------- |
|    GET | `/analytics/category-wise` | Total expense per category |
|    GET | `/analytics/monthly-trend` | Monthly spending trend     |
|    GET | `/analytics/summary`       | Overall expense summary    |

Analytics & Dashboard
Expense data is processed using Pandas
Aggregations and trends are computed server-side
Interactive visualizations are built using Streamlit

## Run Streamlit dashboard
    ```
    streamlit run analytics/streamlit_app.py
    ```

Dashboard Features

    Category-wise expense distribution
    Monthly spending trends
    Expense summaries and insights

    Testing



This project includes automated API tests written using Pytest.
Run tests

```
pytest
```

Test Coverage

    Expense CRUD operations
    Analytics endpoints
    Input validation and edge cases

Logging

    Centralized logging using Python’s logging module
    Logs include:
        API request
        Errors and exceptions
        Analytics processing steps
    Helps in debugging and production monitoring

Future Improvements

    Authentication & user accounts
    JWT-based secure APIs
    Dockerization
    Cloud deployment (AWS / Railway / Render)
    Advanced analytics and forecasting
    Export reports (CSV / PDF)

Contributing
1. Fork the repository
2. Create a new feature branch
    ```
    git checkout -b feature/your-feature
    ```

3. Commit your changes
```
git commit -m "feat: add your feature"
```
4. Push and open a Pull Request

License.
This project is licensed under the MIT License.


---

## ✅ Recommended Commit Message

```bash
git commit -m "docs: add complete README with setup, APIs, analytics, Streamlit dashboard, and 
