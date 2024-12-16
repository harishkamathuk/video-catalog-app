import os
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

# Ensure the 'data' directory exists for database storage
# TODO Move the location of the database to environment variable
db_directory = os.path.join(os.getcwd(), "database")
os.makedirs(db_directory, exist_ok=True)  # Create the directory if it doesn't exist

# Define Base (single instance)
Base = declarative_base()

# Path to SQLite database
db_path = os.path.join(db_directory, "video_metadata.db")
DATABASE_URL = f"sqlite:///{db_path}"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a configured session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def initialize_database(base):
    """
    Ensures all tables defined in Base metadata are created.
    Args:
        base: Declarative base containing table definitions
    """
    base.metadata.create_all(bind=engine)
    print("Database initialized at:", db_path)
