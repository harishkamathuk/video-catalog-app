import pytest
from unittest.mock import MagicMock
from app.media_scan.strategies.audio_validation import AudioValidationStrategy
from app.media_scan.strategies.video_validation import VideoValidationStrategy
from app.media_scan.strategies.image_validation import ImageValidationStrategy
from app.media_scan.strategies.default_validation import DefaultValidationStrategy
from app.media_scan.strategies.composite_validation import CompositeValidationStrategy

@pytest.fixture
def mock_audio_strategy():
    """
    Fixture to create and return a mocked instance of `AudioValidationStrategy` for testing purposes.

    This mocked strategy simulates the behavior of `AudioValidationStrategy`'s `validate` method 
    with custom logic to handle edge case testing. It considers standard audio file names and edge 
    cases such as case-insensitive extensions and invalid filenames.

    Logic Implemented:
        - Returns `True` for common audio file extensions like "song.mp3", "track.wav", 
          "audio.flac", "sample.aac", and "music.ogg".
        - Handles edge cases such as:
          - Uppercase audio extensions (e.g., "song.MP3", "track.WaV").
          - Invalid file names like empty strings (`""`) or filenames like `"audiofile"` or `".mp3"`.
        - Ensures case normalization for audio file extensions to simulate a real-world case-insensitive behavior.

    Returns:
        MagicMock: A mocked instance of `AudioValidationStrategy` with a custom `side_effect`
        applied to the `validate` method for the desired test scenarios.

    Usage:
        This fixture is used in test cases to simulate audio file validation logic without needing 
        real implementations or dependency setups.

    Example:
        ```
        def test_valid_audio_files(mock_audio_strategy):
            assert mock_audio_strategy.validate("song.mp3") == True
            assert mock_audio_strategy.validate("track.WaV") == True
            assert mock_audio_strategy.validate("audiofile") == False
            assert mock_audio_strategy.validate(".mp3") == False
        ```
    """
    mock = MagicMock(spec=AudioValidationStrategy)

    # Map logic for edge case testing
    def validate_logic(file_name):
        valid_files = {"test_song.mp3", "test_track.wav", "test_audio.flac", "test_sample.aac", "test_music.ogg"}
        # Normalize for case-insensitivity handling (assuming supported extensions are case-insensitive)
        if file_name.lower() in valid_files:
            return True
        # Handle edge case logic directly
        if file_name in ["test_song.MP3", "test_track.WaV"]:  # Handle mixed/uppercase extensions
            return True
        if file_name in ["", "test_audiofile", ".mp3"]:
            return False
        return False

    # Apply our logic to the mock
    mock.validate.side_effect = validate_logic
    return mock



@pytest.fixture
def mock_video_strategy():
    """
    Fixture to create and return a mocked instance of `VideoValidationStrategy` for testing purposes.

    This mocked strategy simulates the behavior of `VideoValidationStrategy`'s `validate` method 
    with custom logic to handle edge case testing. It considers standard video file names and edge 
    cases such as case-insensitive extensions and invalid filenames.

    Logic Implemented:
        - Returns `True` for common video file extensions like "movie.mp4", "clip.avi", 
            "video.mkv", "footage.mov", and "film.wmv".
        - Handles edge cases such as:
            - Uppercase video extensions (e.g., "movie.MP4", "clip.AVI").
            - Invalid file names like empty strings (`""`) or filenames like `"videofile"` or `".mp4"`.
        - Ensures case normalization for video file extensions to simulate a real-world case-insensitive behavior.

    Returns:
        MagicMock: A mocked instance of `VideoValidationStrategy` with a custom `side_effect`
        applied to the `validate` method for the desired test scenarios.

    Usage:
        This fixture is used in test cases to simulate video file validation logic without needing 
        real implementations or dependency setups.

    Example:
        ```
        def test_valid_video_files(mock_video_strategy):
            assert mock_video_strategy.validate("movie.mp4") == True
            assert mock_video_strategy.validate("clip.AVI") == True
            assert mock_video_strategy.validate("videofile") == False
            assert mock_video_strategy.validate(".mp4") == False
        ```
    """
    mock = MagicMock(spec=VideoValidationStrategy)

    # Map logic for edge case testing
    def validate_logic(file_name):

        valid_files = ["test_movie.mp4", "test_clip.mkv", "test_video.avi", "test_film.mov", "test_recording.wmv"]

        # Normalize for case-insensitivity handling (assuming supported extensions are case-insensitive)
        if file_name.lower() in valid_files:
            return True
        # Handle edge case logic directly
        if file_name in ["test_movie.MP4", "test_clip.AVI"]:  # Handle mixed/uppercase extensions
            return True
        if file_name in ["", "test_videofile", ".mp4"]:
            return False
        return False

    # Apply our logic to the mock
    mock.validate.side_effect = validate_logic
    return mock

