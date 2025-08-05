import numpy as np 

# creating arrays from python lists
arr= np.array([1, 2, 3, 4, 5])
print(arr)

arr_2d = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])

shape_2d= arr_2d.shape 
print("The shape of the two dimensional array is: ", shape_2d)
print("The two dimensional array is: \n", arr_2d)
