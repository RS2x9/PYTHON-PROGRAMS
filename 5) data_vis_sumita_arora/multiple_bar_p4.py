import numpy as np
import matplotlib.pyplot as plt 
a=[1,2,3,4]
b=[1,4,9,16]
n=np.arange(len(a))

plt.bar(n,a,color='red',width=0.3)

plt.bar(n+0.3,b,color='g',width=0.3)
plt.show()