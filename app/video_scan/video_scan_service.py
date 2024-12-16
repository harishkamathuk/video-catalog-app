import os
from video_repository import VideoRepository
from exceptions import VideoAlreadyExistsError
from dal.database import SessionLocal


class VideoScanApp:
    """Main application logic for scanning and processing video files."""

    def __init__(self):
        self.session = SessionLocal()
        self.video_repository = VideoRepository(self.session)

    def execute_and_save_to_db(self, directory_path):
        """
        Scan the directory for valid video files and attempt to save their metadata into the database.
        """
        if not os.path.exists(directory_path):
            print(f"Error: Directory '{directory_path}' does not exist.")
            return

        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Assuming basic validation for video extensions here
                if file.lower().endswith(('.mp4', '.mkv', '.avi')):
                    try:
                        print(f"Valid video file: {file_path}")
                        video_data = {
                            "file_name": file,
                            "file_path": file_path,
                            "file_size": os.path.getsize(file_path),
                            "created_at": None,
                            "modified_at": None,
                            "duration": 0.0,
                            "resolution": "Unknown",
                            "frame_rate": 0.0,
                            "codec": "Unknown",
                            "bitrate": 0,
                            "thumbnail_path": "Unknown"
                        }
                        self.video_repository.add_video(video_data)
                    except VideoAlreadyExistsError as e:
                        print(f"Skipping video due to duplicate: {e}")
                    except Exception as e:
                        print(f"Unexpected error processing {file_path}: {e}")
