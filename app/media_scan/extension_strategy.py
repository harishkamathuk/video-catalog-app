from app.video_scan.validation_strategy import VideoValidationStrategy
import os


class ExtensionValidationStrategy(VideoValidationStrategy):
    """
    Validates video files based on extensions.
    """

    VALID_EXTENSIONS = [".mp4", ".avi", ".mkv", ".mov", ".flv", ".wmv"]

    def validate(self, file_name: str) -> bool:
        """
        Validates a file based on its extension.

        Args:
            file_name (str): The file name to validate.

        Returns:
            bool: True if valid video, False otherwise.
        """
        _, ext = os.path.splitext(file_name)
        return ext.lower() in self.VALID_EXTENSIONS
