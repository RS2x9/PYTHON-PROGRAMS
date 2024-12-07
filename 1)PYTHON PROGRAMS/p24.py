#22) input a digit and print a three digit number as <n(n+10)(n+2)>
d=int(input("enter a single digit"))
val=d*10+d+1
val=val*10+d+2
print('output is:',val)
