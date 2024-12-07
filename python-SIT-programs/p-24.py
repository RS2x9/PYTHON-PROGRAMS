birthdays={'Alice':'April','Bob':'Dec 12','Carol':'Mar 4'}
while True:
    print('Enter a name:(blank to quit)')
    name=input()
    if name=='':
        break
    if name in birthdays:
        print(birthdays[name]+' is the birthday '+name)
    else:
        print('I dont have birthday information for',name)
        bday=input('What is their birthday?')
        birthdays[name]=bday
print('Updated dictionary',birthdays)
