#extracting list elements
L1=[1,2,3,4,5,6,7]
L2=[1,2,3,4,[5,6,7]]
#L1[a:b] prints elements of list from a to b-1
print(L1[0:4])
print(L1[-1])
print(L1[0:20]) #if the second index is out of range then whole list will get print
print(L1[:])        #this prints the whole list
print(L1[0:-4])
print(L1[0:-10])
#length of list
print(len(L1))
print(len(L2))
#memembership operator in list
print(5 in L1)
print(5 in L2)
print([5,6,7] in L2)
#concating(adding) list
L3=L1+L2
print('L3=',L3)
print('length of L3:',len(L3))
L3+='abc' #remember this shortcut
print(L3)
#replicating list
L4=L1*2
print(L1*2)
print('length of L4:',len(L4))
