import numpy as np

# Aggregate functions = summarize data and typically return a single value 


array = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(np.sum(array)) # sum of all values in array
print(np.mean(array)) # mean of all values in array
print(np.median(array)) # median of all values in array
print(np.std(array)) # standard deviation of all values in array
print(np.var(array)) # variance of all values in array
print(np.min(array)) # minimum value in array
print(np.max(array)) # maximum value in array
print(np.percentile(array, 50)) # 50th percentile (median) of all values in array
print(np.percentile(array, 25)) # 25th percentile of all values in array
print(np.percentile(array, 75)) # 75th percentile of all values in array
print(np.ptp(array)) # peak to peak (max - min) of all values in array
print(np.any(array > 5)) # check if any value in array is greater than 5
print(np.all(array > 0)) # check if all values in array are greater than 0