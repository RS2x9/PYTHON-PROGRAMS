import numpy as np
a = [1,23,4]
num = np.array(a)       #creates numpy array
print(a," and it type : ", type(a))
print(num , " and its type : ", type(num))
print()


#creating numpy array with arange()
num2= np.arange(1,10, 2, np.float32)
print("num2: ", num2)
print()

# creating numpy array with evenly spaced elements : linspace(start , end, number of required elements)
num3 = np.linspace(1 , 10 ,20)
print("num3: ", num3)