from video_scan.directory_scanner import DirectoryScanner
from video_scan.extension_strategy import ExtensionValidationStrategy


class VideoScanApp:
    """
    Main application entry point logic.
    """

    def __init__(self):
        """
        Initialize with directory scanner dependency.
        """
        self.scanner = DirectoryScanner(ExtensionValidationStrategy())

    def execute(self):
        """
        Handles user input and runs the scanning process.
        """
        user_input = input("Please input the directory path to scan for video files: ").strip()
        self.scanner.scan(user_input)
