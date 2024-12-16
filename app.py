from utils.directory_scanner import DirectoryScanner
from app.video_scan.extension_strategy import ExtensionValidationStrategy
from models.video import Video
from dal.database import SessionLocal
import os


class VideoScanApp:
    """
    Main application entry point logic.
    """

    def __init__(self):
        """
        Initialize with directory scanner dependency.
        """
        self.scanner = DirectoryScanner(ExtensionValidationStrategy())

    def execute_and_save_to_db(self, directory_path: str):
        """
        Scans directory and saves valid videos into database.
        Args:
            directory_path (str): Directory to scan.
        """
        session = SessionLocal()
        try:
            for video_file in self.scanner.scan(directory_path):
                # Attempt to save each valid file to database
                self.add_video_to_db(session, video_file)
        except Exception as e:
            print(f"Error during database saving: {e}")
        finally:
            session.close()

    def add_video_to_db(self, session, file_path: str):
        """
        Handles database insertion logic.
        Args:
            session: Database session
            file_path (str): Valid video file path
        """
        try:
            new_video = Video(
                file_name=os.path.basename(file_path),
                file_path=file_path,
                file_size=os.path.getsize(file_path),
                duration=0.0,  # Placeholder logic - compute dynamically later if needed
                resolution="Unknown",
                frame_rate=0.0,
                codec="Unknown",
                bitrate=0,
                thumbnail_path="Unknown",
            )
            session.add(new_video)
            session.commit()
            print(f"Video successfully added to database: {file_path}")
        except Exception as e:
            print(f"Failed to add video to database: {file_path}, Error: {e}")
