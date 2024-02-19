import pytest
import practice_proj1.functions as functions
from random import randrange

def test_outdimensions_identity_function():
    int_rand = randrange(1, 10)
    assert functions.identity_function(int_rand).size == int_rand * int_rand

def test_dataframe_multiply_identity_function():
    int_rand1 = randrange(1, 10)
    int_rand2 = randrange(1, 10)

    example_matrix = functions.random_dataframe(int_rand1, int_rand2)

    identity_matrix = functions.identity_function(example_matrix.shape[1])

    example_matrixI = functions.dataframe_multiply(example_matrix, identity_matrix)

    assert example_matrix.equals(example_matrixI)

def test_outdimensions_random_dataframe():
    int_rand1 = randrange(1, 10)
    int_rand2 = randrange(1, 10)

    example_matrix = functions.random_dataframe(int_rand1, int_rand2)

    assert (example_matrix.shape[0], example_matrix.shape[1]) == (int_rand1, int_rand2)

def test_outdimensions_dataframe_multiply():
    int_rand1 = randrange(1, 10)
    int_rand2 = randrange(1, 10)
    int_rand3 = randrange(1, 10)

    example_matrix_a = functions.random_dataframe(int_rand1, int_rand2)
    example_matrix_b = functions.random_dataframe(int_rand2, int_rand3)

    example_matrix_ab = functions.dataframe_multiply(example_matrix_a, example_matrix_b)

    assert (example_matrix_ab.shape[0], example_matrix_ab.shape[1]) == (int_rand1, int_rand3)