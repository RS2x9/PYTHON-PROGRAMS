''' THE DICTIONARY STORES THE roll_numbers:names OF STUDENTS WHO HAVE BEEN SELECTED TO PARTICIPATE IN
NATIONAL EVENT.WRITE A PROGRAM TO DISPLAY THE ROLL NUMBERS SELECTED WITH THEIR NAMES  '''
S,roll,names={},[],[]
while True:
    a=eval(input('Enter roll or type next'))
    b=input('Enter names or type next')
    if a=='next' or b=='next':
        break
    roll.append(a)
    names.append(b)
for i in roll:
    S[i]=names[roll.index(i)]
print('Created dictionary:',S)
print('selected roll numbers ,names are:')
for key in S:
    print(key,S[key])
