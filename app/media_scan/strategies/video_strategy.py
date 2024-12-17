from app.media_scan.strategies.media_strategy import MediaValidationStrategy


class VideoValidationStrategy(MediaValidationStrategy):
    """
    Validation strategy for video files based on file extensions.
    """    
    VIDEO_EXTENSIONS = {".mp4", ".mkv", ".avi", ".mov", ".wmv"}

    def validate(self, file_name: str) -> bool:
        _, ext = file_name.rsplit('.', 1)
        return f".{ext.lower()}" in self.VIDEO_EXTENSIONS
