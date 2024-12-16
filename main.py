from dal.database import initialize_database, SessionLocal, engine
from models.video import Base, Video
import os


if __name__ == "__main__":
    # Initialize database schema
    initialize_database(Base)

    # Example: Create a new video object (business logic layer)
    with SessionLocal() as session:
        new_video = Video(
            file_name="example.mp4",
            file_path="/path/to/example.mp4",
            file_size=102400,
            duration=300.0,
            resolution="1920x1080",
            frame_rate=30.0,
            codec="H.264",
            bitrate=4500,
            thumbnail_path="/path/to/thumbnail.png",
        )
        session.add(new_video)
        session.commit()
        print("Video added to the database.")
