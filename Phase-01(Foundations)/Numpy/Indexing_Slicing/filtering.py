import numpy as np

arr= np.array([1, 2, 3, 4, 5])

# x=[True,False,True,False,True]

# new_arr = arr[x]  # boolean indexing
# print(new_arr)  # prints elements where x is True
print(arr[arr>2])  # filtering elements greater than 2






# Filtering elements based on a condition using boolean indexing
# import numpy as np

# arr = np.array([41, 42, 43, 44])

# # Create an empty list
# filter_arr = []

# # go through each element in arr
# for element in arr:
#   # if the element is higher than 42, set the value to True, otherwise False:
#   if element > 42:
#     filter_arr.append(True)
#   else:
#     filter_arr.append(False)

# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)