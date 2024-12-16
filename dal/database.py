import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

# Load environment variables
load_dotenv()

# Retrieve database URL, raise an error if not set
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise EnvironmentError("DATABASE_URL environment variable is required but not set.")

# Define Base (single instance)
Base = declarative_base()

# Configure database
engine = create_engine(DATABASE_URL, echo=True)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def initialize_database(base):
    """
    Ensures all tables defined in the Base metadata are created.
    Args:
        base: Declarative base containing table definitions
    """
    base.metadata.create_all(bind=engine)
    print("Database initialized.")
