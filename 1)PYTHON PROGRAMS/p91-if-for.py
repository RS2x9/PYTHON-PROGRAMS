#print the sum of even numbers upto(and including) n 
n =int(input("Enter"))
sums=0
if n%2==0:     # n is even
    for i in range(1,n+1):
        if i%2==0:
            sums=sums+i
if n%2!=0:        #n is odd
    for i in range(1,n+1):
        if i%2==0:
            sums=sums+i
        if i==n:
            sums=sums+i
print('sum:',sums)
