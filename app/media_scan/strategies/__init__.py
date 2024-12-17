import sys
import os

# Dynamically add the root directory to the Python path to resolve absolute imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Make it easier to import strategies
from app.media_scan.strategies.video_strategy import VideoValidationStrategy
from app.media_scan.strategies.audio_strategy import AudioValidationStrategy
from app.media_scan.strategies.image_strategy import ImageValidationStrategy
from app.media_scan.strategies.composite_strategy import CompositeValidationStrategy


