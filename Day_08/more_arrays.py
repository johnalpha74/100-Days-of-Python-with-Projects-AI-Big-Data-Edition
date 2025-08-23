import numpy as np

# Random arrays
random_array = np.random.rand(2, 3)  # 2x3 array of random floats
print("Random Array:\n", random_array)

# Identity matrix
identity_matrix = np.eye(3)  # 3x3 identity matrix
print("Identity Matrix:\n", identity_matrix)

# Full array
full_array = np.full((2, 2), 7)  # 2x2 array filled with 7
print("Full Array:\n", full_array)

# Diagonal array
diagonal_array = np.diag([1, 2, 3])  # Diagonal matrix with specified diagonal
print("Diagonal Array:\n", diagonal_array)

# Random integers
random_integers = np.random.randint(0, 10, (2, 3))  # 2x3 array of random integers between 0 and 10
print("Random Integers:\n", random_integers)

# Reshape an existing array
reshaped_array = np.arange(12).reshape((3, 4))  # Reshape to 3x4
print("Reshaped Array:\n", reshaped_array)

# Creating arrays with specific data types
arr_int = np.array([1, 2, 3], dtype=np.int32)  # Array of integers
print("Integer Array:", arr_int)
arr_float = np.array([1.0, 2.0, 3.0], dtype=np.float64)  # Array of floats
print("Float Array:", arr_float)

# Creating arrays with complex numbers
arr_complex = np.array([1+2j, 3+4j], dtype=np.complex128)  # Array of complex numbers
print("Complex Array:", arr_complex)

# Creating structured arrays
dtype = np.dtype([('name', 'U10'), ('age', 'i4')])  # Structured data type
structured_array = np.array([('Alice', 30), ('Bob', 25)], dtype=dtype)  # Structured array
print("Structured Array:\n", structured_array)

# Creating masked arrays
masked_array = np.ma.array([1, 2, 3, 4], mask=[0, 1, 0, 1])  # Masked array
print("Masked Array:\n", masked_array)

# Creating arrays with specific shapes
empty_array = np.empty((2, 3))  # Uninitialized array of shape 2x3
print("Empty Array:\n", empty_array)

# Creating arrays with custom shapes
custom_shape_array = np.empty((4, 5), dtype=np.float32)  # Custom shape with float32 type
print("Custom Shape Array:\n", custom_shape_array)

# Creating arrays with specific fill values
fill_value_array = np.full((3, 3), 42)  # 3x3 array filled with 42
print("Fill Value Array:\n", fill_value_array)

# Creating arrays with specific data types
# arr_bool = np.array([True, False, True], dtype=np.bool_)  # Boolean array
# print("Boolean Array:", arr_bool)

# Creating arrays with specific shapes and data types
arr_str = np.array(['a', 'b', 'c'], dtype=np.str_)  # String array
print("String Array:", arr_str)

# Creating arrays with specific shapes and data types
arr_object = np.array([{'key': 'value'}, {'key2': 'value2'}], dtype=object)  # Object array
print("Object Array:", arr_object)

# Creating arrays with specific shapes and data types
arr_datetime = np.array(['2023-01-01', '2023-01-02'], dtype='datetime64[D]')  # Date array
print("Date Array:", arr_datetime)

# Creating arrays with specific shapes and data types
arr_timedelta = np.array(['1 day', '2 days'], dtype='timedelta64[D]')  # Time delta array
print("Time Delta Array:", arr_timedelta)

# Creating arrays with specific shapes and data types
arr_bytes = np.array([b'hello', b'world'], dtype=np.bytes_)  # Byte array
print("Byte Array:", arr_bytes)

# Creating arrays with specific shapes and data types
arr_unicode = np.array(['hello', 'world'], dtype=np.unicode_)  # Unicode array
print("Unicode Array:", arr_unicode)

# Creating arrays with specific shapes and data types
arr_void = np.array([(1, 2), (3, 4)], dtype=np.void)  # Void array
print("Void Array:\n", arr_void)


