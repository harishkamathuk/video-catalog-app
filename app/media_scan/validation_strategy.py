from abc import ABC, abstractmethod


class MediaValidationStrategy(ABC):
    """
    Abstract base class for any media validation strategy.
    """

    @abstractmethod
    def validate(self, file_name: str) -> bool:
        """
        Abstract method to validate a file name.

        Args:
            file_name (str): The file name to validate.

        Returns:
            bool: Whether the file is valid or invalid.
        """
        raise NotImplementedError("You must implement the validate method.")


class VideoValidationStrategy(MediaValidationStrategy):
    """
    Validation strategy for video files based on file extensions.
    """

    VIDEO_EXTENSIONS = {".mp4", ".mkv", ".avi", ".mov", ".wmv"}

    def validate(self, file_name: str) -> bool:
        _, ext = file_name.rsplit('.', 1)
        return f".{ext.lower()}" in self.VIDEO_EXTENSIONS


class AudioValidationStrategy(MediaValidationStrategy):
    """
    Validation strategy for audio files based on file extensions.
    """

    AUDIO_EXTENSIONS = {".mp3", ".wav", ".flac", ".aac", ".ogg"}

    def validate(self, file_name: str) -> bool:
        _, ext = file_name.rsplit('.', 1)
        return f".{ext.lower()}" in self.AUDIO_EXTENSIONS


class ImageValidationStrategy(MediaValidationStrategy):
    """
    Validation strategy for image files based on file extensions.
    """

    IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".gif"}

    def validate(self, file_name: str) -> bool:
        _, ext = file_name.rsplit('.', 1)
        return f".{ext.lower()}" in self.IMAGE_EXTENSIONS


class CompositeValidationStrategy:
    """
    Composite strategy for managing multiple media validation strategies.
    """

    def __init__(self, strategies):
        """
        Initialize with a dictionary of media type -> validation strategy.

        Args:
            strategies (dict): A dictionary mapping media types to validation strategies.
        """
        self.strategies = strategies

    def validate(self, file_name: str) -> str:
        """
        Validate a file and return its media type if valid.

        Args:
            file_name (str): The file name to validate.

        Returns:
            str: The media type if valid, otherwise None.
        """
        for media_type, strategy in self.strategies.items():
            if strategy.validate(file_name):
                return media_type
        return None
