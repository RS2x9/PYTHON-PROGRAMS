#PROGRAM TO TAKE INPUT AND SEARCH FOR AN ELEMENT IN A GIVEN LIST OF ELEMENTS
L=[]
while True:
    a=input('Enters integers or type exit to stop:')
    b=eval(a)
    L.append(b)
    if a=='exit':
        L.pop()
        break
print('Created List:',L)
while True:
    w=input('Enter element to be searchd or type exit to stop:')
    if w=='exit':
        break
    s=int(w)
    print('Element',s,'is at index',L.index(s))
