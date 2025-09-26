import numpy as np

# Filtering = refers to the process of selecting elements from an array that match a given condition

array = np.array([[1,2,3,4,5],[6,7,8,9,10]])

odd = array[array % 2 == 1] # filter odd numbers
even = array[array % 2 == 0] # filter even numbers

print(odd)
print(even)