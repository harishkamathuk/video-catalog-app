import pytest
from tests.fixtures.database_fixtures import test_db_engine,  test_db_tables, test_db_session
from tests.fixtures.media_fixtures import mock_composite_strategy, mock_audio_strategy, mock_video_strategy, mock_image_strategy, mock_default_strategy

@pytest.fixture(scope="session")
def app_config():
    """
    Provides a session-scoped fixture for application configuration.

    This fixture returns a dictionary containing test-specific configuration
    values, such as log level and database URL. These values are used to 
    simulate the application's runtime environment during testing.

    Returns:
        dict: A dictionary with configuration keys and test-specific values.
              Example:
              {
                  "LOG_LEVEL": "DEBUG",
                  "DATABASE_URL": "sqlite:///:memory:"
              }
    """
    return {"LOG_LEVEL": "DEBUG", "DATABASE_URL": "sqlite:///:memory:"}