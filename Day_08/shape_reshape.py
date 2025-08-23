import numpy as np

# The "shape" of an array, matrix, or tensor refers to the size of each of its dimensions. 

arr = np.array([[1, 2, 3], [4, 5, 6]])

# The shape of the array is (2, 3), meaning it has 2 rows and 3 columns.
print("Original array:")
print(arr)
print("Shape of the array:", arr.shape, "\n")

# The shape can be changed using the reshape method.
reshaped_arr = arr.reshape(3, 2)
print("Reshaped array:")
print(reshaped_arr, "\n")

# The new shape is (3, 2), meaning it has 3 rows and 2 columns.
print("Shape of the reshaped array:", reshaped_arr.shape)

# Reshaping does not change the data, just the way it is viewed.
# The original array can still be accessed. 