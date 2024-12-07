'''     write python code to add odd numbers up to( and incliding)

a given value N and print the result  '''
N=int(input("Enter"))
sums=0
if N%2!=0:      # N is odd
    for i in range(1,N+1):
        if i%2!=0:
            sums=sums+i
if N%2==0:     # N is even
    for i in range(1,N+1):
        if i%2!=0:
            sums=sums+i
        if i==N:
            sums=sums+i
print('sum:',sums)
