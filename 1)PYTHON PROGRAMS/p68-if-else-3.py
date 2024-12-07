''' Q) input three numbers
sum1=sum of all the numbers
sum2=sum of non duplicate numbers  '''
a=float(input('enter 1st number'))
b=float(input('enter 2nd number'))
c=float(input('enter 3rd number'))
sum1=a+b+c
print('sum of all numbers is:',sum1)
if a!=b and a!=c and b!=c :
    print('sum of non duplicate numbers are:',a+b+c)
if a==b and b==c :
    print('sum of non duplicate numbers are:',0)
if a==b and b!=c :
    print('sum of non duplicate numbers are:',b+c)
if a==c and c!=b:
    print('sum of non duplicate numbers are:',c+b)
if b==c and c!=a:
    print('sum of non duplicate numbers are:',a+c)
