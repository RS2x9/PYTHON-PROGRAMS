                   #DELETING ELEMENTS IN DICTIONARY

#  del <dictonary>[key]   :to delete only values
#key must exist in dictionary
D={1:12,2:34,3:45,4:56}
del D[3]
print(D)

# del <dictionary name>  :deletes whole dictionary
a={'hi':'Rohan'}
del a
# print(a)  #this will give keyerror

                                # checking for existance of key
# use in ,not in operator : used only to check existance of keys
b={'hi':'rohan'}
print('hi' in b)
print('rohan' in b)   #as 'rohan' is value so False will be returned

                           # checking for existance of value
# <dictionary name>.values()
b={'hi':'rohan'}
print('rohan' in b.values())
