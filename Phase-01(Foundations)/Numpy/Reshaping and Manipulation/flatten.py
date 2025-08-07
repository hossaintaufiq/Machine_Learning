import numpy as np 

arr= np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
flattened_arr = arr.flatten()  # Flatten the array to 1D
rabelled_arr = arr.reshape(-1)  # Also flattens the array to 1D
print(flattened_arr)  # Output: [1 2 3 4 5 6 7 8 9]  return a copy of the original array.
print(rabelled_arr)  # Output: [1 2 3 4 5 6 7 8 9] return a view of the original array.
# Both methods yield the same result for flattening the array.