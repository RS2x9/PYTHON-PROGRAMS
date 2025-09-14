# fancing indexing in numpy
import numpy as np
arr = np.arange(24).reshape(6,4)
print("arr: " , arr)

# print 1,3,5 row
print("particular  rows: " ,arr[[0,2,4]])