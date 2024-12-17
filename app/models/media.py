from sqlalchemy import Column, Integer, String, BigInteger, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from dal.database import Base  # Import Base from the single definition

class Media(Base):
    """
    Generalized Media model linked to the media_type table.
    """
    __tablename__ = "media"

    id = Column(Integer, primary_key=True, autoincrement=True)
    file_path = Column(String, nullable=False, unique=True)  # Path to media file
    file_size = Column(BigInteger, nullable=False)  # Size in bytes
    media_type_id = Column(Integer, ForeignKey("media_type.id"), nullable=False)  # Reference to media_type - establish ForeignKey relationship
    duration = Column(Float)  # Media duration in seconds
    resolution = Column(String)  # Resolution as "widthxheight" (example: 1920x1080)
    codec = Column(String)  # Codec type (e.g., H.264, MP3)
    bit_rate = Column(BigInteger)  # Bit rate in bits per second
    date_created = Column(DateTime)  # When the file/media was created
    media_type = relationship("MediaType", back_populates="media")

