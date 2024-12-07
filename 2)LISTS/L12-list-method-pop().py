                                      #LISTS FUNCTIONS AND METHODS
#pop() :REMOVE ITEM FROM LIST AND ALSO RETURNS THE MOVED ITEM FROM THE LIST
#FORMULA:   pop(<index>)
t1=['k','a','e','i','p','q','u']
ele1=t1.pop(3)
print(t1)
print(ele1)
#IF NO INDEX IS PROVIDED THEN pop() WILL REMOVE THE LAST ITEM FROM THE LIST
ele2=t1.pop()
print(t1)
print(ele2)
# IF THE LIST IS ALREADY EMPTY THEN WHILE USING pop() PYTHON RAISES AN ERROR
t2=[]
t2.pop()
print(t2)
