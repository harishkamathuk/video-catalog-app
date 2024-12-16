from app import VideoScanApp
from dal.database import SessionLocal
from models.video import Video


def add_video_to_db(file_path: str):
    """
    Adds a valid video file to the database.
    Args:
        file_path (str): Path of the video file to add to the database.
    """
    session = SessionLocal()
    try:
        new_video = Video(
            file_name=file_path.split("/")[-1],
            file_path=file_path,
            file_size=os.path.getsize(file_path),
            duration=0.0,  # Placeholder; compute duration if needed
            resolution="Unknown",  # Placeholder
            frame_rate=0.0,  # Placeholder
            codec="Unknown",  # Placeholder
            bitrate=0,  # Placeholder
            thumbnail_path="Unknown",
        )
        session.add(new_video)
        session.commit()
        print(f"Video successfully added to database: {file_path}")
    except Exception as e:
        print(f"Could not add to database: {e}")
    finally:
        session.close()


if __name__ == "__main__":
    app = VideoScanApp()
    # User inputs directory path
    directory_to_scan = input(
        "Please input the directory path to scan for video files: "
    ).strip()
    print("Scanning directory...")
    for video_file in app.execute_and_get_video_files(directory_to_scan):
        # Add the video to database if it's valid
        add_video_to_db(video_file)
