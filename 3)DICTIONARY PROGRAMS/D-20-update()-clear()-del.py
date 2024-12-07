#<old dictionary>.update(new dictionary)   :

employee1={'name':'John','Salary':10000,'age':24}
employee2={'name':'Diya','Salary':54000,'dept':'Sales'}
employee1.update(employee2)
'''as key are immutable so the if the keys are same in both dictionaries then the value associated with the key
in the second dictionary will get replaced    '''
print('updated employee1:',employee1)

print()

# clear(): REMOVES ALL THE ITEMS OF THE DICTIONARY AND DICTIONARY BECOMES EMPTY
Employee={'name':'John','salary':1000,'age':24}
Employee.clear()
print(Employee)

print()
 # del statement  :deletes the whole dictionary
Employee={'name':'John','salary':1000,'age':24}
del Employee
# print(Employee)  #this gives error 
