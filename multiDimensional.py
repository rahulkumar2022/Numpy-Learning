import numpy as np


array = np.array('A')

print(array)
print("Array shape:", array.shape)
print(type(array))
print(array.ndim) # Number of dimensions => 0
# array = array * 2 error
# print(array)

array = np.array(['A'])

print(array.ndim) # Number of dimensions => 1

array = np.array([['A', 'B', 'C'],['D', 'E', 'F']]);
print(array)
print("Array shape:", array.shape)
print(type(array))
print(array.ndim) # Number of dimensions => 2


array = np.array([[['A', 'B', 'C'],['D', 'E', 'F']],[['G', 'H', 'I'],['J', 'K', 'L']]]);
print(array)
print("Array shape:", array.shape)
print(type(array))
print(array.ndim) # Number of dimensions => 3

print(array[0][0][0]) # A
print(array[1][1][2]) # L
print(array[0,0,0]) # A
print(array[1,1,2]) # L

word = array[0,0,0] + array[1,1,2] + array[1,1,2]
print(word) # ALL