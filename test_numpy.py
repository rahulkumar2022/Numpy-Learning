import numpy as np

# Create a simple array
arr = np.array([1, 2, 3, 4, 5])
print("Created array:", arr)

# Show array properties
print("\nArray properties:")
print("Shape:", arr.shape)
print("Data type:", arr.dtype)
print("Dimensions:", arr.ndim)

# Perform some basic operations
print("\nBasic operations:")
print("Mean value:", np.mean(arr))
print("Sum of elements:", np.sum(arr))
print("Array squared:", np.square(arr))

# Create a 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D array:")
print(matrix)