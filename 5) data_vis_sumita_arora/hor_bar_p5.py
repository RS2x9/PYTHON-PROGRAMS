# plotting horizontal bar chart
import numpy as np 
import matplotlib.pyplot as plt
x_axis= np.arange(5)
y_axis = np.array([0,1,4,9,16])
plt.barh(x_axis , y_axis, color='yellow')
plt.show()