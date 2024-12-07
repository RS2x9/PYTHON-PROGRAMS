# read N numbers and create a list. find mean ,variance,standard deviation
import numpy as np
List=[]
n=int(input('Enter number of elments'))
for i in range(n):
    num=int(input('Enter data'))
    List.append(num)
print('mean:',np.mean(List))
print('variance:',np.var(List))
print('standard dev:',np.std(List))
