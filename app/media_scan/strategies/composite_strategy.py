from app.media_scan.strategies.audio_strategy import AudioValidationStrategy
from app.media_scan.strategies.video_strategy import VideoValidationStrategy
from app.media_scan.strategies.image_strategy import ImageValidationStrategy
from app.media_scan.strategies.default_strategy import DefaultValidationStrategy


class CompositeValidationStrategy:
    """
    Composite strategy to dynamically validate multiple types of media
    with a fallback for unsupported media types.
    """

    def __init__(self):
        self.strategies = {
            "audio": AudioValidationStrategy(),
            "video": VideoValidationStrategy(),
            "image": ImageValidationStrategy(),
            "default": DefaultValidationStrategy(),
        }

    def validate(self, file_name: str) -> str:
        """
        Validate a file and return its media type or fallback to default.

        Args:
            file_name (str): The file name to validate.

        Returns:
            str: Media type if found, otherwise 'unknown'.
        """
        for media_type, strategy in self.strategies.items():
            if media_type != "default" and strategy.validate(file_name):
                return media_type
        
        # If no type matches, call the default fallback strategy.
        self.strategies["default"].validate(file_name)
        return "unknown"
