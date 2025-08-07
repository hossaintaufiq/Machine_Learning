"""
np.concatenate((array1,array2),axis=None) concatenates two or more arrays along the specified axis.
array1 and array2 are the arrays to be concatenated.
axis =0 concatenates along rows, axis=1 concatenates along columns.
If axis is None, the arrays are flattened before concatenation.
"""

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
new_arr = np.concatenate((arr, [[10, 11, 12]]), axis=0)  # Concatenate a new row
print(new_arr)  # Output: [[ 1  2  3] [ 4  5  6] [ 7  8  9] [10 11 12]]

#joining two arrays along a new axis
arr2 = np.array([[13, 14, 15], [16, 17, 18]])
new_arr2 = np.concatenate((arr, arr2), axis=0)  # Concatenate along rows
print(new_arr2)  # Output: [[ 1  2  3] [ 4  5  6] [ 7  8  9] [10 11 12] [13 14 15] [16 17 18]]