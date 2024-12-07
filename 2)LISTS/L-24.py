#WRITE A PROGRAM TO TAKE INPUT AND CHECK IF THE MAXIMUM ELEMENT OF THE LIST LIES IN THE FIRST HALF
#OR IN SECOND HALF
L=[]
while True:
    a=input('enter integers to make list or type exit to stop')
    b=eval(a)
    L.append(b)
    if a=='exit':    #exit is keyword,its not an string
        L.pop()
        break    
print('Created list:',L)
print()
length=len(L)
while True:
    w=input('Enter element to be checked or type exit to stop')
    if w=='exit':
        break
    element=int(w)
    if length%2==0:
        if element not in L:
            print('Enter valid number') 
        for i in range(int(length/2)):
            if element==L[i]:
                print(element,'lies in first half at index',L.index(element))
        for j in range(int(length/2),length):
            if element==L[j]:
                print(element,'lies in second half at index',L.index(element))
    else:
        if element not in L:
            print('Enter valid number')
        else:
            for i in range(int(length/2)):
                if element==L[i]:
                    print(element,'lies in first half at index',L.index(element))
                elif L.index(element)==int(length/2):
                    print(element,'is at half point of list at index',L.index(element))
                for j in range(int(length/2)+1,length):
                    if element==L[j]:
                        print(element,'lies in second half at index',L.index(element))   
