# reshaping numpy arrays 

#ravel() : makes the all the types of dimensioanl arrays to 1-D
import numpy as np
arr1 = np.arange(6).reshape(3,2)
print("arr1: ", arr1)
print("arr1 dimen: ", arr1.ndim)
arr2 = arr1.ravel()
print("arr2:", arr2)

# reshape()
arr3 = np.arange(6).reshape(2,3)
print("arr3: ", arr3)

#transpose() 
print("arr3 transpose  : ", arr3.transpose())

# hstack() : hprizontally combining two array of same shape 
arr4 = np.arange(6,12).reshape(2,3)
print("arr4 : ", arr4)
print("hstack arrr3 and arr4" , np.hstack((arr3 , arr4)))

# vstack(): vertically combines two array of same shape 
print("vstack arr3 and arr4: ", np.vstack((arr3 , arr4)))

# hslpit(<array name> , <number of parts to be splitted>): splits the array horizontally
print("\n arr3: ", arr3)
print("arr3 horizontal split: " , np.hsplit(arr3, 3)) 

# vsplit(<array name> , <number of parts to be splitted>): splits the array vertically
print("\n arr3 vertical split: " , np.vsplit(arr3, 2))