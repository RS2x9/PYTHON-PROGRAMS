# READ STUDENT DETAILS LIKE NAME,USN,MARKS IN THREE SUBJECTS.DISPLAY THEM,TOTAL MARKS PERCENTAGE
name=input('Enter your name')
usn=input('Enter USN')
marks=[]
sub=['phy','chem','math']
for i in range(len(sub)):
    print('Enter marks in',sub[i])
    mark=int(input())
    marks.append(mark)
print(name)
print(usn)
print('total marks:',sum(marks))
print('percentage:',sum(marks)/len(marks))
