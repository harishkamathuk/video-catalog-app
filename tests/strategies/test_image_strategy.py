import pytest

from app.media_scan.strategies.image_validation import ImageValidationStrategy

# File: tests/strategies/test_image_strategy.py

def test_validate_supported_extensions(mock_image_strategy):
    """
    Test that supported image file extensions are validated as True.

    Args:
        image_strategy (ImageValidationStrategy): Fixture for the strategy.

    Asserts:
        True for each file name with a supported extension.
    """
    valid_files = ["test_image.jpg", "test_picture.png", "test_photo.gif", "test_graphic.bmp", "test_icon.tiff"]
    for file_name in valid_files:
        assert mock_image_strategy.validate(file_name) is True

def test_validate_unsupported_extensions(mock_image_strategy):
    """
    Test that unsupported file extensions are validated as False.

    Args:
        image_strategy (ImageValidationStrategy): Fixture for the strategy.

    Asserts:
        False for each file name with an unsupported extension.
    """
    invalid_files = ["document.txt", "video.mp4", "audio.mp3", "archive.zip"]
    for file_name in invalid_files:
        assert mock_image_strategy.validate(file_name) is False

def test_validate_edge_cases(mock_image_strategy):
    """
    Test edge cases for file validation, including uppercase, no extension, invalid input, and exceptions.

    Args:
        image_strategy (ImageValidationStrategy): Fixture for the strategy.

    Asserts:
        Correct behavior for edge cases like empty names, invalid extensions, etc.
    """
    edge_cases = [
        ("", False),                    # Empty file name
        ("test_imagefile", False),      # No extension
        ("test_image.JPG", True),       # Uppercase extension
        ("test_picture.PnG", True),     # Mixed case extension
        (".jpg", False),                # Just the extension without a name
    ]
    for file_name, expected in edge_cases:
        assert mock_image_strategy.validate(file_name) == expected

def test_validate_no_dot_string(mock_image_strategy):
    """
    Test strings that don't have dots at all.
    """
    assert mock_image_strategy.validate("no_extension") == False
    assert mock_image_strategy.validate("") == False

def test_validate_malformed_strings(mock_image_strategy):
    """
    Test strings that would trigger the except block, e.g., invalid formats or errors during split.
    """
    malformed_inputs = [
        "image..jpg",  # Double dots
        "picture.jpg.jpg",  # Multiple extensions
        ".jpg",  # Edge-case with only the dot
        "photo/image.jpg",  # Path-like structure
    ]
    for file_name in malformed_inputs:
        assert mock_image_strategy.validate(file_name) == False

def test_validate_edge_case_uppercase(mock_image_strategy):
    """
    Test case for uppercase file extensions and mixed-case extensions.
    """
    assert mock_image_strategy.validate("test_image.JPG") == True
    assert mock_image_strategy.validate("test_picture.PnG") == True

def test_validate_non_image_inputs(mock_image_strategy):
    """
    Test that images are only validated when explicitly matching known image extensions.
    """
    invalid_inputs = [
        "random_file.pdf",  # Non-media
        "audio.mp3",
    ]
    for file_name in invalid_inputs:
        assert mock_image_strategy.validate(file_name) == False

def test_validate_supported_extensions_without_mock():
    """
    Test that supported image file extensions are validated as True.
    """
    image_strategy = ImageValidationStrategy()
    valid_files = ["test_image.jpg", "test_picture.png", "test_photo.gif", "test_graphic.bmp", "test_icon.tiff"]
    for file_name in valid_files:
        assert image_strategy.validate(file_name) is True

def test_validate_unsupported_extensions_without_mock():
    """
    Test unsupported image extensions return False.
    """
    image_strategy = ImageValidationStrategy()
    invalid_files = ["document.txt", "video.mp4", "audio.mp3", "archive.zip"]
    for file_name in invalid_files:
        assert image_strategy.validate(file_name) is False

def test_validate_no_dot_string_without_mock():
    """
    Test strings that don't have dots at all.
    """
    image_strategy = ImageValidationStrategy()
    
    # Edge case: No dot at all in filename
    invalid_files = ["no_extension", "", "imagename", "file_with_no_valid_format"]
    for file_name in invalid_files:
        assert image_strategy.validate(file_name) is False

def test_validate_malformed_strings_without_mock():
    """
    Test strings that would trigger the except block, e.g., invalid formats or errors during split.
    """
    image_strategy = ImageValidationStrategy()
    malformed_inputs = [
        "image..jpg",  # Double dots
        "picture.jpg.jpg",  # Multiple extensions
        ".jpg",  # Edge-case with only the dot
        "photo/image.jpg",  # Path-like structure
    ]
    for file_name in malformed_inputs:
        assert image_strategy.validate(file_name) == False

def test_validate_edge_case_uppercase_without_mock():
    """
    Test case for uppercase file extensions and mixed-case extensions.
    """
    image_strategy = ImageValidationStrategy()
    assert image_strategy.validate("image.JPG") == True
    assert image_strategy.validate("picture.PnG") == True

def test_validate_non_image_inputs_without_mock():
    """
    Test that images are only validated when explicitly matching known image extensions.
    """
    image_strategy = ImageValidationStrategy()
    invalid_inputs = [
        "random_file.pdf",  # Non-media
        "audio.mp3",
    ]
    for file_name in invalid_inputs:
        assert image_strategy.validate(file_name) == False