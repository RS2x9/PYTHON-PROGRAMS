# indexing  , slicing , iteration
import numpy as np
arr1=np.arange(24)
# using reshape()
arr2= np.arange(24).reshape(6,4)   #6x4=24
print("arr1: ", arr1)
print("arr2: ", arr2 , "\n")  
print(arr2[1:3] , "\n")

for i in arr2:
    print(i)
print()

for i in np.nditer(arr2):
    print(i , " " , end=" ")