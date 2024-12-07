#consider dictionary M in the previous exapmle.write a program to modify marks of roll number
#obtain the roll number as input

#I will be creating dictionary:    my mood
M={}
roll,marks=[],[]
n=int(input("how many students are there?"))
for i in range(n):
    b,c=eval(input('Enter roll,marks'))
    roll.append(b)
    marks.append(c)
for i in roll:
    M[i]=marks[roll.index(i)]
print('Created dictionary:',M)
rollin=int(input('Enter rollto change value'))
marksch=int(input('Enter marks to change value'))
M[rollin]=marksch
print('New dictionary:',M)
