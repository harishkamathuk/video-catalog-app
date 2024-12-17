from abc import ABC, abstractmethod


class MediaValidationStrategy(ABC):
    """
    Abstract base class for any media validation strategy.
    """

    @abstractmethod
    def validate(self, file_name: str) -> bool:
        """
        Abstract method to validate a file name.

        Args:
            file_name (str): The file name to validate.

        Returns:
            bool: Whether the file is valid or invalid.
        """
        raise NotImplementedError("You must implement the validate method.")
