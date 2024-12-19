# app/media_scan/services/media_scanner.py
import os
from app.media_scan.models.media_type import MediaType
from utils.directory_scanner import DirectoryScanner
from app.media_scan.dal.database import SessionLocal

from app.media_scan.services.media_type import MediaTypeService
from app.media_scan.repositories.media_repository import MediaRepository
from app.media_scan.strategies.composite_validation import CompositeValidationStrategy

from app.media_scan.exceptions.media_exceptions import MediaAlreadyExistsError


class MediaScanner:
    """
    Media scanner logic for scanning and processing media files.
    """

    def __init__(self, validation_strategy):
        """
        Accept the CompositeValidationStrategy to use during scanning.
        Args:
            validation_strategy: CompositeValidationStrategy instance.
        """
        self.session = SessionLocal()
        self.media_repository = MediaRepository(self.session)
        self.validation_strategy = validation_strategy

    def execute_and_save_to_db(self, directory_path: str):
        """
        Scan the directory for valid media files and attempt to save their metadata into the database.
        Args:
            directory_path (str): Directory to scan.
        """
        # Initialize directory scanner with media validation logic
        scanner = DirectoryScanner(validation_strategy=self.validation_strategy)
        
        try:
            for file_path, media_type in scanner.scan(directory_path):
                
                print(f"Processing {file_path} as type {media_type}")
                
                # Insert logic to handle database save based on media_type
                try:
                    # TODO This may be redundant check
                    # media_type = MediaTypeService.identify(file_path)
                    if media_type == "unknown":
                        continue  # Skip unsupported media types
                    # media_data = {
                    #     #TODO Add a file name attribute to the Media object
                    #     # "file_name": os.path.basename(file_path),
                    #     "file_path": file_path,
                    #     "file_size": os.path.getsize(file_path),
                    #     "media_type": media_type,
                    #     "created_at": None,
                    #     "modified_at": None,
                    #     "duration": 0.0,
                    #     "resolution": "Unknown",
                    #     "frame_rate": 0.0,
                    #     "codec": "Unknown",
                    #     "bitrate": 0,
                    #     "thumbnail_path": "Unknown"
                    # }
                    media_data = {
                        "file_path": file_path,
                        "file_size": os.path.getsize(file_path),
                        "media_type_id": MediaType.get_id_by_name(self.session, media_type),  # Use the static method here
                        "duration": 0.0,
                        "resolution": "Unknown",
                        "codec": "Unknown",
                        "bit_rate": 0,
                        "date_created": None,
                    }                    

                    # Save the data to the database
                    self.media_repository.add_media(media_data)
                    print(f"Media added: {file_path}")
                except MediaAlreadyExistsError as e:
                    print(f"Skipping media due to duplicate: {e}")
                except Exception as e:
                    print(f"Unexpected error processing {file_path}: {e}")

        except Exception as e:
            print(f"Error during scanning process: {e}")
