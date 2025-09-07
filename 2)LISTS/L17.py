#write  a program that asks the user to input a number or a list of numbers to be appended to the existing list
L=[10,20,30]
n=eval(input('enter number or a list of numbers'))
if type(n)==type(1):
    L.extend(n)
    print(L)
elif type(n)==type([]):
    L.extend(n)
    print(L)
else :
    print('enter only number or list of numbers')
    
