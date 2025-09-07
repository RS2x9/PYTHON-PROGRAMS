#SLICING A LIST
lst=[10,12,14,20,22,24,30,32,34]
print(lst)
seq1=lst[3:-3]
print(seq1)
seq1[1]=28
print(seq1)

seq2=lst[-15:7]
print(seq2)
print()

L1=[2,3,4,5,6,7,8]
print(L1[2:5])
print(L1[6:])
print(L1[-10:20])
print(L1[10:20])
print()

lst=[10,12,14,20,22,24,30,32,34]
print(lst)
print(lst[0:10:2])
print(lst[0:10:3])
print(lst[::3])
print()

List=[5,6,8,11,3]
print(List[::-1]) #LIST GETS REVERSED
L=['one','two','three']
L[0:2]=[0,1]
print(L)
print()

L1=['one','two','three']
L1[0:2]='a' #this removes elements of index 0,1 & a gest inserted there
print(L1)
print()

L2=[1,2,3]
L2[2:]='604'
print(L2)
#L2[2:]=100  this cant happnen.values assigned should be list ,string,tuple
L2[2:]=[604,204]
print(L2)
L2[1:]=[33]
print(L2)
L2[10:20]='abcd' #no error even if slice limits are outside the length
print(L2)
