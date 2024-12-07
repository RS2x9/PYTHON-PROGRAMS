#lists-any datatype is supported
a=[1, 2, 3, 4, 5]
b=['a','e','c','d']
c=['a','d',12,13]
print('a is',a)
print('memeory address of a is',id(a))
# changing values in lists
a[0]=10
print('changed list of a is:',a)
print('memory address of changed list',id(a))
print('''the memory of list has remained unchanged
      therefore list is mutable type''')

