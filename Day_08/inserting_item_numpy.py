# NumPy arrays are fixed-size, so you typically use np.insert() to create a new array with the element inserted.
# Syntax: np.insert(arr, index, value, axis=None)

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Original array:\n", arr)

# Insert a new row at index 1
arr_new = np.insert(arr, 1, [7, 8,9], axis=0)
print("New array:\n", arr_new)
