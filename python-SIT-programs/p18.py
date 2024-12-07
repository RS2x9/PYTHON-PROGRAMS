#return values and return statements
print(len('hello'))  #5 is returned.so 5 is returned value
spam=print('hello')
print(spam)
print(None==spam)  #true is returned because hello is stored in print()
print()
#Local and Global scope
eggs=100
def spam():
    eggs=31337
    print(eggs)
spam()  #eggs under spam() will get printed
print(eggs) 
