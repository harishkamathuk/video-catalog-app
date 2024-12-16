import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Ensure the 'data' directory exists for database storage
db_directory = os.path.join(os.getcwd(), "database")
os.makedirs(db_directory, exist_ok=True)

# Path to SQLite database
db_path = os.path.join(db_directory, "video_catalog.db")
engine = create_engine(f'sqlite:///{db_path}', echo=True)  # Point SQLite to the database path

# Create a configured session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def initialize_database(Base):
    """Initialize database schema."""
    Base.metadata.create_all(bind=engine)
    print("Database initialized.")
