# FILE: app/media_scan/strategies/test_media_validation.py

import pytest

from abc import ABCMeta
from app.media_scan.strategies.media_validation import MediaValidationStrategy

def test_media_validation_strategy_abstract():
    """
    Test that instantiating the abstract class MediaValidationStrategy raises a TypeError.

    This test ensures that the MediaValidationStrategy class cannot be instantiated directly,
    as it is intended to be an abstract base class. The test will pass if a TypeError is raised
    when attempting to create an instance of MediaValidationStrategy.
    """
    with pytest.raises(TypeError):
        MediaValidationStrategy()

def test_media_validation_strategy_validate():
    """
    Test the validate method of the DummyMediaValidationStrategy class.
    This test creates a dummy implementation of the MediaValidationStrategy
    class, where the validate method always returns True. It then asserts
    that the validate method returns True when called with a dummy file name.
    """
    class DummyMediaValidationStrategy(MediaValidationStrategy):
        def validate(self, file_name: str) -> bool:
            return True

    strategy = DummyMediaValidationStrategy()
    assert strategy.validate("dummy_file") == True
    
def test_media_validation_strategy_subclass_must_implement_validate():
    """
    This test defines an incomplete subclass of MediaValidationStrategy that does not implement
    the required validate method. It then asserts that calling the validate method on an instance
    of this subclass raises a NotImplementedError, which is the expected behavior when an abstract
    method is not implemented.
    Raises:
        NotImplementedError: If the subclass does not implement the validate method.
    """
    class IncompleteValidationStrategy(MediaValidationStrategy):
        def validate(self, file_name: str) -> bool:
            return super().validate(file_name)

    strategy = IncompleteValidationStrategy()
    with pytest.raises(NotImplementedError):
        strategy.validate("dummy_file")
