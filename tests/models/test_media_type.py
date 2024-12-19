import pytest

from app.media_scan.models.media_type import MediaType

def test_media_type_get_id_by_name(test_db_session):
    """
    Test the MediaType.get_id_by_name method.
    This test performs the following steps:
    1. Adds a media type with the name 'video' to the database.
    2. Commits the transaction.
    3. Retrieves the media type ID by the name 'video' and asserts that it matches the ID of the added media type.
    4. Attempts to retrieve a media type ID by a non-existent name 'nonexistent' and asserts that a ValueError is raised.
    Args:
        session: The database session fixture used for the test.
    """
    # Add a media type to the database
    media_type = MediaType(name='video')
    test_db_session.add(media_type)
    test_db_session.commit()

    # Test retrieving the media type ID by name
    media_type_id = MediaType.get_id_by_name(test_db_session, 'video')
    assert media_type_id == media_type.id

    # Test retrieving a non-existent media type
    with pytest.raises(ValueError):
        MediaType.get_id_by_name(test_db_session, 'nonexistent')