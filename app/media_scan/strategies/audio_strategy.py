from app.media_scan.strategies.media_validation_strategy import MediaValidationStrategy
import os


class AudioValidationStrategy(MediaValidationStrategy):
    """
    Validation strategy for audio files based on file extensions.
    """

    AUDIO_EXTENSIONS = {".mp3", ".wav", ".flac", ".aac", ".ogg"}

    def validate(self, file_name: str) -> bool:
        _, ext = os.path.splitext(file_name)
        return ext.lower() in self.AUDIO_EXTENSIONS
