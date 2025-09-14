# some motre functions 
import numpy as np
import random
# percentile(<array> , <percentile>) : calculates the q-th percentile of a dataset. 
# That means it finds the value below which a given percentage of data falls.
a = np.random.randint(1,50,12)
print("a: " , a)
a= np.sort(a)
print("a: ", a)
print(np.percentile(a,25))