@pytest.fixture
def mock_image_strategy():
    """
    Fixture to create and return a mocked instance of `ImageValidationStrategy` for testing purposes.

    This mocked strategy simulates the behavior of `ImageValidationStrategy`'s `validate` method 
    with custom logic to handle edge case testing. It considers standard image file names and edge 
    cases such as case-insensitive extensions and invalid filenames.

    Logic Implemented:
        - Returns `True` for common image file extensions like "image.jpg", "picture.png", 
          "photo.gif", "graphic.bmp", and "icon.tiff".
        - Handles edge cases such as:
          - Uppercase image extensions (e.g., "image.JPG", "picture.PNG").
          - Invalid file names like empty strings (`""`) or filenames like `"imagefile"` or `".jpg"`.
        - Ensures case normalization for image file extensions to simulate a real-world case-insensitive behavior.

    Returns:
        MagicMock: A mocked instance of `ImageValidationStrategy` with a custom `side_effect`
        applied to the `validate` method for the desired test scenarios.

    Usage:
        This fixture is used in test cases to simulate image file validation logic without needing 
        real implementations or dependency setups.

    Example:
        ```
        def test_valid_image_files(mock_image_strategy):
            assert mock_image_strategy.validate("image.jpg") == True
            assert mock_image_strategy.validate("picture.PNG") == True
            assert mock_image_strategy.validate("imagefile") == False
            assert mock_image_strategy.validate(".jpg") == False
        ```
    """
    mock = MagicMock(spec=ImageValidationStrategy)

    # Map logic for edge case testing
    def validate_logic(file_name):
        valid_files = {"test_image.jpg", "test_picture.png", "test_photo.gif", "test_graphic.bmp", "test_icon.tiff"}
        # Normalize for case-insensitivity handling (assuming supported extensions are case-insensitive)
        if file_name.lower() in valid_files:
            return True
        # Handle edge case logic directly
        if file_name in ["test_image.JPG", "test_picture.PNG"]:  # Handle mixed/uppercase extensions
            return True
        if file_name in ["", "test_imagefile", ".jpg"]:
            return False
        return False

    # Apply our logic to the mock
    mock.validate.side_effect = validate_logic
    return mock


@pytest.fixture
def mock_default_strategy():
    """
    Provides a mocked instance of the DefaultValidationStrategy.

    The mock is used to simulate the behavior of the DefaultValidationStrategy 
    class during testing without invoking its actual implementation.

    Returns:
        MagicMock: A mock object for DefaultValidationStrategy.
    """
    return MagicMock(spec=DefaultValidationStrategy)


@pytest.fixture
def composite_strategy(mock_audio_strategy, mock_video_strategy, mock_image_strategy, mock_default_strategy):
    """
    Provides a configured CompositeValidationStrategy instance with mocked sub-strategies.

    This fixture creates a CompositeValidationStrategy and replaces its internal
    strategies with mocked versions. This allows for isolated testing of the 
    composite strategy logic without relying on the actual implementations of 
    the sub-strategies.

    Args:
        mock_audio_strategy (MagicMock): Mocked AudioValidationStrategy.
        mock_video_strategy (MagicMock): Mocked VideoValidationStrategy.
        mock_image_strategy (MagicMock): Mocked ImageValidationStrategy.
        mock_default_strategy (MagicMock): Mocked DefaultValidationStrategy.

    Returns:
        CompositeValidationStrategy: An instance of the composite strategy with mocked sub-strategies.
    """
    composite = CompositeValidationStrategy()
    composite.strategies = {
        "audio": mock_audio_strategy,
        "video": mock_video_strategy,
        "image": mock_image_strategy,
        "default": mock_default_strategy,
    }
    return composite
