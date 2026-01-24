from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.app.database import Base
from backend.app.models import Expense
import pytest


TEST_DATABASE_URL="mysql+pymysql://root:Rudra%40123@localhost:3306/expense_tracker_test"

engine=create_engine(TEST_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

@pytest.fixture(scope="session")
def db_engine():
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def db(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()