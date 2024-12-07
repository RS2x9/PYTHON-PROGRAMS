#Dictionary={immutable key:value,immutable key:value,........}

#PROGRAM TO READ ROLL NUMBERS AND MARKS OF FOUR STUDENTS AND CREATE A DICTIONARY,ROLL as keys
dicti={}
roll=[]
marks=[]
while True:
    a=input('Enter roll numbers:,marks: or type next')
    if a=='next':
        break
    b,c=eval(a)
    roll.append(b)
    marks.append(c)   
print(roll)
print(marks)
leng_roll,leng_marks=len(roll),len(marks)
for i in roll:
    dicti[i]=marks[roll.index(i)]    #adding value at specified key in dictionary
    print('Created dictionary',dicti)
print(dicti)
