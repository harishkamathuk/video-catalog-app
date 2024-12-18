"""
Fixtures for setting up a test database using SQLAlchemy.

Provides an in-memory SQLite database engine and session for testing 
database interactions.
"""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

@pytest.fixture(scope="session")
def test_db_engine():
    """
    Fixture for creating an in-memory SQLite database engine.

    Scope:
        - session: The database engine is shared across all tests in the session.

    Yields:
        sqlalchemy.Engine: The database engine instance.

    Cleanup:
        - Disposes of the engine after all tests in the session are completed.
    """
    engine = create_engine("sqlite:///:memory:")
    yield engine
    engine.dispose()

@pytest.fixture(scope="function")
def test_db_session(test_db_engine):
    """
    Fixture for providing a new database session for each test function.

    Dependencies:
        - test_db_engine: Uses the in-memory SQLite database engine.

    Scope:
        - function: A new session is created for each test function.

    Yields:
        sqlalchemy.orm.Session: A database session instance.

    Cleanup:
        - Closes the session after the test function is executed.
    """
    Session = sessionmaker(bind=test_db_engine)
    session = Session()
    yield session
    session.close()
