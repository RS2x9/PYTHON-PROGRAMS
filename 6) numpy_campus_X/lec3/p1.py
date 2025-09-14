# creating nd arrays 
import numpy as np

# numpy.array()
arr1= np.array([1,23,45])           #1-d array
print("arr1: ", arr1 ,"\n")

#2-d array
arr2= np.array([[1,2,3] , [4,5,6] ])
print("arr2: ", arr2 , "\n")

# numpy.zeros((<number of rows> , <number of columns>))
arr3 = np.zeros((2,3))
print("arr3: ", arr3 , "\n")

# numpy.ones((<number of rows> , <number of coloumns> ))
arr4= np.ones((3,3))
print("arr4: ", arr4 , "\n")

# numpy.identity(<any number>)
arr5= np.identity(5)     # all the diagonal elements will be 1, others 0
print("arr5: ", arr5 , "\n")

# numpy.arange()
arr6= np.arange(10)
print("arr6: ", arr6 , "\n")

arr7 = np.arange(5,20)
print("arr7: ", arr7 , "\n")

arr8 = np.arange(5,20,3)
print("arr8: ", arr8 , "\n")

# numpy.linspace(<a> , <b> ,<c>): creates c  equally spaced items from a to b
arr9 = np.linspace(2,20,15)
print("arr9: ", arr9 , "\n")

# <array2> = <array1>.copy()
arr10 = arr9.copy()
print("arr10: ", arr10 , "\n")