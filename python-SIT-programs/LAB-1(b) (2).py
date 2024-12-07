# person is senior citizen or not
name=input('Enter name')
y_birth=int(input('Enter year of birth'))
c_year=int(input('Enter current year'))
if c_year-y_birth>=60 :
    print(name,'is senior citizen')
else :
    print(name,'is not a senior citizen')
