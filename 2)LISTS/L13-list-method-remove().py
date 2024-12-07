                                     #LIST FUNCTIONS AND METHODS
#remove(<VALUE>) :USED TO REMOVE THE VALUE IF WE DONT KNOW THE INDEX.
#IF THERE IS NO SUCH ITEM THEN PYTHON RAISES ERROR
#RETURNS NO VALUE
t1=['a','e','i','p','q','a','q','p']
ele1=t1.remove('a')
print(t1)
print(ele1) #OUTPUT=None: because remove() returns nothing
t1.remove('e')
print(t1)
