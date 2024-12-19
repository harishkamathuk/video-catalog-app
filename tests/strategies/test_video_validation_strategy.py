import pytest
from app.media_scan.strategies.video_validation import VideoValidationStrategy

def test_validate_supported_extensions(mock_video_strategy):
    """
    Test that supported video file extensions are validated as True.

    Args:
        video_strategy (VideoValidationStrategy): Fixture for the strategy.

    Asserts:
        True for each file name with a supported extension.
    """
    valid_files = ["test_movie.mp4", "test_clip.mkv", "test_video.avi", "test_film.mov", "test_recording.wmv"]
    for file_name in valid_files:
        assert mock_video_strategy.validate(file_name) is True

def test_validate_unsupported_extensions(mock_video_strategy):
    """
    Test that unsupported file extensions are validated as False.

    Args:
        mock_video_strategy (VideoValidationStrategy): Fixture for the strategy.

    Asserts:
        False for each file name with an unsupported extension.
    """
    invalid_files = ["document.txt", "audio.mp3", "image.jpg", "archive.zip"]
    for file_name in invalid_files:
        assert mock_video_strategy.validate(file_name) is False

def test_validate_edge_cases(mock_video_strategy):
    """
    Test edge cases for file validation, including uppercase, no extension, invalid input, and exceptions.

    Args:
        mock_video_strategy (VideoValidationStrategy): Fixture for the strategy.

    Asserts:
        Correct behavior for edge cases like empty names, invalid extensions, etc.
    """
    edge_cases = [
        ("", False),                    # Empty file name
        ("video_file", False),          # No extension
        ("test_movie.MP4", True),            # Uppercase extension
        ("test_clip.MkV", True),             # Mixed case extension
        (".mp4", False),                # Just the extension without a name
    ]
    for file_name, expected in edge_cases:
        assert mock_video_strategy.validate(file_name) == expected

def test_validate_no_dot_string(mock_video_strategy):
    """
    Test strings that don't have dots at all.

    Args:
        video_strategy (VideoValidationStrategy): Fixture for the strategy.

    Asserts:
        False for strings without dots.
    """
    assert mock_video_strategy.validate("no_extension") == False
    assert mock_video_strategy.validate("") == False

def test_validate_malformed_strings(mock_video_strategy):
    """
    Test strings that would trigger the except block, e.g., invalid formats or errors during split.

    Args:
        mock_video_strategy (VideoValidationStrategy): Fixture for the strategy.

    Asserts:
        False for malformed strings.
    """
    malformed_inputs = [
        "video..mp4",  # Double dots
        "clip.mp4.mp4",  # Multiple extensions
        ".mp4",  # Edge-case with only the dot
        "movie/clip.mp4",  # Path-like structure
    ]
    for file_name in malformed_inputs:
        assert mock_video_strategy.validate(file_name) == False

def test_validate_edge_case_uppercase(mock_video_strategy):
    """
    Test case for uppercase file extensions and mixed-case extensions.

    Args:
        video_strategy (VideoValidationStrategy): Fixture for the strategy.

    Asserts:
        True for valid uppercase and mixed-case extensions.
    """
    assert mock_video_strategy.validate("test_movie.MP4") == True
    assert mock_video_strategy.validate("test_clip.AVI") == True

def test_validate_non_video_inputs(mock_video_strategy):
    """
    Test that video is only validated when explicitly matching known video extensions.

    Args:
        video_strategy (VideoValidationStrategy): Fixture for the strategy.

    Asserts:
        False for non-video file extensions.
    """
    invalid_inputs = [
        "random_file.pdf",  # Non-media
        "image.jpeg",
    ]
    for file_name in invalid_inputs:
        assert mock_video_strategy.validate(file_name) is False

def test_validate_supported_extensions_without_mock():
    """
    Test that supported video file extensions are validated as True.

    Asserts:
        True for each file name with a supported extension.
    """
    video_strategy = VideoValidationStrategy()
    valid_files = ["movie.mp4", "clip.mkv", "video.avi", "film.mov", "recording.wmv"]
    for file_name in valid_files:
        assert video_strategy.validate(file_name) is True

def test_validate_unsupported_extensions_without_mock():
    """
    Test unsupported video extensions return False.

    Asserts:
        False for each file name with an unsupported extension.
    """
    video_strategy = VideoValidationStrategy()
    invalid_files = ["document.txt", "audio.mp3", "image.jpg", "archive.zip"]
    for file_name in invalid_files:
        assert video_strategy.validate(file_name) is False

def test_validate_no_dot_string_without_mock():
    """
    Test strings that don't have dots at all.

    Asserts:
        False for strings without dots.
    """
    video_strategy = VideoValidationStrategy()
    
    invalid_files = ["no_extension", "", "videoname", "file_with_no_valid_format"]
    for file_name in invalid_files:
        assert video_strategy.validate(file_name) is False

def test_validate_malformed_strings_without_mock():
    """
    Test strings that would trigger the except block, e.g., invalid formats or errors during split.

    Asserts:
        False for malformed strings.
    """
    video_strategy = VideoValidationStrategy()
    malformed_inputs = [
        "video..mp4",  # Double dots
        "clip.mp4.mp4",  # Multiple extensions
        ".mp4",  # Edge-case with only the dot
        "movie/clip.mp4",  # Path-like structure
    ]
    for file_name in malformed_inputs:
        assert video_strategy.validate(file_name) is False

def test_validate_edge_case_uppercase_without_mock():
    """
    Test case for uppercase file extensions and mixed-case extensions.

    Asserts:
        True for valid uppercase and mixed-case extensions.
    """
    video_strategy = VideoValidationStrategy()
    assert video_strategy.validate("movie.MP4") == True
    assert video_strategy.validate("clip.MkV") == True

def test_validate_non_video_inputs_without_mock():
    """
    Test that video is only validated when explicitly matching known video extensions.

    Asserts:
        False for non-video file extensions.
    """
    video_strategy = VideoValidationStrategy()
    invalid_inputs = [
        "random_file.pdf",  # Non-media
        "image.jpeg",
    ]
    for file_name in invalid_inputs:
        assert video_strategy.validate(file_name) is False