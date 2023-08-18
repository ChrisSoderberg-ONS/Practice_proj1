# Top-level run code
import functions

def main():

    # Generate two dataframes: a, b
    df_a = functions.random_dataframe(5,3)
    df_b = functions.random_dataframe(3,8)

    # Display results
    print(df_a, '\n')
    print(df_b, '\n')

    # Create product a*b
    product_ab = functions.dataframe_multiply(df_a, df_b)

    # View product
    print(product_ab, '\n')
    
    # Create identity matrix compatible with a*b
    id_matrix_ab = functions.identity_function(product_ab.shape[1])

    # Verify a*b*I = a*b
    print(id_matrix_ab, '\n')

    print(functions.dataframe_multiply(product_ab, id_matrix_ab))


if __name__ == '__main__':
    main()