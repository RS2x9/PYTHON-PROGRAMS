#TRUE COPY OF LIST
a=[1,2,3]
b=a #it dont make b as a duplicate list,python make label b to point where label a is pointing ie no true copy
print('a:',a)
print('b',b)
print('memory address of a:',id(a))
print('memory address of b:',id(b))
#making any changes in any one list,other list also get changed because a and b are alias of same list 
a[0]=10
print('b:',b)
print('b id:',id(b),'a id:',id(a))
print(a==b==[10,2,3])
print()
#TRUE COPY OF LIST:TO MAKE CHANGES in b Only AND  a REMAIN UNCHANGED: make copy of list a
A=[10,20,30,40]
B=list(A)
print('A id:',id(A),'B id:',id(B))
A[0]=100
B[0]=200
print('A is:',A)
print('B is:',B)
print()
#OTHER METHOD TO MAKE TRUE COPY OF LIST
L=[100,200,300,400]
print('L is:',L)
L_copy=L.copy()
print('L id is:',id(L),',','L_copy id is :',id(L_copy))
L[1]=['hi']
L_copy[1]=['bye']
print('L is:',L,',','L_copy is:',L_copy)
