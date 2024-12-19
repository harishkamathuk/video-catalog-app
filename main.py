import sys
import os

# Add the root directory to Python's search path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dal.database import initialize_database, Base
from app.media_scan.services.media_scanner import MediaScanner
from app.media_scan.strategies.composite_validation import CompositeValidationStrategy


if __name__ == "__main__":
    try:
        # Initialize database schema
        initialize_database(Base)

        # Dynamically create composite strategy
        composite_strategy = CompositeValidationStrategy()

        # Initialize MediaScanner with the strategy
        app = MediaScanner(composite_strategy)

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
