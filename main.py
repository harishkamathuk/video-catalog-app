from app import VideoScanApp
from models.video import Video  # Import the model to ensure it is registered
from dal.database import initialize_database, Base, engine
import sys

if __name__ == "__main__":
    try:
        # Initialize database and ensure tables exist
        initialize_database(Base)

        # Execute application logic
        app = VideoScanApp()
        user_input_path = input(
            "Please input the directory path to scan for video files: "
        ).strip()
        print("Starting directory scan & database processing...")
        app.execute_and_save_to_db(user_input_path)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)  # Exit with an error status code
        
