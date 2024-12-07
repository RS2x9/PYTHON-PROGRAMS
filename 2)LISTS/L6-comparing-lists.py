#comparing lists:
'''two sequences of same types.python compares individul
elements of lists (or tuples) in lexographical order '''
L1,L2=[1,2,3],[1,2,3]
L3=[1,[2,3]]
print(L1==L2)
print(L1==L3)
print(L1<L2)
'''print(L1<L3)  this prints error because '<' is not supported
between instances of int and lists '''
'''if the corresponding elements are equal,it goes to the next element untill it
finds the elements the elements that differ.
subsequent elements are not considered even if they are really big'''
L4,L5,L6=[1,2,8,9],[9,1],[1,2,9,1]
print(L4<L5)
print(L4<L6)
print()
a,b,c,d,e=[2,3],[2,3],['2','3'],[2.0,3.0],[2,3,4]
print(a==b)
print(a==c)
print(a>b)
print(d>a) #for comparision purpose python has ignored the type of elment and compared values only
print(d==a)
print(a<e)
#print(a>c)   error:no comparision between int and string
