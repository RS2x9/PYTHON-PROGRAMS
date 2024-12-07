#exit() : USED TO END THE PROGRAM
#WE HAVE TO FIRST IMPORT sys module
import sys
while True:
    print('type exit to exit').lower()
    response=input()
    if response=='exit':
        sys.exit()
print('you typed'+response+'.')
