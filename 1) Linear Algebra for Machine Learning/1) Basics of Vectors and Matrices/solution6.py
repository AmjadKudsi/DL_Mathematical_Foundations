# combine two 2x2 matrices into a 3D matrix, which is just multiple 2D matrices stacked together

import numpy as np

# Define matrix A
A = [
    [1, 2],
    [3, 4]
]

# Define matrix B
B = [
    [5, 6],
    [7, 8]
]

# TODO: Create a 3D matrix to combine A and B. To do it, simply put matrices A and B into one list and then transform it into a numpy array with np.array
# TODO: Print the 3D matrix

print("Resulting Matrix:")
print(np.array([A, B]))