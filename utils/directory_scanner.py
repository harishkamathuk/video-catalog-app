import os
import logging


logging.basicConfig(
    filename="logs/media_scan.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class DirectoryScanner:
    """
    Handles scanning directories for valid media files and yields results.
    """

    def __init__(self, validation_strategy):
        """
        Initialize the scanner with a specific validation strategy.
        
        Args:
            validation_strategy: Strategy or a dictionary of strategies for validation logic.
        """
        self.validation_strategy = validation_strategy

    def identify_media_type(self, file_name: str):
        """
        Identifies the media type based on file extension.

        Args:
            file_name (str): Name of the file.

        Returns:
            str: Media type (e.g., 'video', 'audio', 'image') or None if unsupported.
        """
        # Directly call the composite strategy's validation logic
        media_type = self.validation_strategy.validate(file_name)
        return media_type  # Either "video", "audio", "image", or None


    def scan(self, directory_path: str):
        """
        Scans directory and yields valid media file paths and their media types.

        Args:
            directory_path (str): Directory to scan.

        Yields:
            tuple: (str, str): Full path to valid media file, Media type.
        """
        if not os.path.exists(directory_path):
            logging.error(f"Directory path does not exist: {directory_path}")
            print("Invalid directory path. Please check and try again.")
            return

        for root, _, files in os.walk(directory_path):
            for file in files:
                full_path = os.path.join(root, file)
                media_type = self.identify_media_type(file)
                if media_type:
                    print(f"Valid {media_type} file: {full_path}")
                    yield full_path, media_type
                else:
                    logging.info(f"Invalid or unsupported file type: {full_path}")
