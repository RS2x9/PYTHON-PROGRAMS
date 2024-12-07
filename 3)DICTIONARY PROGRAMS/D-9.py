# WORKING WITH DICTIONARIES
#EMPTY DICTIONARY
employees={}
print('employees:',employees)

#dict()  :creates dictionary
employee1=dict(name='John',salary=10000,age=24)
print('employee1:',employee1)

#dict(zip(<key tuple sequence>,<values tuple sequence>))   :
#specific keys seperately and corresponding values separetely in tuple form
employee2=dict(zip(('name','salary','age'),('John',10000,24)))
print('emplouyee2:',employee2)

#using lists:
employee3=dict([['name','John'],['salary',10000],['age',24]])
print('employee3:',employee3)

#tuple containing list or tuple
employee4=dict((['name','John'],['salary',10000],['age',24]))
print('employee4:',employee4)

#using tuples
employee5=dict((('name','John'),('salary',10000),('age',24)))
print('employee5:',employee5)
