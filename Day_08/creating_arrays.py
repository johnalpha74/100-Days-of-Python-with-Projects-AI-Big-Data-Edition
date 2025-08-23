import numpy as np

# From Python list
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2d, "\n")

# Using built-in functions
zeros = np.zeros((3, 3))   # 3x3 of zeros
ones = np.ones((2, 4))     # 2x4 of ones
arange = np.arange(0, 10, 2)  # from 0 to 10 step 2
linspace = np.linspace(0, 1, 5)  # 5 evenly spaced numbers between 0 and 1
print("Zeros:\n", zeros, "\n")
print("Ones:\n", ones, "\n")
print("Arange:", arange, "\n")
print("Linspace:", linspace, "\n")

