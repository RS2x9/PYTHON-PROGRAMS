# not getting the  right answer
import os
print(os.getcwd()) ; print()

print(os.listdir(os.getcwd())) ; print()

for i in os.listdir(os.getcwd()):
    print(os.path.join(os.getcwd(),i))
print()
print(os.path.getsize(os.getcwd()))
print()
# example :to get total size of all the files in the directory
total=0
for i in os.listdir(os.getcwd()):
    total=total+os.path.getsize(os.path.join(os.getcwd(),i))
print(total)
