from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import relationship

from app.models import Base

class MediaType(Base):
    """
    MediaType table for normalization to categorize types of media (audio, video, image, etc.)
    """
    __tablename__ = "media_type"

    id = Column(Integer, primary_key=True, autoincrement=True)  # Primary key for reference
    name = Column(String, nullable=False, unique=True)  # Media type name (e.g., video, image)

    # Establish parent-child relationship
    media = relationship("Media", back_populates="media_type")

