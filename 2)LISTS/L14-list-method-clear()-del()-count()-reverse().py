                                         #LISTS FUNCTIONS AND METHODS
#clear() method:REMOVES ALL ITEMS OF THE LIST,
#RETURNS NOTHING
L1=[1,2,3,4,5,67]
L1.clear()
print(L1)

                                        #del<statement>
#DELETE AN ELEMENT BY INDEX
L2=['hi','how','are','you']
del L2[0]
print(L2)
#DELETE A SLICE OF ELEMENTS
del L2[0:2]
print(L2)
#DELETE THE ENTIRE LIST
del L2
#print(L2)   ERROR:NOW NO L2 EXISTS SO L2 IS NOT DEFINED
print()

                                           #count()
#RETURNS HOW MANY TIMES AN ELEMENT IS REPEATED IN THE LIST.
#IF THE ITEM IS NOT IN LIST THEN PYTHON RETURNS 0
L1=[13,18,20,10,18,23]
print(L1.count(18))
print(L1.count(100))
print(L1.count(20))
print()

                                           #reverse()
#DONT CREATE A NEW LIST
#REVERSES THE ITEMS OF THE LIST.TAKES NO ARGUMENT AND RETURNS NO LIST
print('ORIGINAL L1:',L1)
L1.reverse()
print('REVERSE L1:',L1)
