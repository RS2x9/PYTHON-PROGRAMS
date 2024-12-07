# Febonnaci sequence of length N. take N from user
N=int(input('Enter Fibonnaci sequence length'))
n1,n2=0,1
sums=0
if N<0:
    print('No sequence found!!')
elif N==1:
    print(n1)
elif N==2:
    print(n1)
    print(n2)
elif N>=2:
    print(n1)
    print(n2)
    for i in range(N-2):
        sums=n1+n2
        n1=n2
        n2=sums
        print(sums)
