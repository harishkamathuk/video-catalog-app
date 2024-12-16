import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve and validate required environment variables
LOG_LEVEL = os.getenv("LOG_LEVEL")
if not LOG_LEVEL:
    raise EnvironmentError("LOG_LEVEL environment variable is required but not set.")

# Configure logging
logging.basicConfig(level=getattr(logging, LOG_LEVEL.upper(), logging.INFO))

# Your existing imports and logic
from app import VideoScanApp
from dal.database import initialize_database, Base

if __name__ == "__main__":
    try:
        # Initialize database
        initialize_database(Base)

        # Run application logic
        app = VideoScanApp()
        user_input_path = input(
            "Please input the directory path to scan for video files: "
        ).strip()
        print("Starting directory scan & database processing...")
        app.execute_and_save_to_db(user_input_path)
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        sys.exit(1)
