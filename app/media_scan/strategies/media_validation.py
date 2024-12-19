from abc import ABC, abstractmethod


class MediaValidationStrategy(ABC):
    """
    Abstract base class for any media validation strategy.
    """

    @abstractmethod
    def validate(self, file_name: str) -> bool:
        raise NotImplementedError("You must implement the validate method.")
