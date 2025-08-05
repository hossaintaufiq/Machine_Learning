import numpy as np
"""
array[index] #1d array indexing 
array [row,column ] #2d array indexing
"""

arr= np.array([1, 2, 3, 4, 5])
print(arr[1])
print(arr[-1]) # accessing last element

print(arr[0:5])
print(arr[:3])
print(arr[::2])  # slicing with step
print(arr[::-1])  # reversing the array
