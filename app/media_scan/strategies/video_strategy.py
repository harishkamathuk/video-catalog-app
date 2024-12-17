from app.media_scan.strategies.media_validation_strategy import MediaValidationStrategy
import os


class VideoValidationStrategy(MediaValidationStrategy):
    """
    Validation strategy for video files based on file extensions.
    """

    VIDEO_EXTENSIONS = {".mp4", ".mkv", ".avi", ".mov", ".wmv"}

    def validate(self, file_name: str) -> bool:
        _, ext = os.path.splitext(file_name)
        return ext.lower() in self.VIDEO_EXTENSIONS
