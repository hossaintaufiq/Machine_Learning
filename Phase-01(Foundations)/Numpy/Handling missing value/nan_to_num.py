import numpy as np

arr= np.array([1, 2, np.nan, 4, 5, np.nan])

result=np.nan_to_num(arr,nan=0) #default value for nan is 0

print(result)  # Output: [1. 2. 0. 4. 5. 0.]