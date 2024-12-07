n=int(input("Enter any number>=0:"))
def fac(n):
    if n==0 or n==1 :
        return 1
    if n>=0:
        return n*fac(n-1)
print(fac(n))
