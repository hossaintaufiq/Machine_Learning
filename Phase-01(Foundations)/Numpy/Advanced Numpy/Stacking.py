"""
vertically,
horizontally, or depth-wise.
This is useful for combining multiple arrays into a single array.

vstack(arrays, axis=0) stacks arrays vertically (along rows).
hstack(arrays, axis=1) stacks arrays horizontally (along columns).
dstack(arrays, axis=2) stacks arrays depth-wise (along the third axis).Stacking is useful for combining arrays of the same shape along a new axis.
"""

import numpy as np

# Example of vertical stacking
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
vstacked_arr = np.vstack((arr1, arr2))  # Stack arrays vertically   
print("Vertical Stacking:\n", vstacked_arr)  # Output: [[ 1  2  3] [ 4  5  6] [ 7  8  9] [10 11 12]]

# Example of horizontal stacking
hstacked_arr = np.hstack((arr1, arr2))  # Stack arrays horizontally
print("Horizontal Stacking:\n", hstacked_arr)  # Output: [[ 1  2  3  7  8  9] [ 4  5  6 10 11 12]]          
# Example of depth-wise stacking
dstacked_arr = np.dstack((arr1, arr2))  # Stack arrays depth-wise           
print("Depth-wise Stacking:\n", dstacked_arr)  # Output: [[[ 1  7] [ 2  8] [ 3  9]] [[ 4 10] [ 5 11] [ 6 12]]]
# Example of stacking arrays with different shapes
arr3 = np.array([[13, 14], [15, 16]])
vstacked_arr_diff = np.vstack((arr1, arr3))  # Stack arrays with different shapes
print("Vertical Stacking with Different Shapes:\n", vstacked_arr_diff)  # Output: [[ 1  2  3] [ 4  5  6] [13 14] [15 16]]   
# Example of stacking arrays with different shapes horizontally
hstacked_arr_diff = np.hstack((arr1, arr3))  # Stack arrays with different shapes
print("Horizontal Stacking with Different Shapes:\n", hstacked_arr_diff)  #
# Output: [[ 1  2  3 13 14] [ 4  5  6 15 16]]
# Example of depth-wise stacking with different shapes
dstacked_arr_diff = np.dstack((arr1, arr3))  # Stack arrays with different shapes
print("Depth-wise Stacking with Different Shapes:\n", dstacked_arr_diff)  # Output: [[[ 1 13] [ 2 14] [ 3 15]] [[ 4 16] [ 5 16] [ 6 16]]]   
