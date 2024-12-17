import sys
import os

# Add the project's root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.ext.declarative import declarative_base

# Define a single Base instance to use across the models
Base = declarative_base()

from app.models.media_type import MediaType
from app.models.media import Media

