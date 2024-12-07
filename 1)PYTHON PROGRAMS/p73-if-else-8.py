#read three integers and print them in ascending order

x=int(input('Enter any number'))
y=int(input('Enter any number'))
z=int(input('Enter any number'))
if x>y and x>z :
    if y>z :
        print('ascending order:',x,'>',y,'>',z)
    else :
        print('ascending order:',x,'>',z,'>',y)
elif x<y and x<z :
    if y>z :
        print('ascending order:',y,'>',z,'>',x)
    else :
        print('ascending order:',z,'>',y,'>',x)
elif y<x and y<z :
    if x<z :
        print('ascending order:',z,'>',x,'>',y)
elif z<x and z<y :
    if x<y:
        print('ascending order:',y,'>',x,'>',z)
