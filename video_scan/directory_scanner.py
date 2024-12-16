import os
import logging


logging.basicConfig(
    filename="logs/video_scan.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class DirectoryScanner:
    """
    Handles scanning directories for valid/invalid video files.
    """

    def __init__(self, validation_strategy):
        """
        Initializes DirectoryScanner with a validation strategy.

        Args:
            validation_strategy: Strategy for validation logic.
        """
        self.validation_strategy = validation_strategy

    def scan(self, directory_path: str):
        """
        Scans a given directory for valid video files and logs invalid ones.

        Args:
            directory_path (str): The directory path to scan.
        """
        if not os.path.exists(directory_path):
            logging.error(f"Directory path does not exist: {directory_path}")
            print("Invalid directory path. Please check and try again.")
            return

        print(f"Scanning directory: {directory_path}")
        for root, _, files in os.walk(directory_path):
            for file in files:
                if self.validation_strategy.validate(file):
                    print(f"Valid video file found: {os.path.join(root, file)}")
                else:
                    logging.info(f"Unsupported or invalid file type: {os.path.join(root, file)}")
                    print(f"Unsupported file type: {os.path.join(root, file)}")

        print("\nScan completed.")
