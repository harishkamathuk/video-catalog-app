from app.media_scan.strategies.media_validation import MediaValidationStrategy
class ImageValidationStrategy(MediaValidationStrategy):
    """
    A validation strategy for image files that checks the file extension.

    This strategy determines whether a given file is a valid image file by checking its 
    extension against a predefined set of valid image file extensions. It incorporates robust 
    validation logic and error handling to reject invalid filenames, paths, or malformed inputs. 

    The validation logic specifically accounts for:
    - Filenames with path-like patterns (e.g., '/path/to/file' or '\\path').
    - Filenames with invalid patterns (e.g., multiple dots, repeated dots, filenames with no name before the extension).
    - Edge cases such as filenames that contain only an extension (e.g., `.jpg`) without a valid base name.

    Attributes:
        IMAGE_EXTENSIONS (set): A predefined set of valid image file extensions.

    Methods:
        validate(file_name: str) -> bool:
            Determines whether the provided file name corresponds to a valid image file based on:
            - Extension matching against `IMAGE_EXTENSIONS`.
            - Exclusion of invalid filenames or patterns (e.g., paths, malformed filenames, multiple dots).

    Example:
        strategy = ImageValidationStrategy()
        strategy.validate("picture.jpg")  # Returns True
        strategy.validate("document.txt")  # Returns False
        strategy.validate("..//path.jpg")  # Returns False
        strategy.validate(".jpg")  # Returns False due to invalid filename structure.

    Notes:
        - The method will return `False` for filenames with invalid patterns, malformed paths, or unsupported extensions.
        - This is designed to prevent misuse, invalid files, or security issues by rejecting invalid filenames upfront.
    """

    IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff"}

    def validate(self, file_name: str) -> bool:
        """
        Validates the provided file name to determine if it corresponds to a valid image file.

        The validation logic checks:
        1. Whether the filename is empty or malformed.
        2. Whether the filename contains path-like characters (e.g., '/' or '\\') indicating a directory traversal attempt.
        3. Whether the filename has invalid patterns like consecutive dots, or multiple dots.
        4. Whether the final extension is in the predefined `IMAGE_EXTENSIONS` list.

        Args:
            file_name (str): The name of the file to validate.

        Returns:
            bool: 
                - `True` if the filename has a valid image file extension and passes all validation checks.
                - `False` otherwise, such as for invalid filenames, path-like strings, or unsupported extensions.

        Example:
            - `validate("picture.jpg")` will return `True`.
            - `validate("document.txt")` will return `False`.
            - `validate("..//path.jpg")` will return `False`.
            - `validate(".jpg")` will return `False` due to missing a valid base name.

        Edge Cases Handled:
            - Empty filenames.
            - Filenames with directory paths or escape sequences (`/`, `\\`).
            - Filenames with invalid patterns like multiple dots.
            - Filenames that have only the extension without any valid name preceding it.
        """
        # Reject invalid filenames or patterns
        if not file_name:
            return False  # Empty string is invalid
        if '/' in file_name or '\\' in file_name:  # Prevent path-like strings
            return False
        if '..' in file_name:  # Reject filenames with consecutive dots
            return False
        if file_name.count('.') != 1:  # Reject filenames with multiple dots
            return False

        # Split and validate only the final extension
        try:
            name, ext = file_name.rsplit('.', 1)  # Split only at the last dot
            
            if name is None or name.strip() == "":  # Reject a filename that only has an extension
                return False
            if f".{ext.lower()}" in self.IMAGE_EXTENSIONS:
                return True
            return False
        except ValueError:
            # Handle edge cases when splitting fails
            return False
        
