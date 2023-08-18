# Top-level run code
import functions

def main():

    df_a = functions.random_dataframe(5,3)
    df_b = functions.random_dataframe(3,2)

    print(df_a, '\n')
    print(df_b, '\n')

    product_ab = functions.dataframe_multiply(df_a, df_b)

    print(product_ab, '\n')
    
    id_matrix_ab = functions.identity_function(product_ab.shape[1])

    print(id_matrix_ab, '\n')

    print(functions.dataframe_multiply(product_ab, id_matrix_ab))


if __name__ == '__main__':
    main()