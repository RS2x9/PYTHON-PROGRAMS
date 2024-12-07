# os.listdir("folder name")  :to check which folders(also known as directory) are in data directiory
import os
for i in os.listdir("data") :
    print(f"folder is: {i}")
    
print()

# checking any folder inside renamed folder
for i in os.listdir("data") :
    print(os.listdir(f"data/{i}"))     

print()

# os.getcwd()  : to know in which directory i am working
print('i am working in:',os.getcwd())

# os.chdir() : to change directory
