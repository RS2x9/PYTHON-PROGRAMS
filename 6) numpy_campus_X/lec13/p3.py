# method-2 
# where( <condition> , <statemnet when True> , <statement when false>)
import numpy as np
import random 
arr = np.random.randint(1,50,10)
print("arr: " , arr , "\n")
arr2 = np.where(arr%2==1 , -1 , arr)
print("arr2: " , arr2)
