# VARIABLE LENGTH ARGUMENTS :to pass more aruments than the variables defined
# method-1

def average(*numbers):
    print(type(numbers))         #so number is a tuple
    sum=0
    for i in numbers:
        sum=sum+i
    print('average is :',sum/len(numbers))
average(5,6,7,8,9,10)

print()
# METHOD-2
def name(**names):
    print(type(names))
    print("Hello",names["fname"],names["mname"],names["lname"])
name(mname='Buchanan',lname='Barnes',fname='James') # ** will this as dictionary key,value pair
