"""
Unit tests for the CompositeValidationStrategy class.

These tests validate that CompositeValidationStrategy correctly delegates 
file validation to the appropriate media-specific strategy or falls back 
to the default strategy for unsupported media types.
"""

import pytest
from unittest.mock import MagicMock
from app.media_scan.strategies.composite_validation import CompositeValidationStrategy
from app.media_scan.strategies.audio_validation import AudioValidationStrategy
from app.media_scan.strategies.video_validation import VideoValidationStrategy
from app.media_scan.strategies.image_validation import ImageValidationStrategy
from app.media_scan.strategies.default_validation import DefaultValidationStrategy

def test_validate_audio(mock_composite_strategy, mock_audio_strategy, mock_video_strategy, mock_image_strategy, mock_default_strategy):
    """
    Test that CompositeValidationStrategy correctly validates an audio file.

    Mocks:
        - mock_audio_strategy: Simulates validation success for audio files.
        - mock_video_strategy, mock_image_strategy, mock_default_strategy: 
          Simulate validation failures for other media types.

    Asserts:
        - The media type is identified as "audio".
        - The audio strategy's `validate` method is called with the correct file name.
    """
    mock_audio_strategy.validate.return_value = False
    mock_video_strategy.validate.return_value = True
    mock_image_strategy.validate.return_value = False
    mock_default_strategy.validate.return_value = False

    media_type = mock_composite_strategy.validate("test_song.mp3")
    assert media_type == "audio"
    mock_audio_strategy.validate.assert_called_once_with("test_song.mp3")


def test_validate_video(mock_composite_strategy, mock_audio_strategy, mock_video_strategy, mock_image_strategy, mock_default_strategy):
    """
    Test that CompositeValidationStrategy correctly validates a video file.

    Mocks:
        - mock_video_strategy: Simulates validation success for video files.
        - mock_audio_strategy, mock_image_strategy, mock_default_strategy: 
          Simulate validation failures for other media types.

    Asserts:
        - The media type is identified as "video".
        - The video strategy's `validate` method is called with the correct file name.
    """
    mock_video_strategy.validate.return_value = True
    mock_audio_strategy.validate.return_value = False
    mock_image_strategy.validate.return_value = False
    mock_default_strategy.validate.return_value = False

    media_type = mock_composite_strategy.validate("test_movie.mp4")
    assert media_type == "video"
    mock_video_strategy.validate.assert_called_once_with("test_movie.mp4")


def test_validate_image(mock_composite_strategy, mock_audio_strategy, mock_video_strategy, mock_image_strategy, mock_default_strategy):
    """
    Test that CompositeValidationStrategy correctly validates an image file.

    Mocks:
        - mock_image_strategy: Simulates validation success for image files.
        - mock_audio_strategy, mock_video_strategy, mock_default_strategy: 
          Simulate validation failures for other media types.

    Asserts:
        - The media type is identified as "image".
        - The image strategy's `validate` method is called with the correct file name.
    """
    mock_image_strategy.validate.return_value = True
    mock_audio_strategy.validate.return_value = False
    mock_video_strategy.validate.return_value = False
    mock_default_strategy.validate.return_value = False

    media_type = mock_composite_strategy.validate("test_image.jpg")
    assert media_type == "image"
    mock_image_strategy.validate.assert_called_once_with("test_image.jpg")


def test_validate_unknown(mock_composite_strategy, mock_audio_strategy, mock_video_strategy, mock_image_strategy, mock_default_strategy):
    """
    Test that CompositeValidationStrategy falls back to the default strategy 
    for unknown media files.

    Mocks:
        - mock_default_strategy: Simulates validation success for the default strategy.
        - mock_audio_strategy, mock_video_strategy, mock_image_strategy: 
          Simulate validation failures for other media types.

    Asserts:
        - The media type is identified as "unknown".
        - The default strategy's `validate` method is called with the correct file name.
    """
    mock_audio_strategy.validate.return_value = False
    mock_video_strategy.validate.return_value = False
    mock_image_strategy.validate.return_value = False
    mock_default_strategy.validate.return_value = True

    media_type = mock_composite_strategy.validate("unknown_file.xyz")
    assert media_type == "unknown"
    mock_default_strategy.validate.assert_called_once_with("unknown_file.xyz")
