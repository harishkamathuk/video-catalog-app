from dal.database import Base  # Import Base from the single definition
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Session

class MediaType(Base):
    """
    MediaType table for normalization to categorize types of media (audio, video, image, etc.)
    """
    __tablename__ = "media_type"

    id = Column(Integer, primary_key=True, autoincrement=True)  # Primary key for reference
    name = Column(String, nullable=False, unique=True)  # Media type name (e.g., video, image)

    # Establish parent-child relationship
    media = relationship("Media", back_populates="media_type")

    @staticmethod
    def get_id_by_name(session: Session, media_type: str) -> int:
        """
        Static method to query the database for a MediaType ID based on the given string name.

        Args:
            session (Session): The database session.
            media_type (str): The media type string (e.g., 'video', 'audio').

        Returns:
            int: The ID of the media type in the database.
        """
        media_type_record = session.query(MediaType).filter_by(name=media_type).first()
        if not media_type_record:
            raise ValueError(f"Media type '{media_type}' is not registered in the database.")
        return media_type_record.id