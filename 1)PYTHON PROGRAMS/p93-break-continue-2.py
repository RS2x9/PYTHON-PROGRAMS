# break IN for LOOP
for letter in'amuls':
    if letter=='u':
        break
    else:
        print(letter)
print('thank you')
'''when letter=='u'  THEN break WILL COME IN THE PICTURE AND FROM LETTER u NO OTHER letterS WILL BE PRINTED
AND for LOOP GETS TERMINATED AND NEXT STATEMENT that is print('thank you') IS EXECUTED '''
print()

# continue IN for LOOP
for letter in 'amuls':
    if letter=='u':
        continue #when letter=='u':then u will not be printed continue returns the control again to for loop
    else:
        print(letter)
print('thank you')
print()    #just to create a new empty line

#continue IN while LOOP
var=10
while var>0:
    var=var-1
    if var==3:
        continue
    print(var)
print('thank you')
# MORE EXAMPLES
print()
var=10
while var>0:
    var=var-1
    if var==3:
        continue
    print('*')
print('thank you')
