#PROGRAM TO TAKE INTEGERS FROM USER AND PRINT ITS MEAN
L=[]
while True:
    a=input('Enter numbers for mean or type exit to stop')
    b=eval(a)
    L.append(b)
    if a=='exit':
        L.pop()
        break
print('Created list is:',L)
sum=sum(L)
length=len(L)
mean=sum/length
print('mean is',mean)
