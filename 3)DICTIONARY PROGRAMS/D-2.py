#PROGRAM TO READ ROLL AND MARKS OF FOUR STUDENTS,CREATE DICTIONARY WHERE ROLL AS KEYS.
#CHECK WHETHER ROLL 2 HAS SCORED MORE THAN 75 OR NOT
dicti={}
roll=[]
marks=[]
while True:
    a=input('enter roll ,marks or type next to stop')
    if a=='next':
        break
    b,c=eval(a)
    roll.append(b)
    marks.append(c)
print('roll',roll)
print('obtained marks',marks)
for i in roll:
    dicti[i]=marks[roll.index(i)]
print('Created dictionary:',dicti)
print()
if dicti[2]>75:
    print('roll 2 has scored >75')
elif dicti[2]==75:
    print('roll 2 has scored exactly 75')
else :
    print('roll 2 has scored less than 75')
