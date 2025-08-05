# creating arrays from python lists 
# np.array([elements]) creates an array from a list of elements

import numpy as np 

arr = np.array([1, 2, 3, 4, 5])
print(arr); 


# default values 
zeros_array= np.zeros(3) # creates an array of zeros with length 3
print("\nArray of zeros: ", zeros_array)

zeros_array_2d = np.zeros((5,4)) # creates a 2D array of zeros with shape 5x4
print("\n2D Array of zeros: \n", zeros_array_2d )

# ones array = np.ones(3) # creates an array of ones with length 3
ones_array = np.ones(3)
ones_array_2d= np.ones((5,4)) # creates a 2D array of ones with shape 5x4
print("\nArray of ones: ", ones_array)
print("\n2D Array of ones: \n", ones_array_2d )


# full array =np.full((3,4), 7) # creates a 2D array of shape 3x4 filled with the value 7
filled_array= np.full((5,3),6) # creates a 2D array of shape 5x3 filled with the value 6
print("\nFilled Array: \n", filled_array)

# creating sequence arrays 
# arange(start, stop, step) creates an array with a sequence of numbers
sequence_array = np.arange(0, 10, 3) # creates an array with numbers from 0 to 10 with a step of 2
print("\nSequence Array: ", sequence_array)

# identity matrix 
identity_matrix= np.eye(4) # creates a 3x3 identity matrix
print("\nIdentity Matrix: \n", identity_matrix)