'''
    Broadcasting:-
    --> it's ability of Numpy to treat arrays of different shapes during
        arithmetic operations.
    --> Arithmetic opearions on arrays are usuallyy done on corresponding 
        elements.
    --> if two arrays are of exactly of same shape, then these operations 
        are smoothly performed.
    --> if the dimensions are disimilar, element to element operations
        are not possible.
    --> the smaller array is broadcast to the size of the larger array 
    so that they have compatible shapes.
''' 

import numpy as np
arr1 = np.arange(12).reshape(3,4)
arr2 = np.array([0,1,2,4])
print("arr1: ", arr1)
print("arr2: ", arr2 , "\n\n", "sum: ")
print(arr1+arr2)