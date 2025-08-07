"""
append(arr, values, axis=None) appends values to the end of the array along the specified axis.
array-original is the array to which values are appended.
"""

import numpy as np
arr= np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
new_arr= np.append(arr, [[10, 11, 12]], axis=0)  # Append a new row
print(new_arr)  # Output: [[ 1  2  3] [ 4  5  6] [ 7  8  9] [10 11 12]]