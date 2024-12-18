from app.media_scan.strategies.media_strategy import MediaValidationStrategy


class AudioValidationStrategy(MediaValidationStrategy):
    """
    A validation strategy for audio files that checks the file extension.

    This strategy determines whether a given file is a valid audio file
    based on its extension. Supported audio extensions are defined in
    the `AUDIO_EXTENSIONS` set. It includes robust error handling to 
    manage edge cases, such as invalid filenames that do not contain 
    a proper extension.

    Attributes:
        AUDIO_EXTENSIONS (set): A set of supported audio file extensions.

    Methods:
        validate(file_name: str) -> bool:
            Validates the file name by checking if its extension is in
            the `AUDIO_EXTENSIONS` set. If the filename is invalid or
            does not conform to expected formats, it returns False.

    Example:
        strategy = AudioValidationStrategy()
        is_valid = strategy.validate("example.mp3")  # Returns True
        is_valid = strategy.validate("example.txt")  # Returns False
        is_valid = strategy.validate("invalid_file")  # Returns False due to missing extension
    """

    AUDIO_EXTENSIONS = {".mp3", ".wav", ".flac", ".aac", ".ogg"}

    def validate(self, file_name: str) -> bool:
        """
        Validate the provided file name to determine if it is a valid audio file.

        This method attempts to split the provided filename by '.' to extract
        and validate its extension. It includes error handling to manage filenames
        without proper extensions or malformed formats.

        Args:
            file_name (str): The name of the file to validate.

        Returns:
            bool: 
                - True if the file has a valid audio extension.
                - False if the filename is invalid, the extension is unsupported, 
                  or the file cannot be processed correctly.

        Raises:
            ValueError: Caught internally when splitting a malformed file name.

        Example:
            validate("example.mp3")  # Returns True
            validate("example.txt")  # Returns False
            validate("invalid_file")  # Returns False due to invalid or missing extension
        """
        try:
            # Attempt to split and check the extension
            _, ext = file_name.rsplit('.', 1)
            return f".{ext.lower()}" in self.AUDIO_EXTENSIONS
        except ValueError:
            # Catch edge cases where splitting fails
            return False
