#bar chart
import numpy as np
import matplotlib.pyplot  as plt 
a = np.array([1,2,3,4,5,6,7,8])
b= np.array([2,4,6,8,10,12,14,16])
c= np.array([1,4,9,16,25,36,49,64])
plt.bar(a,b,color='g')           #width of bar = 0.8 by default
plt.xlabel("a")
plt.ylabel("b")
plt.show()

plt.bar(a,c, width=0.4 , color='r')
plt.xlabel("a")
plt.ylabel("c")
plt.show()