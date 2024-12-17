from app.media_scan.strategies.media_strategy import MediaValidationStrategy


class AudioValidationStrategy(MediaValidationStrategy):
    """
    Validation strategy for audio files based on file extensions.
    """
    
    AUDIO_EXTENSIONS = {".mp3", ".wav", ".flac", ".aac", ".ogg"}

    def validate(self, file_name: str) -> bool:
        _, ext = file_name.rsplit('.', 1)
        return f".{ext.lower()}" in self.AUDIO_EXTENSIONS
