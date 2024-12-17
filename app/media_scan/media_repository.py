from sqlalchemy.exc import IntegrityError
from dal.database import SessionLocal
from app.models.media import Media
from app.models.media_type import MediaType
from app.exceptions.media_exceptions import MediaAlreadyExistsError, MediaTypeNotFoundError


class MediaRepository:
    """Repository pattern to handle database transactions for media."""

    def __init__(self, session=None):
        # Use a provided session or create a new one for standalone operations
        self.session = session or SessionLocal()

    def add_media(self, media_data):
        """
        Insert a new media entry into the database.
        If a UNIQUE constraint fails (e.g., file_path already exists), raise a custom exception.
        """
        try:
            # Map data into a Media model instance
            media = Media(**media_data)
            self.session.add(media)
            self.session.commit()
            print("Media added successfully.")
            return media
        except IntegrityError:
            # Handle the case where insertion fails due to a duplicate file_path
            self.session.rollback()
            raise MediaAlreadyExistsError(
                f"Media with path {media_data.get('file_path')} already exists in the database."
            )

    def get_media_by_id(self, media_id):
        """
        Retrieve a media entry by its ID.
        """
        return self.session.query(Media).filter(Media.id == media_id).first()

    def get_media_by_type(self, media_type_name):
        """
        Retrieve all media entries of a specific type (e.g., video, image).
        """
        media_type = self.session.query(MediaType).filter_by(name=media_type_name).first()
        if not media_type:
            raise MediaTypeNotFoundError(f"Media type '{media_type_name}' not found.")
        return self.session.query(Media).filter(Media.media_type_id == media_type.id).all()

    def update_media(self, media_id, updates):
        """
        Update an existing media entry by ID.
        """
        media = self.get_media_by_id(media_id)
        if not media:
            return None
        for key, value in updates.items():
            setattr(media, key, value)
        self.session.commit()
        print(f"Media with ID {media_id} updated successfully.")
        return media

    def delete_media(self, media_id):
        """
        Delete a media entry by ID.
        """
        media = self.get_media_by_id(media_id)
        if not media:
            return None
        self.session.delete(media)
        self.session.commit()
        print(f"Media with ID {media_id} deleted successfully.")
