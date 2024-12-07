# PROGRAM TO PRINT FREQUENCY OF EACH DIGIT 
number=int(input('Enter any number'))
print('Digit \t Frequency')
for i in range(10):
    count=0
    temp=number
    while temp>0:
        digit=temp%10
        if digit==i:
            count+=1
        temp=temp//10
    if count>0:
        print(i,'\t',count)
