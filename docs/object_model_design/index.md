# Object Model approach

1. Database interactions.
2. Data representation in business logic.
3. Compatibility with frameworks like Alembic for migrations.

Here’s an updated approach for a reusable design:

---

## **Improvements**

1. **Modular Design:**
   - Create a dedicated `models` module for object models.
   - Define data models in a way that they can be reused in APIs, GUI, and other layers.

2. **Use Data Access Layer (DAL):**
   - Abstract database operations in a separate layer for better encapsulation.

3. **Decouple Metadata:**
   - Ensure the SQLAlchemy `Base` and metadata are modular and easily importable for migrations.

---

## **Updated Implementation**

Here’s how you can refactor your project:

#### **Project Structure**

```plaintext
project/
├── alembic/                # Alembic migrations
├── models/                 # Object models
│   ├── __init__.py         # Initializes the module
│   └── video.py            # Video model definition
├── dal/                    # Data Access Layer
│   ├── __init__.py         # Initializes the module
│   └── database.py         # Database connection logic
├── alembic.ini             # Alembic configuration
├── main.py                 # Application entry point
└── requirements.txt        # Dependencies
```

#### **`models/video.py`**

```python
from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, Text
from sqlalchemy.orm import declarative_base

# Initialize SQLAlchemy Base
Base = declarative_base()

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
```

---

#### **`dal/database.py`**

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///video_metadata.db"

# Create an SQLite engine
engine = create_engine(DATABASE_URL)

# Create a configured session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def initialize_database(Base):
    """Creates the database tables."""
    Base.metadata.create_all(bind=engine)
    print("Database initialized.")
```

---

#### **`alembic/env.py`**

Update the `env.py` file to reference the `Base` metadata from the `models` module:

```python
import sys
from pathlib import Path

# Add project root to the system path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from models.video import Base

# Assign metadata for Alembic migrations
target_metadata = Base.metadata
```

---

#### **`main.py`**

Example of how to initialize the database and use the models:

```python
from dal.database import initialize_database, engine
from models.video import Base, Video

if __name__ == "__main__":
    # Initialize the database
    initialize_database(Base)

    # Example: Create a new video object (business logic layer)
    session = SessionLocal()
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
```

---

### **Benefits of This Approach**

1. **Reusability:**
   - Models can be used across multiple layers (e.g., APIs, GUI, data processing).
2. **Encapsulation:**
   - Database operations are abstracted into the DAL.
3. **Scalability:**
   - Modular structure allows easy addition of new features or database objects.
4. **Migrations:**
   - Seamless integration with Alembic for schema evolution.
