#program to calculate and print the roots of quadratic equation
import math
print('the quadratic equation is:ax**2+b*x+c=0')
a=int(input('enter a'))
b=int(input('enter b'))
c=int(input('enter c'))
deter=math.sqrt(math.pow(b,2)-4*a*c)
root1=(-b+deter)/2*a
root2=(-b-deter)/2*a
if a!=0 and deter>=0  :
    print('roots are','root1',root1,'\n','root2',root2)
if a==0:
    print('a=0 is not possible')
if deter<0 :
    print('imaginary roots')

    

