# GLOBAL STATEMENT
print("code1")
def spam():
    global eggs
    eggs='Spam'
eggs='global'
spam()
# if global is used in local scope then pyhton dont care about that varible defined outside local scope
print(eggs)

print()
print('code2')
# GLOBAL STATEMENT
def spam():
    global eggs
    eggs='Spam'
    print(eggs)
eggs='global'
spam()
print(eggs)

print()
print('code3')
def spam():
    global eggs
    eggs = 'spam'        # this is the global
def bacon():
    eggs = 'bacon'       # this is a local
def ham():
    print(eggs)           # this is the global
eggs = 42               # this is the global
spam()
print(eggs)
