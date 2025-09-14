#numpy operations 
import numpy as np
arr1 = np.arange(6)
arr2= np.arange(6,12)
print(arr1+arr2)
print(arr1*arr2)
print(arr1*2)
print(arr1>3)

# dot product
arr3= np.arange(6).reshape(2,3)
arr4= np.arange(6,12).reshape(3,2)
print("\narr3: ", arr3)
print("arr4: ", arr4)
print("\n dot prod:",arr3.dot(arr4))
print("\n arr4 min: ", arr4.min())
print("arr4 max: ", arr4.max())

arr5 = np.array( [ [10,1],[4,2] ] )
print("\n arr5: ", arr5)
print("arr5 min in each row : ", arr5.min(axis=0))   #gives min. values in each column in the form of array
print("arr5 max in each row: ", arr5.max(axis=1))       # gives max. values in each row in the form of array
print("arr5 sum: ", arr5.sum())
print("arr5 column sum:  ",arr5.sum(axis=0) )   # gives column sum
print("arr5 row sum : " , arr5.sum(axis=1))
print("arr5 mean: ", arr5.mean())
print("arr5 column mean: ", arr5.mean(axis=0))
print("arr5 row mean: ", arr5.mean(axis=1))
print("arr5 standard deviation: ", arr5.std())
print("arr5 median: ", np.median(arr4))

print("\n arr1: ", arr1)
print("arr1 sin values: ", np.sin(arr1))
print("arr1 exponential val: ", np.exp(arr1))