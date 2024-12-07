'''program that reads two numbers and an
arithmetic operator and displays the computed result'''

a=float(input('enter number'))
b=float(input('enter number'))
op=input("chosse operator:'+','-','*','/','//','%','**'")
if op=='+' :
    print('sum is:',a+b)
elif op=='-' :
    print('minus is:',a-b)
elif op=='*' :
    print('multiplication is:',a*b)
elif op=='/' :
    print('after dividing:',a/b)
elif op=='//' :
    print('after floor division:',a//b)
elif op=='%' :
    print('remainder is:',a%b)
elif op=='**' :
    print('exponent:',a**b)
else:
    print('valid operator')
