                     # THERE ARE FOUR TYPES OF ARGUMENTS WE CAN PROVIDE IN FUNCTION

#1) REQUIRED ARGUMENTS
def average1(a,b):             #a,b are required arguments   
    print("The average1 is",(a+b)/2)
average1(4,6)
print()
#2) default arguments
def average2(a=9,b=1):
    print('The average2 is:',(a+b)/2)
average2()
average2(1,5)
average2(5)             #pyhton will take a=5 and value of b remains 1
average2(b=9)          # python will take value of a as 9 
print()
