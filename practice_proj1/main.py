from practice_proj1.functions import *

def main():
    """
    Example usage code
    """
    matrix_a = random_dataframe(5,4)
    matrix_b = random_dataframe(4,5)

    print("Matrix A\n", matrix_a, "\n")
    print("Matrix B\n", matrix_b, "\n")

    matrix_ab = dataframe_multiply(matrix_a, matrix_b)

    print("Matrix AB\n", matrix_ab, "\n")

    matrix_I = identity_function(matrix_ab.shape[1])
    matrix_abI = dataframe_multiply(matrix_ab, matrix_I)

    print("Matrix ABI = Matrix AB\n", matrix_abI, "\n")

if __name__ == "__main__":
    main()