import functions
import pytest
import pandas as pd 

def test_outdimensions_identity_function():
    assert functions.identity_function(6).size == 6*6