# vectors and matrices at work in Python

import numpy as np

# Let's create and display vectors and matrices to see how it works

# Creating a row vector
row_vector = np.array([1, 2, 3])

# Creating a column vector
column_vector = np.array([
    [1],
    [2],
    [3]
])

# Creating a matrix
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Displaying the vectors and matrix
print("Row Vector:", row_vector)  # Output: Row Vector: [1 2 3]
print("Column Vector:\n", column_vector)  # Output: Column Vector: [[1] [2] [3]]
print("Matrix:\n", matrix)  # Output: Matrix: [[1 2 3] [4 5 6] [7 8 9]]