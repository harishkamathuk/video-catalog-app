from app.media_scan.strategies.media_strategy import MediaValidationStrategy

class ImageValidationStrategy(MediaValidationStrategy):
    """
    Validation strategy for image files based on file extensions.
    """
    
    IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".gif"}

    def validate(self, file_name: str) -> bool:
        _, ext = file_name.rsplit('.', 1)
        return f".{ext.lower()}" in self.IMAGE_EXTENSIONS
