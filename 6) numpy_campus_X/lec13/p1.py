# important functions 
import numpy as np
import random
print("\n", "using functions and results:-")
# random(): always displays values between 0 and 1
print("random: ",np.random.random())


# uniform() : to get random float value between the given range
print("uniform: ", np.random.uniform(4,8) , "\n")

# to get random valus in list within a given range 
print("uniform in range: ",np.random.uniform(2,8,10), "\n")

# reshape()
print("reshape: ", np.random.uniform(2,8,10).reshape(2,5) , "\n")

# randint() : generates random integer
print("randint: " , np.random.randint(2,20))

# generating integer array
print("int array: ", np.random.randint(2,20,5))

#argmax(<array name >) : this returns the indexof the max value in array
arr = np.random.randint(2,20,10)
print("arr: " , arr )
print("arr max value index: " , np.argmax(arr))

#argmin(<array name >) : this returns the indexof the min value in array
print("arr min value index: " , np.argmin(arr))

#seed(<any integer>) : to get the same number always after applied with the same number given inside seed()
print("\nseed(): ",np.random.seed(10))     # seed() will always return None
print(np.random.random())       # seed() will work for this