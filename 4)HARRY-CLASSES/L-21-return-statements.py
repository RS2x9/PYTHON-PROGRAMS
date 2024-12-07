def average1(num):
    sum=0
    for i in num:
        sum=sum+i
    return sum/len(num)

# average(5,6,7,1) writting this only gives no output.

print(average1([5,6,7,1]))  

print()

# return matlab value ko leke wapas chale jao

def average2(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return 7
    return sum/len(numbers)
c=average2(5,6,7,1)
print(c)
''' the output is only 7 because python gives the value of first return
                so when average2() is called,only 7 is returned .After calling average()
                 7 is stored in c and then print() prints it'''
