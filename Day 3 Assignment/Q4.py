import numpy as np

arr = np.array(range(1,10))
print(arr.shape)

arr1 =  arr[np.newaxis, :] #making it row vector
print(arr1.shape)

arr2 = arr[:, np.newaxis] #making it column vector
print(arr2.shape)
