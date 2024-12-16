import os
import logging


logging.basicConfig(
    filename="logs/video_scan.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class DirectoryScanner:
    """
    Handles scanning directories for valid video files and yields results.
    """

    def __init__(self, validation_strategy):
        """
        Initialize the scanner with a specific validation strategy.
        Args:
            validation_strategy: Strategy for validation logic.
        """
        self.validation_strategy = validation_strategy

    def scan(self, directory_path: str):
        """
        Scans directory and yields valid video file paths.

        Args:
            directory_path (str): Directory to scan.

        Yields:
            str: Full path to valid video file.
        """
        if not os.path.exists(directory_path):
            logging.error(f"Directory path does not exist: {directory_path}")
            print("Invalid directory path. Please check and try again.")
            return

        for root, _, files in os.walk(directory_path):
            for file in files:
                full_path = os.path.join(root, file)
                if self.validation_strategy.validate(file):
                    print(f"Valid video file: {full_path}")
                    yield full_path
                else:
                    logging.info(f"Invalid or unsupported file type: {full_path}")
