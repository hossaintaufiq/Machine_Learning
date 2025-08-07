"""
3 functions to split an array into multiple sub-arrays:
1. np.split(array, indices_or_sections, axis=0) splits an array into multiple sub-arrays along the specified axis.
2. np.hsplit(array, indices_or_sections) splits an array into multiple sub-arrays along the horizontal axis (axis=1).
3. np.vsplit(array, indices_or_sections) splits an array into multiple sub-arrays along the vertical axis (axis=0).
"""

import numpy as np

arr= np.array([1, 2, 3, 4, 5, 6, 7, 8])
# new_arr= np.split(arr, 3)  # Split into 3 equal parts
# print(new_arr)  # Output: [array([1, 2, 3]), array([4, 5, 6]), array([7, 8, 9])]

new_arr2 = np.split(arr,2)  
print(new_arr2)  # Output: [array([1, 2, 3, 4]), array([5, 6, 7, 8])]


# Example of horizontal split
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
hsplit_arr = np.hsplit(arr2, 3)  # Split into 3 equal parts along the horizontal axis
print("Horizontal Split:\n", hsplit_arr)  # Output: [array([[1      2, 3]]), array([[4, 5, 6]]), array([[7, 8, 9]])]    

# Example of vertical split
vsplit_arr = np.vsplit(arr2, 3)  # Split into 3 equal parts along the vertical axis
print("Vertical Split:\n", vsplit_arr)  # Output: [array([[1, 2, 3]]), array([[4, 5, 6]]), array([[7, 8, 9]])]
