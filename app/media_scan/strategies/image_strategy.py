from app.media_scan.strategies.media_validation_strategy import MediaValidationStrategy
import os


class ImageValidationStrategy(MediaValidationStrategy):
    """
    Validation strategy for image files based on file extensions.
    """

    IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".gif"}

    def validate(self, file_name: str) -> bool:
        _, ext = os.path.splitext(file_name)
        return ext.lower() in self.IMAGE_EXTENSIONS
