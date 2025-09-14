# plotting graphs using numpy 
import numpy as np
import matplotlib.pyplot as plt
x= np.linspace(-50,50,100)
y1= np.sin(x)
plt.plot(x,y1 , 'g')
plt.show()

y2=x*x +2*x +6
plt.plot(x,y2 , 'r')
plt.show()