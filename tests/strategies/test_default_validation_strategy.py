import pytest
from app.media_scan.strategies.default_validation import DefaultValidationStrategy

def test_default_validation_strategy():
    """
    Test the DefaultValidationStrategy for unsupported file extensions.

    Asserts:
        False for a file name with an unsupported extension.
    """
    strategy = DefaultValidationStrategy()
    file_name = "unsupported_file.xyz"
    
    result = strategy.validate(file_name)
    
    assert result is False