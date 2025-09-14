# replace all the odd digits by -1
# method-1 
import numpy as np
import random
arr = np.random.randint(2,20,10)
print("arr: " , arr)
arr[arr%2!=0] =-1
print("\n arr: " , arr)