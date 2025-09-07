#1
for i in range(1,6):
    print('*')
#2
print()                              # written to just create gap between first and second program
for i in range(1,6):
    print('-->')                       #when no end='' is used then all the stars will be verticle
print()                              # written to just create gap between first and second program 
#3
for i in range(1,6):
    print('* ',end='')               #end='' ,this makes all the stars horizontal
print()
#4
print()
for i in range(1,6):
    print('!',end='')
print()
#5
for i in range(1,6):
    for j in range(1,i):
        print('% ',end='')
#6
print()                   #used only to create gap between 5th and 6th program
for i in range(1,6):
    for j in range(1,i):
        print('%',end='')
    print()       #this print() creates the difference between 5th and 6th program
