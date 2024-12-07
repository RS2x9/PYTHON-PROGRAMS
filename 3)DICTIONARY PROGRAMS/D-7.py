'''  WRITE A PROGRAM TO CREATE A DICTIONARY M WHICH STORES THE MARKS OF STUDENTS OF CLASS WITH
ROLL NUMBERS AS THE KEYS AND MARKS AS THE VALUES.GET THE NUMBER OF STUDENTS AS INPUT        '''
M={}
roll,marks=[],[]
n=int(input('How many students are there?'))
for i in range(n) :
      a=input('Enter roll,marks')
      b,c=eval(a)
      roll.append(b)
      marks.append(c)
for i in roll:
    M[i]=marks[roll.index(i)]
print('Created Dictionary:',M)
