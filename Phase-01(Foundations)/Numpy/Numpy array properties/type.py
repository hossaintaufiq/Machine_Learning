import numpy as np 

# creating arrays from python lists
arr = np.array([1, 2, 3, 4, 5])
string_array = np.array(['apple', 'banana', 'cherry'])
bool_array = np.array([True, False, True])
float_array = np.array([1.5, 2.5, 3.5])
print("type of the array is: ", arr.dtype)
print("type of the string array is: ", string_array.dtype)
print("type of the boolean array is: ", bool_array.dtype)
print("type of the float array is: ", float_array.dtype)