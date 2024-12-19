import pytest
from unittest.mock import Mock
from utils.directory_scanner import DirectoryScanner

from app.media_scan.strategies.composite_validation import CompositeValidationStrategy
from app.media_scan.strategies.audio_validation import AudioValidationStrategy
from app.media_scan.strategies.video_validation import VideoValidationStrategy
from app.media_scan.strategies.image_validation import ImageValidationStrategy
from app.media_scan.strategies.default_validation import DefaultValidationStrategy

def test_identify_media_type_video(mock_composite_strategy, mock_audio_strategy, mock_video_strategy, mock_image_strategy, mock_default_strategy):
    """
    Test the identify_media_type method of DirectoryScanner for a video file.
    This test sets up mock strategies for audio, video, image, and default media types.
    It configures the mock strategies to return specific validation results, ensuring
    that only the video strategy validates the given media file as a video.
    Args:
        composite_strategy: The composite strategy used by the DirectoryScanner.
        mock_audio_strategy: Mock strategy for validating audio files.
        mock_video_strategy: Mock strategy for validating video files.
        mock_image_strategy: Mock strategy for validating image files.
        mock_default_strategy: Mock strategy for validating default media files.
    Asserts:
        The result of identify_media_type is 'video'.
        The composite strategy's validate method is called once with the file name.
    """
    mock_audio_strategy.validate.return_value = False
    mock_video_strategy.validate.return_value = True
    mock_image_strategy.validate.return_value = False
    mock_default_strategy.validate.return_value = False

    scanner = DirectoryScanner(mock_composite_strategy)
    media_type = scanner.identify_media_type('test_movie.mp4')
    assert media_type == 'video'
    mock_video_strategy.validate.assert_called_once_with('test_movie.mp4')

def test_identify_media_type_audio(mock_composite_strategy, mock_audio_strategy, mock_video_strategy, mock_image_strategy, mock_default_strategy):
    """
    Test the identify_media_type method of DirectoryScanner for an audio file.
    This test verifies that the identify_media_type method correctly identifies
    an audio file by using the mock_audio_strategy. It ensures that the validate
    method of the mock_audio_strategy is called and returns True, while the 
    validate methods of the other strategies return False.
    Args:
        mock_composite_strategy: A mock composite strategy used by DirectoryScanner.
        mock_audio_strategy: A mock strategy for validating audio files.
        mock_video_strategy: A mock strategy for validating video files.
        mock_image_strategy: A mock strategy for validating image files.
        mock_default_strategy: A mock default strategy for validating files.
    Asserts:
        The identified media type is 'audio'.
        The validate method of mock_audio_strategy is called once with 'test_song.mp3'.
    """
    
    mock_audio_strategy.validate.return_value = True
    mock_video_strategy.validate.return_value = False
    mock_image_strategy.validate.return_value = False
    mock_default_strategy.validate.return_value = False
    
    scanner = DirectoryScanner(mock_composite_strategy)
    media_type = scanner.identify_media_type('test_song.mp3')
    assert media_type == 'audio'
    mock_audio_strategy.validate.assert_called_once_with('test_song.mp3')

def test_identify_media_type_image(mock_composite_strategy, mock_audio_strategy, mock_video_strategy, mock_image_strategy, mock_default_strategy):
    """
    Test the identify_media_type method of DirectoryScanner for identifying an image file.
    This test sets up mock strategies for audio, video, image, and default media types.
    It configures the mock strategies to return specific validation results, ensuring that
    only the image strategy validates the given file as an image.
    Args:
        mock_composite_strategy: Mock composite strategy used by DirectoryScanner.
        mock_audio_strategy: Mock strategy for validating audio files.
        mock_video_strategy: Mock strategy for validating video files.
        mock_image_strategy: Mock strategy for validating image files.
        mock_default_strategy: Mock strategy for validating default files.
    Asserts:
        The identified media type is 'image'.
        The image strategy's validate method is called once with the given file.
    """
    
    mock_audio_strategy.validate.return_value = False
    mock_video_strategy.validate.return_value = False
    mock_image_strategy.validate.return_value = True
    mock_default_strategy.validate.return_value = False
        
    scanner = DirectoryScanner(mock_composite_strategy)
    media_type = scanner.identify_media_type('test_image.jpg')
    assert media_type == 'image'
    mock_image_strategy.validate.assert_called_once_with('test_image.jpg')

def test_identify_media_type_unknown(mock_composite_strategy, mock_audio_strategy, mock_video_strategy, mock_image_strategy, mock_default_strategy):
    '''
    Test the identify_media_type method of DirectoryScanner for an unknown file type.
    This test ensures that the identify_media_type method correctly identifies a file
    with an unknown extension as "unknown" by using the default validation strategy.
        mock_composite_strategy: The composite strategy used by the DirectoryScanner.
        The identify_media_type method returns "unknown" for the given file.
        The default validation strategy is called once with the given file.
    '''
    mock_audio_strategy.validate.return_value = False
    mock_video_strategy.validate.return_value = False
    mock_image_strategy.validate.return_value = False
    mock_default_strategy.validate.return_value = True
    
    scanner = DirectoryScanner(mock_composite_strategy)
    media_type = scanner.identify_media_type('unknown_file.xyz')
    assert media_type == "unknown"

    mock_default_strategy.validate.assert_called_once_with('unknown_file.xyz')
    
def test_scan_valid_media_files(mock_composite_strategy, mock_audio_strategy, mock_video_strategy, mock_image_strategy, mock_default_strategy, tmp_path):
    """
    Test the scan method of DirectoryScanner for valid media files.
    This test sets up a temporary directory with various media files and ensures
    that the scan method correctly identifies and yields the valid media files.
    Args:
        composite_strategy: The composite strategy used by the DirectoryScanner.
        mock_audio_strategy: Mock strategy for validating audio files.
        mock_video_strategy: Mock strategy for validating video files.
        mock_image_strategy: Mock strategy for validating image files.
        mock_default_strategy: Mock strategy for validating default media files.
        tmp_path: Temporary directory path provided by pytest.
    Asserts:
        The scan method yields the correct file paths and media types.
    """
    # Create temporary media files
    video_file = tmp_path / "test_movie.mp4"
    audio_file = tmp_path / "test_song.mp3"
    image_file = tmp_path / "test_image.jpg"
    unknown_file = tmp_path / "unknown_file.xyz"
    video_file.write_text("dummy content")
    audio_file.write_text("dummy content")
    image_file.write_text("dummy content")
    unknown_file.write_text("dummy content")

    # Set up mock return values for validation strategies
    mock_audio_strategy.validate.side_effect = lambda x: x == "test_song.mp3"
    mock_video_strategy.validate.side_effect = lambda x: x == "test_movie.mp4"
    mock_image_strategy.validate.side_effect = lambda x: x == "test_image.jpg"
    mock_default_strategy.validate.side_effect = lambda x: x == "unknown_file.xyz"

    scanner = DirectoryScanner(mock_composite_strategy)

    expected_results = [
        (str(image_file), "image"),
        (str(video_file), "video"),
        (str(audio_file), "audio"),
        (str(unknown_file), "unknown"),
    ]

    results = list(scanner.scan(tmp_path))

    assert results == expected_results