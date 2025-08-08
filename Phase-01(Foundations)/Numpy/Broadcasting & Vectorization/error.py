import numpy as np

arr1=np.array([1, 2, 3, 4, 5, 6, 7, 8])
arr2=np.array([[10, 20, 30],[2,3,5]])


result = arr1 + arr2

print(result)  # give error cz imcompatible shapes
# Output: ValueError: operands could not be broadcast together with shapes (8,) (2,3)
