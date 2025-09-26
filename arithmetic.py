import numpy as np

# Scalar arithmetic operations

array = np.array([1,2,3])

print(array + 5)  # Addition
print(array - 2)  # Subtraction
print(array * 3)  # Multiplication
print(array / 2)  # Division
print(array ** 3) # Exponentiation
print(array % 2)  # Modulus
print(array // 2) # Floor Division

# Vectorised arithmetic operations

array = np.array([1.02,2.8,3.9])
print(np.sqrt(array))
print(np.round(array))
print(np.floor(array))
print(np.ceil(array))
print(np.pi)

radii = np.array([1,2,3,4,5])

areas = np.pi * np.power(radii, 2)
print(areas)
print(np.pi * radii ** 2)

#Element wise operations

array1 =np.array([1,2,3])
array2 =np.array([4,5,6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)
print(array1 % array2)
print(array1 // array2)

# Comparison operations
scores = np.array([65, 70, 85, 90, 95])
print(scores > 75)
print(scores < 75)
print(scores >= 85)
print(scores <= 85)
print(scores == 90)
print(scores != 90)

