# indexing with boolean arrays 
import numpy as np
arr = np.random.randint(low=1 , high=100 , size=20).reshape(4,5)
print("arr: ", arr)
print("\n ", arr>50)   # outputs array of boolean values 

# i wish to fetch element>50 : we use overlapping
#technique  name : filtering or indexing using boolean array
arr2 = arr[arr>50] ;  ''' arr>50 is overlaped on arr so that 
only elements greater than 50 will show up

'''
print(" arr2:" , arr2)

# fetching elements>50 and odd
arr3 = arr[ (arr>50) & (arr%2!=0)]   # bitwise & is used on boolean values
print("arrr3 : " , arr3)

# fetching elements>50 and odd and making them 0
arr[ (arr>50)&(arr%2!=0)]=0
print("\n arr: " , arr)