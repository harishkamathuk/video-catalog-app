import os

from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

from app.media_scan.config.settings import config

# Define Base (single instance)
Base = declarative_base()

# Configure database i.e. SQLAlchemy setup with environment configuration
engine = create_engine(config.DATABASE_URL, echo=config.LOG_LEVEL == "DEBUG")

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def initialize_database(base):
    """
    Ensures all tables defined in the Base metadata are created.
    Args:
        base: Declarative base containing table definitions
    """
    base.metadata.create_all(bind=engine)
    # print("Database initialized.")
