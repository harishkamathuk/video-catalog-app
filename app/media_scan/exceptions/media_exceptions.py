class MediaAlreadyExistsError(Exception):
    """Raised when a media file already exists in the database."""
    pass

class MediaTypeNotFoundError(Exception):
    """Raised when a requested media type is not found."""
    pass

class VideoAlreadyExistsError(Exception):
    """Raised when trying to insert a duplicate video into the database."""
    pass
