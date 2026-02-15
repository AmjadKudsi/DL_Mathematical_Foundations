# find and print the number of rows and columns in this matrix

import numpy as np

# Define the matrix
matrix = np.array([
    [8, 9, 3],
    [4, 2, 7],
    [6, 1, 5],
    [3, 9, 8]
])

# Number of rows
num_rows = matrix.shape[0]

# TODO: Find out number of columns
num_cols = matrix.shape[1]

# TODO: Display the number of rows and columns
print("Number of rows: ", num_rows)
print("Number of columns: ", num_cols)