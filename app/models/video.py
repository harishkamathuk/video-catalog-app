from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, Text
from sqlalchemy.orm import declarative_base
from dal.database import Base  # Import shared Base instance
class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    file_name = Column(String, nullable=False)
    file_path = Column(Text, nullable=False, unique=True)
    file_size = Column(Integer)
    created_at = Column(TIMESTAMP)
    modified_at = Column(TIMESTAMP)
    duration = Column(Float)
    resolution = Column(String)
    frame_rate = Column(Float)
    codec = Column(String)
    bitrate = Column(Integer)
    thumbnail_path = Column(Text)

    def to_dict(self):
        """Convert the Video object into a dictionary for API responses or UI."""
        return {
            "id": self.id,
            "file_name": self.file_name,
            "file_path": self.file_path,
            "file_size": self.file_size,
            "created_at": self.created_at,
            "modified_at": self.modified_at,
            "duration": self.duration,
            "resolution": self.resolution,
            "frame_rate": self.frame_rate,
            "codec": self.codec,
            "bitrate": self.bitrate,
            "thumbnail_path": self.thumbnail_path,
        }
