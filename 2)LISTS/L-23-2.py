#WRITE A PROGRAM TO COUNT THE FREQUENCY OF GIVEN ELEMENT IN THE LIST
lst=eval(input('enter list'))
length=len(lst)
element=int(input('Enter the element:'))
count=0
for i in range(length):
    if element==lst[i]:
        count+=1
if count==0:
    print(element,'not found in the given list')
else:
    print(element,'has frequency as',count,'in given list')