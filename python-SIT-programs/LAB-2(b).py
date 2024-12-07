# FACTORIAL OF A NUMBER
n=int(input('Enter number to find factorial:'))
f=1
if n==0 or n==1:
    print('factorial of',n,'is',1)
elif n>1:
    for i in range(1,n+1) :
        f=f*i
print(f)

print()

# COMPUTE BINOMIAL COFFICIENT
f1,f2,f3=1,1,1
N=int(input('Input N'))
R=int(input('Input R'))
c=N-R
# finding factorial of N
for i in range(1,N+1) :
    f1=f1*i
for j in range(1,R+1):
    f2=f2*j
for k in range(1,c+1):
    f3=f3*k
bin_cof=f1/(f2*f3)
print('Binomial cofficient:',int(bin_cof))
