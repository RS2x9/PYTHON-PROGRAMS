#example
a,b=9,8
gmean1=(a*b)/(a+b)
print(gmean1)
c,d=8,7
gmean2=(c*d)/(c+d)
print(gmean2)

print()
# we can write this whole program by defining functions

def calculategmean(a,b):   #calculategmean is the name of function & a,b are arguments
    mean=(a*b)/(a+b)
    print(mean)
a,b=9,8
calculategmean(a,b)     #we are calling the defined function
c,d=8,7
calculategmean(c,d)
