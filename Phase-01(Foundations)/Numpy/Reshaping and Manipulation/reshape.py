""" 
reshape(rows,cols) specifies the number of rows and columns to reshape the array.
If the total number of elements in the array does not match rows * cols, an error will be raised.
"""

import numpy as np 

arr= np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
reshaped_arr = arr.reshape(1, 9)  # Reshape to 1 row and 9 columns
print(reshaped_arr)  # Output: [[1 2 3 4 5 6 7 8 9]]