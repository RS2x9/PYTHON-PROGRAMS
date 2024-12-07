#program to take input from user and find minimum value of element in list along with its index
L=[]
while True:
    b=input('typeintegers to create list or type exit to stop')
    a=eval(b)
    L.append(a)
    if b=='exit':
        L.pop()
        break
print('created list:',L)
print('minimum is',min(L),end='')
print('at index',L.index(min(L)))
