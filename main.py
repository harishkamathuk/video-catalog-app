import sys
import os

# Add the root directory to Python's search path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dal.database import initialize_database, Base
from app.video_scan.video_scan_service import VideoScanApp

if __name__ == "__main__":
    try:
        # Initialize the database schema
        initialize_database(Base)

        # Initialize main application logic
        app = VideoScanApp()
        user_input_path = input(
            "Please input the directory path to scan for video files: "
        ).strip()
        print("Starting directory scan & database processing...")
        app.execute_and_save_to_db(user_input_path)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)  # Exit with an error status code
