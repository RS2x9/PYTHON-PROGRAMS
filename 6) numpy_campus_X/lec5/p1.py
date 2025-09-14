# numpy array vs python list
'''
    --> arrays :
        --> are faster
        --> are convinient 
        --> less memory usage for same datatype
'''

import numpy as np
lista = range(100)
arr1 = np.arange(100)

# arrays occupy less memory usage for same datatype
import sys      # to calculate size 
print("list ka :", sys.getsizeof(1)*len(lista),  "bytes")
print("array ka :", arr1.itemsize*arr1.size , "bytes")   

# arrays are faster than list
import time 
x= range(100000)
y=range(100000,200000)
start_time=  time.time()
c=[ (x,y) for x,y in zip(x,y)]   # zip() takes both the corresponding elements and add them
print("list time:",time.time() - start_time)  # this will give duration to store numbers in c 

a= np.arange(100000)
b= np.arange(100000, 200000)
start_time2 =time.time()
d=a+b  
print("array time:", time.time() - start_time2) 