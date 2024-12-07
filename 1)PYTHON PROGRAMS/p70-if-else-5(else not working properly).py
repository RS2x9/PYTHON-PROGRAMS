''' progarm to find multiples of number
(the divisor) out of given five numbers  '''
a=float(input('enter 1st number:'))
b=float(input('enter 2nd number:'))
c=float(input('enter 3dr number:'))
d=float(input('enter 4th number:'))
e=float(input('enter 5th number:'))
f=float(input('enter divisor number:'))
if a%f==0 :
    print('multiple of',f,'is:',a)
if b%f==0 :
    print('multiple of',f,'is:',b)
if c%f==0 :
    print('multiple of',f,'is:',c)
if d%f==0 :
    print('multiple of',f,'is:',d)
if e%f==0 :
    print('multiple of',f,'is:',e)
else :
    print('no multipe of',f,'is found')
    
    
    

