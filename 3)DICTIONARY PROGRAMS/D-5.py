#to acess all the keys :<dictionary>.keys()
#TO WRITE ALL THE VALUE: <dictionary>.values()
d={1:12,2:23,4:78}
print(d.keys())    #output is:  dict_keys([1,2,4])
print(d.values())  #output is:  dict_values([12,23,78])
print()
#we can convert the sequence returned by keys()  and values()
print(list(d.keys()))
print(list(d.values()))
