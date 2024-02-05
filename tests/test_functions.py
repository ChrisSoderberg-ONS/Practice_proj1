import practice_proj1.functions as functions
import pytest

def test_outdimensions_identity_function():
    assert functions.identity_function(6).size == 6*6