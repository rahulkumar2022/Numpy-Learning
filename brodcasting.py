import numpy as np

# Broadcasting allows Numpy to perform operations on arrays of different shapes.
# The smaller array is "broadcast" across the larger array so that they have compatible shapes.

# The dimensions have the same size or one of the dimensions has a size of 1

array1 = np.array([[1,2,3]])
array2 = np.array([[4],[5],[6]])
print(array1.shape)
print(array2.shape)

print(array1 + array2) # Broadcasting in action
print(array1*array2)