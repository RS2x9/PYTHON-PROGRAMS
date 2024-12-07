print() ; print("Devil!!!".center(50)) ; print()

import os
print(os.getcwd())
# os.path.exists(path)  : check path exists or not
print(os.path.exists(os.getcwd()))
print()
# os.path.isdir(path) : checks whether file exists or not
print(os.path.isdir(os.getcwd()))
print()
# os.path.isfile(filename) : checks file exists or not
print(os.path.isfile('reading and writing files'))   # this is giving error
print()
# to check whrther any drive exists in computer:
print(os.path.exists('C:\\'))
print(os.path.exists('D:\\'))
