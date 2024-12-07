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
average2(1,5)           # python will ignore 9,1 and it will take a=1 ,b=5
average2(5)             #pyhton will take a=5 and value of b remains 1
average2(b=9)           # python will take value of a as 9 

print()

def name(fname,mname='John',lname='Whatson'):
    print("Hello",fname,mname,lname)
name("Amy")        #here name() is called, and Amy get stored in fname
name('Amy','Agarwall')     #Amy is stored in fname and Agarwall get stored in mname
name('Amy','Agarwall','Jain')

print()
#3) KEYWORD ARGUMENTS : arrangement of passed argument does not matter
def average3(a=9,b=1):
    print('average3 is:',(a+b)/2)
average3(b=9,a=21)     #value of a changed to 21 and of b to 9

print()
# required arguments examples
def name(fname,mname,lname):
    print('Hello',fname,mname,lname)
name('Peter','Ego','Quill')
