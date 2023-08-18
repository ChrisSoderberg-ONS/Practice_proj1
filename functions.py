# Imports

import pandas as pd
import numpy as np

# Functions

def dataframe_multiply(a, b):
## Implement matrix multiplication for two numeric dataframes a and b

    # check types - all data in a and b must be numeric
    # force convert data in each column to numeric (non numeric converts to null) and check notnull == True

    if(a.apply(lambda s: pd.to_numeric(s, errors='coerce').notnull().all()).all() == False |
       b.apply(lambda s: pd.to_numeric(s, errors='coerce').notnull().all()).all() == False):
        raise ValueError('Matrices cannot be multiplied - both matrices must be numeric')

    # check input dimensions: columns of a must equal rows of b
    if(a.shape[1] != b.shape[0]):
        raise ValueError('Matrices cannot be multiplied - dimensions are not valid')

    # if no error has been raised yet, matrices are numeric and can be multiplied

    # initialise empty df for product
    product = pd.DataFrame()

    # Let a be an m x n matrix
    # Let b be an n x p matrix

    n = a.shape[1]

    # dimensions of product matrix
    m = a.shape[0] # rows
    p = b.shape[1] # columns

    for i in range(0, m): # iterate over rows

        # initialise product row
        row = []

        for j in range(0, p): # iterate over columns

            # intialise dot product for position i,j
            dot_prod = 0

            # dot product summation
            for k in range(0, n):
                dot_prod = dot_prod + (a.iloc[i, k] * b.iloc[k, j])

            # append dot product for position i,j to current product column
            row.append(dot_prod)
        
        # convert completed product row to pandas series and append to product dataframe
        series = pd.Series(data = row)
        product = product.append(series, ignore_index = True)

    # output product
    product = product.convert_dtypes()

    return product

def random_dataframe(n, m):
## Returns a dataframe of random integers (0-10) with dimensions n x m

    # throw error for bad input
    if(n < 1 | m < 1):
        raise ValueError('Matrix cannot have zero or negative dimensions')
    
    # initialise empty df for output
    df = pd.DataFrame()

    # populate
    for i in range(0, n): # iterate over rows
        
        # initialise empty row
        row = []

        for i in range(0, m): # iterate over columns
            row.append(int(np.random.rand()*10)) # append random int (0-10)
        
        # convert row to pandas series and append to output df
        series = pd.Series(data = row)
        df = df.append(series, ignore_index = True)

    # output df
    df = df.convert_dtypes()

    return df

def identity_function(n):
## Given the parameter n, generate the n x n identity matrix as a dataframe

    # throw error for bad input
    if(n < 1):
        raise ValueError('Matrix cannot have zero or negative dimensions')

    # initialise empty dataframe
    df = pd.DataFrame()

    # populate
    for i in range(0, n):

        row = [0] * n

        # for the identity matrix the ith row will have index[i] = 1
        row[i] = 1

        series = pd.Series(data=row)

        df = df.append(series, ignore_index = True)
    
    # output df
    df = df.convert_dtypes()

    return df