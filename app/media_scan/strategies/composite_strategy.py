class CompositeValidationStrategy:
    """
    Composite strategy for managing multiple media validation strategies.
    """

    def __init__(self, strategies):
        """
        Initialize with a dictionary of media type -> validation strategy.

        Args:
            strategies (dict): A dictionary mapping media types to validation strategies.
        """
        self.strategies = strategies

    def validate(self, file_name: str) -> str:
        """
        Validate a file and return its media type if valid.

        Args:
            file_name (str): The file name to validate.

        Returns:
            str: The media type if valid, otherwise None.
        """
        for media_type, strategy in self.strategies.items():
            if strategy.validate(file_name):
                return media_type
        return None
