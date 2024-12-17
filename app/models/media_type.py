from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MediaType(Base):
    """
    MediaType table for normalization to categorize types of media (audio, video, image, etc.)
    """
    __tablename__ = "media_type"

    id = Column(Integer, primary_key=True, autoincrement=True)  # Primary key for reference
    name = Column(String, nullable=False, unique=True)  # Media type name (e.g., video, image)
