import numpy as np
import matplotlib.pyplot as plt
num = np.linspace(1 , 5, 8)
y_num1= np.log(num)
print("num: ", num)
print()
print("y_num1: ", y_num1)
plt.plot(num , y_num1 , 'b', linewidth=2 , linestyle='dashed')       # creates the plot with blue colour line
plt.xlabel('num')
plt.ylabel("log(num1)")
plt.show()      # used to see the plot 

y_num2=num*2
plt.plot(num,y_num2,'r',linewidth=5 , linestyle='dashdot')
plt.xlabel('num')
plt.ylabel("num*2")
plt.show()      # used to see the plot 