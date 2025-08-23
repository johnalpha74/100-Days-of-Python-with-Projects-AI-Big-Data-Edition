# NumPy – create and manipulate array

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Numpy Array:", arr)
print("Numpy Array Type:", type(arr))

# Perform basic operations
print("Numpy sum:", np.sum(arr))
print("Numpy max:", np.max(arr))
print("Numpy min:", np.min(arr))
print("Numpy median:", np.median(arr))
print("Numpy std deviation:", np.std(arr))
print("Numpy variance:", np.var(arr))
print("Numpy square root:", np.sqrt(arr))
print("Numpy log:", np.log(arr))
print("Numpy exponential:", np.exp(arr))
print("Numpy mean: ", np.mean(arr))
print("Numpy squared:", np.array([x**2 for x in arr]))
# Perform advanced operations
print("Numpy cumulative sum:", np.cumsum(arr))
print("Numpy cumulative product:", np.cumprod(arr))
print("Numpy dot product:", np.dot(arr, arr))
print("Numpy cross product:", np.cross(arr, arr))
print("Numpy unique elements:", np.unique(arr))
