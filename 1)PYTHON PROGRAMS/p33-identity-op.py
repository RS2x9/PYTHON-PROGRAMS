#IDENTITIY OPERATORS-CHECKS WHETHER TWO
#BELONGS TO SAME MEMORY ADDRESS OR NOT
a=10
b=10
c=20
print(a is b)
print(a is not b)
print(a is c)
print(a is not c)
print(id(a),id(b),id(c))  #checking memory address of a,b,c 
c=c-10
print(a is c)
print(id(a),id(b),id(c)) #memory of all is same now
print()
#in few cases python two different objects even both
#store the same value.python changes memory addresss
s1='abc'
s2=input('just enter abc')
print(s1==s2)
print(s1 is s2)
s3='abc'
print(s1 is s3)
print(id(s1),id(s2),id(s3))
print()
k=3.5
L=float(input('just enter 3.5'))
print(k==L)
print(k is L)
print(id(k),id(L))
