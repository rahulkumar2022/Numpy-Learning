import numpy as np

array = np.array([[1,2,3,4,5],
                 [6,7,8,9,10],
                 [11,12,13,14,15]])

# array[start:stop:step]
# arry[start:stop]
# array[start:]


print(array[1:3]) # from row 1 to row 2
print(array[0:2]) # from row 0 to row 1
print(array[0:3]) # from row 0 to row 2
print(array[0:]) # from row 0 to the end
print(array[1:]) # from row 1 to the end
print(array[:2]) # from the beginning to row 1
print(array[:3]) # from the beginning to row 2
print(array[:]) # from the beginning to the end
print(array[::2]) # every second row
print(array[::1]) # every row
print(array[1::2]) # every second row from row 1 to the end
print(array[0::2]) # every second row from row 0 to the end

print(array[0:3:2])

print(array[::-1]) # reverse the array
print(array[:,::-1]) # reverse each row
print(array[::-1,::-1]) # reverse the array and each row