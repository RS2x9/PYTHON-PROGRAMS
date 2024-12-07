#operator precendence

'''
()                     #paranthesis
**                     #arithmetic operator 
+x,-x; unary+ and -     
* / // %               #arithmetic operator
+ -                    #arithmetic operator 
< <= > >= <> != ==     #relatioanal operator
is ,is not             #identity operator 
not x                  #logical operator 
and                    #logical operator
or                     #logical operator
'''
#** this has right to left associativity
print(2**3**4) #same as 2**(3**4)
print(7*8/5//2)
print((((7*8)/5)//2))
print(7*(8/(5//2)))
print()
print((5<10)and(10<5)or(3<18)and not(8<18))
#print(2/0) this prints error message
#but
print((5<10) or (50<100/0))
'''if the first argument is true then python
do not evaluates the second argument when or operator is present.2nd ARGUMENT IS NOT EVUALATED AT ALL'''
# print((50<100/0) or(5<10))  this results in error
