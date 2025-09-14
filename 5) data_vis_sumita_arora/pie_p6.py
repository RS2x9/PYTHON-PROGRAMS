#pie chart
import matplotlib.pyplot as plt
a=[10,25,3,41,56]
names =['a','b','c','d','e']
col=["red", "yellow", "pink","green","blue"]
plt.axis("equal")
plt.pie(a,labels=names , autopct="%.3f%%", colors= col)        #labels: used to label the values 
plt.show()