import numpy as np 

# creating arrays from python lists

arr_2d= np.array([[1, 2, 3], [4, 5, 6]])
float_arr2= np.array([[8.5, 2.0, 3.9], [4.0, 5.8, 6.0]])

# float_arr = arr_2d.astype(float)
# print(float_arr)
print("Before conversion array type: ")
print(float_arr2.dtype)

int_arr= float_arr2.astype(int)
print(int_arr)
print("After conversion array type: ")
print(int_arr.dtype)
