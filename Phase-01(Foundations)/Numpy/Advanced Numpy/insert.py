"""
np.insert(arr, index, values, axis=None) inserts values along the specified axis before the given index.
array-original is the array to be modified.
index is the position before which values are inserted.
values are the new values to be inserted.
axis is the axis along which to insert the values (default is None, meaning the array is flattened).
If axis is specified, the shape of values must match the shape of the array along that axis.
If axis is None, values must be 1D and will be flattened before insertion.

axis=0 inserts a new row, axis=1 inserts a new column.
"""

import numpy as np


print("2d array insert")
arr= np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

arr_inserted = np.insert(arr, 1, [10, 11, 12], axis=0)  # Insert a new row at index 1
print(arr_inserted)


print("1d array insert")
arr_1d= np.array([1, 2, 3, 4, 5])
arr_inserted_1d = np.insert(arr_1d, 2, 100, axis=0)  # Insert values at index 2
print(arr_1d)  # Original array remains unchanged
print(arr_inserted_1d)