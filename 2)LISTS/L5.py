'''program to print elements of list ['q','w','e','r','t','y'] in seperate lines
along with element's both indexes(positive and negative) '''
L=['q','w','e','r','t','y']
length=len(L)
for a in range(length):
    print('at index',a,'and',(a-length),'element',L[a])
