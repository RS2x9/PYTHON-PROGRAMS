#make a dictionary and add roll numbers marks in the dictionary

#I am taking 5 students initially
M={1:89,2:100,3:79,4:90,5:98}
print('Initial Dictionary:',M)
n=int(input('How many students you need to add?'))
# adding other students data
for i in range(n):
    addroll=int(input('Enter roll:'))
    addmarks=int(input('Enter marks:'))
    M[addroll]=addmarks   
print('New dictionary:',M)
