# utils/media_utils.py
def identify_media_type(file_path: str) -> str:
    """
    Determines the media type (video, audio, image) based on file extension.

    Args:
        file_path (str): The full file path.

    Returns:
        str: Media type identifier - video, audio, image, or unknown.
    """
    if file_path.lower().endswith(('.mp4', '.mkv', '.avi')):
        return "video"
    elif file_path.lower().endswith(('.mp3', '.wav')):
        return "audio"
    elif file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
        return "image"
    else:
        return "unknown"
