#PROGRAM TO INPUT INTEGERS COUNT THE FREQUENCYOF ELEMENT IN A LIST
L=[]
while True:
    a=input('Enter integers or type exit to stop')
    b=eval(a)
    L.append(b)
    if a=='exit':
        L.pop()
        break
print('Created List:',L)    
length=len(L)
for i in range(length):
    L.count(L[i])
    print('frequency of',L[i],'is',L.count(L[i]))
