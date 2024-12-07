x=4
print(x)
def hello():   # to define function of our choice we use def
    x=5
    y=1
    print(f"{x},this {x} prints because x={x} is local varible here")
    print('Hello')
print(f"{x}, this {x} prints because x={x} is global variable")
hello()      # function is called
print(f"{x}, this {x} prints because x={x} is global variable")
#print(y) # Error : y is not defined outside hello().when hello() will be called then only y will be printed.
         # untill and unless y is defined outside
print()

# global :This keyword makes the locally defined variable as global
x1=10
def my_function() :
    global x1
    x1=20
    y1=1
    print(y1)
    # print(x1) : this will give error because x1 is not now a local variable
my_function()
print(x1)   #since x1 is defined globally so value of x1 changed to 20 from 10
