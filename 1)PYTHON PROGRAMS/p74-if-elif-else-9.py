''' program to write whether a given character is
upper case or lower case or a digit or any other character'''

while True:
    ch=input('enter character')
    if ch>='A' and ch<='Z' :
        print('you entered upper case character')
    elif ch>='a' and ch<='z' :
        print('you entered a lower case character')
    elif ch>='1' and ch<='9' :
        print('you entered a digit')
    else :
        print('you enetered special chaacter')
