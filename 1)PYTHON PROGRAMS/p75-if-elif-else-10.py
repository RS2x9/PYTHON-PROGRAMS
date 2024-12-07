''' program to write whether a given character is
upper case or lower case or any other character,
if ordial number(ascii values)are already known'''

ch=float(input('enter ASCII VALUE or ORDIAL NUMBER any character:'))
if ch>=ord('A') and ch<=ord('Z') :
       print('you entered upper case character')
elif ch>=ord('a') and ch<=ord('z') :
    print('you entered lower case character')
else:
    print('you entered digit or special character')
''' ord('character')    this gives ASCII VALUE of any alphabet
if i know ASCII VALUE of any character then how to know that character '''
