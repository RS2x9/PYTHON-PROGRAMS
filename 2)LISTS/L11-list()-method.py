                    #LIST FUNCTIONS AND METHODS
                            #list() method
#creating list from string
print(list('hello'))
#creating list from tuple
print(list((1,2,3,4,5,6,7,8,9)))
#creating empty list
print(list())
#creating list from dictionary
print(list({'a':101,'b':201})) #list will be created from keys of dictionary
print()

                         # index() method
#THIS FUNCTION RETURNS THE INDEX OF THE FIRST MATCHED ITEM FROM THE LIST
a=[12,3,3,4,5,6,7,8,9]
print(a.index(12))
print(a.index(5))
print(a.index(3))
print()
#print(a.index(50))  ERROR:NO 50 IN THE LIST

                        # append()
#ADDS ELEMENTS AT THE THE LAST
a=[12,3,3,4,5,6,7,8,9]
print(a.append('hi'))   #None will get printed as hi is stored in a
print(a)
a.append(list('hello'))
print(a)
a.append(list((12,2,34,56,7,8)))    #the whole will be treated as a single element in list a
print(a)
print(a[9])
print(a[10])
a.append(100)
print(a)
#a.append(200,300)
#print(a)    ERROR:append() takes only one argument
print()

                                     # extend()
#ADDS MULTIPLE ITEMS TO THE LIST
#FORMAT:     List.extend(<list>)
b=['hi','how','are','you']
print('b is:',b)
b.extend(['I','am','fine'])
print(b)
b.extend(['where','are','you','now'])
print(b)
# both append() and extend() do not return any value
c=['at','goa','beach']
b.extend(c)
print(b)
d=b.extend(c)
print(d) #None is printed becaue extend() do not returns any value
print()

                                #DIFFERENCE BETWEEN append() and extend()
t1=[1,3,5]
t2=[7,8]
t1.append([12,14])   #append() adds [12,14] as a single element
print('t1 is:',t1)
t1.extend([12,14])     #extend() adds [12,14] as normal elements
print('t1:',t1)
t3=[20,40]
t2.extend(t3)
print('t2:',t2 , "\n")

                                       # insert()
#INSERTS ITEMS AT THE SPECIFIED POSITION.
#List.insert(<index>,<item>)
#TAKES TWO ARGUMENTS AND RETURNS NO VALUE
t1=['a','e','u']
t1.insert(2,'i')
print(t1)
t1.insert(len(t1),'x')        #this is equivalent to t1.append('x')
print(t1)
#IF WE GIVE NEGATIVE INDEXES WHICH ARE NOT VALID THEN insert() ADDS THE ITEM AT THE BEGINING OF THE LIST
t1.insert(-9,'k')
print(t1)
print()

# IF WE GIVE POSITIVE INDEXES WHICH ARE more than len(list)
#THEN insert() ADDS THE ITEM AT THE LAST OF THE LIST
a=[1,2,3,4]
a.insert(10,10)
print(a)
