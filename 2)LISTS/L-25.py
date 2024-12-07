#PROGRAM TO INPUT TWO LISTS,FIND MAXIMUM VALUE IN EACH AND PRINT MAX.OF THE LIST COMBINED
L1=[]
while True:
    a=input('Enter integer to make 1st list or type next to write next list')
    b=eval(a)
    L1.append(b)
    if a=='next':
        L1.pop()
        break
print('1st List:',L1)
print()
L2=[]
while True:
    c=input('Enter integer to make 2nd List or type next to see results')
    d=eval(c)
    L2.append(d)
    if c=='next':
        L2.pop()
        break
print('2nd List:',L2)
print()
mL1=max(L1)
mL2=max(L2)
if mL1>mL2:
    print('maxvalue in 1st List:',mL1)
elif mL1==mL2:
    print('max.value in both Lists are equal')
else :
    print('max.value in 2nd list:',mL2)
