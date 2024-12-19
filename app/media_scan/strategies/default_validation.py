from app.media_scan.strategies.media_validation import MediaValidationStrategy


class DefaultValidationStrategy(MediaValidationStrategy):
    """
    A catch-all strategy for unsupported or unknown file types.
    """

    def validate(self, file_name: str) -> bool:
        """
        This strategy is always false but acts as a fallback.
        Log unsupported media file types for debugging or auditing.
        """
        print(f"[WARNING] Unsupported media type detected: {file_name}")
        return False
