import sys
import os

# Add the root directory to Python's search path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dal.database import initialize_database, Base
from app.media_scan.media_scan_service import MediaScanApp
from app.media_scan.validation_strategy import (
    VideoValidationStrategy,
    AudioValidationStrategy,
    ImageValidationStrategy,
    CompositeValidationStrategy,
)

if __name__ == "__main__":
    try:
        # Initialize the database schema
        initialize_database(Base)

        # Initialize media validation strategies
        strategies = {
            "video": VideoValidationStrategy(),
            "audio": AudioValidationStrategy(),
            "image": ImageValidationStrategy(),
        }
        composite_strategy = CompositeValidationStrategy(strategies)

        # Initialize main application logic
        app = MediaScanApp(composite_strategy)
        user_input_path = input(
            "Please input the directory path to scan for media files: "
        ).strip()

        if not user_input_path:
            print("Error: Directory path cannot be empty.")
            sys.exit(1)

        print("Starting directory scan & database processing...")
        app.execute_and_save_to_db(user_input_path)
        print("Directory scan completed successfully.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)  # Exit with an error status code
