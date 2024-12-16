from sqlalchemy.exc import IntegrityError
from dal.database import SessionLocal
from models.video import Video
from app.exceptions.video_exceptions import VideoAlreadyExistsError


class VideoRepository:
    """Repository pattern to handle database transactions for videos."""

    def __init__(self, session):
        self.session = session

    def add_video(self, video_data):
        """
        Attempt to insert a video into the database.
        If a UNIQUE constraint fails, raise a custom exception.
        """
        try:
            # Map data into a Video model instance
            video = Video(**video_data)
            self.session.add(video)
            self.session.commit()
            print("Video added successfully.")
        except IntegrityError:
            # Handle the case where insertion fails due to a duplicate file_path
            self.session.rollback()
            raise VideoAlreadyExistsError(
                f"Video with path {video.file_path} already exists in database."
            )
