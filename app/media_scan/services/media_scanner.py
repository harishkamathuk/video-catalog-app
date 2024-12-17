import os
from app.media_scan.repositories.media_repository import MediaRepository
from utils.directory_scanner import DirectoryScanner
from app.media_scan.services.media_type import MediaTypeService
from dal.database import SessionLocal
from app.exceptions.media_exceptions import MediaAlreadyExistsError


class MediaScanner:
    """Main application logic for scanning and processing media files."""

    def __init__(self):
        self.session = SessionLocal()
        self.media_repository = MediaRepository(self.session)

    def execute_and_save_to_db(self, directory_path: str):
        """
        Scan the directory for valid media files and attempt to save their metadata into the database.
        Args:
            directory_path (str): Directory to scan.
        """
        # Initialize directory scanner with media validation logic
        scanner = DirectoryScanner(validation_strategy=MediaTypeService())
        
        try:
            for media_file_path in scanner.scan(directory_path):
                try:
                    media_type = MediaTypeService.identify(media_file_path)
                    if media_type == "unknown":
                        continue  # Skip unsupported media types
                    media_data = {
                        "file_name": os.path.basename(media_file_path),
                        "file_path": media_file_path,
                        "file_size": os.path.getsize(media_file_path),
                        "media_type": media_type,
                        "created_at": None,
                        "modified_at": None,
                        "duration": 0.0,
                        "resolution": "Unknown",
                        "frame_rate": 0.0,
                        "codec": "Unknown",
                        "bitrate": 0,
                        "thumbnail_path": "Unknown"
                    }

                    # Save the data to the database
                    self.media_repository.add_media(media_data)
                    print(f"Media added: {media_file_path}")
                except MediaAlreadyExistsError as e:
                    print(f"Skipping media due to duplicate: {e}")
                except Exception as e:
                    print(f"Unexpected error processing {media_file_path}: {e}")

        except Exception as e:
            print(f"Error during scanning process: {e}")
