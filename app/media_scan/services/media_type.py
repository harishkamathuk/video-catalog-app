# app/media_scan/services/media_type_service.py
class MediaTypeService:
    @staticmethod
    def identify(file_path: str) -> str:
        """
        Determines the media type (video, audio, image) based on file extension.
        """
        if file_path.lower().endswith(('.mp4', '.mkv', '.avi')):
            return "video"
        elif file_path.lower().endswith(('.mp3', '.wav')):
            return "audio"
        elif file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            return "image"
        else:
            return "unknown"
