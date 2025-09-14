# properties and attributes
# attributes don't have ()
import numpy as np
arr1 = np.array( [ [ [1,2] , [3,4] , [5,6] ] , [ [7,8], [9,10] , [11,12]] ] )

# 1> shape 
print("arr1: ", arr1 , "\n", "arr1 shape: " , arr1.shape )

# 2> ndim : gives the dimensions 
print(" arr1 dimensions : " , arr1.ndim)

#3> size : returns the total number of elements in tensor 
print(" arr1 size : ", arr1.size)

#4> itemsize : returns the datatype size in bytes  
print(" arr1 itemsize: ", arr1.itemsize)

#5> dtype : returns datatype 
print("arr1 datatype: ", arr1.dtype)

#6> astype('<datatype>') : the array gets converted to specified datatype
arr1 = arr1.astype('float')
print("\n","arr1" , arr1 , "\n")
print("arr1 datatype: ", arr1.dtype)