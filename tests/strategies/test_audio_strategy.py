# File: tests/strategies/test_audio_strategy.py
import pytest
from app.media_scan.strategies.audio_validation import AudioValidationStrategy

def test_validate_supported_extensions(mock_audio_strategy):
    """
    Test that supported audio file extensions are validated as True.

    Args:
        audio_strategy (AudioValidationStrategy): Fixture for the strategy.

    Asserts:
        True for each file name with a supported extension.
    """
    valid_files = ["test_song.mp3", "test_track.wav", "test_audio.flac", "test_sample.aac", "test_music.ogg"]
    for file_name in valid_files:
        assert mock_audio_strategy.validate(file_name) is True

def test_validate_unsupported_extensions(mock_audio_strategy):
    """
    Test that unsupported file extensions are validated as False.

    Args:
        audio_strategy (AudioValidationStrategy): Fixture for the strategy.

    Asserts:
        False for each file name with an unsupported extension.
    """
    invalid_files = ["document.txt", "video.mp4", "image.jpg", "archive.zip"]
    for file_name in invalid_files:
        assert mock_audio_strategy.validate(file_name) is False

def test_validate_edge_cases_old(mock_audio_strategy):
    """
    Test edge cases for file validation, including uppercase, no extension, and invalid input.

    Args:
        audio_strategy (AudioValidationStrategy): Fixture for the strategy.

    Asserts:
        Correct behavior for edge cases like empty names, uppercase extensions, etc.
    """
    edge_cases = [
        ("", False),                    # Empty file name
        ("test_audiofile", False),           # No extension
        ("test_song.MP3", True),             # Uppercase extension
        ("test_track.WaV", True),            # Mixed case extension
        (".mp3", False),                # Just the extension without a name
    ]
    for file_name, expected in edge_cases:
        assert mock_audio_strategy.validate(file_name) == expected

def test_validate_edge_cases(mock_audio_strategy):
    """
    Test edge cases for file validation, including uppercase, no extension, invalid input, and exceptions.

    Args:
        audio_strategy (AudioValidationStrategy): Fixture for the strategy.

    Asserts:
        Correct behavior for edge cases like empty names, invalid extensions, etc.
    """
    # Simulate cases that would enter the except block
    assert mock_audio_strategy.validate("") == False  # Empty name
    assert mock_audio_strategy.validate("test_audiofile") == False  # No valid extension
    assert mock_audio_strategy.validate(".mp3") == False  # Edge case just with an extension
    assert mock_audio_strategy.validate("..mp3") == False  # Malformed edge cases

    # Valid but edge-case insensitive checks
    assert mock_audio_strategy.validate("test_song.MP3") == True  # Uppercase valid case
    assert mock_audio_strategy.validate("test_track.WaV") == True  # Mixed-case valid

def test_validate_no_dot_string(mock_audio_strategy):
    """
    Test strings that don't have dots at all.
    """
    assert mock_audio_strategy.validate("no_extension") == False
    assert mock_audio_strategy.validate("") == False

def test_validate_malformed_strings(mock_audio_strategy):
    """
    Test strings that would trigger the except block, e.g., invalid formats or errors during split.
    """
    malformed_inputs = [
        "audio..mp3",  # Double dots
        "track.mp3.mp3",  # Multiple extensions
        ".mp3",  # Edge-case with only the dot
        "song/track.mp3",  # Path-like structure
    ]
    for file_name in malformed_inputs:
        assert mock_audio_strategy.validate(file_name) == False

def test_validate_edge_case_uppercase(mock_audio_strategy):
    """
    Test case for uppercase file extensions and mixed-case extensions.
    """
    assert mock_audio_strategy.validate("test_song.MP3") == True
    assert mock_audio_strategy.validate("test_track.WaV") == True

def test_validate_non_audio_inputs(mock_audio_strategy):
    """
    Test that audio is only validated when explicitly matching known audio extensions.
    """
    invalid_inputs = [
        "random_file.pdf",  # Non-media
        "image.jpeg",
    ]
    for file_name in invalid_inputs:
        assert mock_audio_strategy.validate(file_name) == False

def test_validate_supported_extensions_without_mock():
    """
    Test that supported audio file extensions are validated as True.
    """
    audio_strategy = AudioValidationStrategy()
    valid_files = ["test_song.mp3", "test_track.wav", "test_audio.flac", "test_sample.aac", "test_music.ogg"]
    for file_name in valid_files:
        assert audio_strategy.validate(file_name) is True

def test_validate_unsupported_extensions_without_mock():
    """
    Test unsupported audio extensions return False.
    """
    audio_strategy = AudioValidationStrategy()
    invalid_files = ["document.txt", "video.mp4", "image.jpg", "archive.zip"]
    for file_name in invalid_files:
        assert audio_strategy.validate(file_name) is False

def test_validate_no_dot_string_without_mock():
    """
    Test strings that don't have dots at all.
    """
    audio_strategy = AudioValidationStrategy()
    
    # Edge case: No dot at all in filename
    invalid_files = ["no_extension", "", "trackname", "file_with_no_valid_format"]
    for file_name in invalid_files:
        assert audio_strategy.validate(file_name) == False

def test_validate_malformed_strings_without_mock():
    """
    Test strings that would trigger the except block, e.g., invalid formats or errors during split.
    """
    audio_strategy = AudioValidationStrategy()
    malformed_inputs = [
        "audio..mp3",  # Double dots
        "track.mp3.mp3",  # Multiple extensions
        ".mp3",  # Edge-case with only the dot
        "song/track.mp3",  # Path-like structure
    ]
    for file_name in malformed_inputs:
        assert audio_strategy.validate(file_name) == False

def test_validate_edge_case_uppercase_without_mock():
    """
    Test case for uppercase file extensions and mixed-case extensions.
    """
    audio_strategy = AudioValidationStrategy()
    assert audio_strategy.validate("song.MP3") == True
    assert audio_strategy.validate("track.WaV") == True

def test_validate_non_audio_inputs_without_mock():
    """
    Test that audio is only validated when explicitly matching known audio extensions.
    """
    audio_strategy = AudioValidationStrategy()
    invalid_inputs = [
        "random_file.pdf",  # Non-media
        "image.jpeg",
    ]
    for file_name in invalid_inputs:
        assert audio_strategy.validate(file_name) == False
