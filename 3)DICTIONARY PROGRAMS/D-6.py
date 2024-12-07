#program to input roll as keys and marks as values.check anyone scored marks as 89.9
M={}
roll,marks=[],[]
count=0
while True:
    a=input('Enter roll , marks or type next to see results')
    if a=='next':
        break
    b,c=eval(a)
    roll.append(b)
    marks.append(c)
for i in roll:
    M[i]=marks[roll.index(i)]
print('Created dictionary:',M)
for key in M:
    if M[key]==89.9:
        print('roll',key,'got:',89.9)
        count+=1
if count==0:
    print('no one got 89.9')
