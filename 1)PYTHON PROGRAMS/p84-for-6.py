#in all the questons nested for is used
'''1) here nothing will get printed because range(1,1) means we are taking i=1
and we are not taking i=1.so nothing will get printed  '''
for i in range(1,2):
    for j in range(1,i):
        print('*',end='')
    print()
#2)
for i in range(1,3):
    for j in range(1,i): # for i=1,nothing will get printed
        print('&',end='')
    print()    #using print() here we can actually how many * are printing for each value of j
#3)
for i in range(1,4):
    for j in range(1,i): #for i=1,nothing will get printed
        print('*',end='')
    print()
#4)
for i in range(1,5):
    for j in range(1,i): #for i=1,nothing will get printed
        print('$',end='')
    print()
#5)
for i in range(1,6) :
     for j in range(1,i) : #for i=1,nothing will get printed
         print('@',end='')
     print()
