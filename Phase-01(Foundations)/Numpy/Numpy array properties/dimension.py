import numpy as np 

# creating arrays from python lists
arr_1d= np.array([10,20,30,40,50,60,70,80,90,100])
arr_2d = np.array([[1, 2, 3], 
                   [4, 5, 6],
                   [7, 8, 9]])

arr_3d= np.array([[[1, 2], [3, 4]], 
                   [[5, 6], [7, 8]]])
arr_1d_dimension = arr_1d.ndim
arr_2d_dimension = arr_2d.ndim
arr_3d_dimension= arr_3d.ndim
print("The dimension of the one dimensional array is : ", arr_1d_dimension)
print("The dimension of the two dimensional array is: ", arr_2d_dimension)
print("The dimension of the three dimensional array is: ", arr_3d_dimension)
