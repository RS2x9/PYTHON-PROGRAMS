import os
print(os.getcwd())
a=open("hello.txt","r")
print(a.read())
a.close()

b=open("hello.txt","w")
b.write(" i am using here")
b.close() 

# open("filename","r"),readline() : rad line by line
c=open("hello.txt")
while True:
    line=c.readline()
    print(line)
    if not line:
        break
c.close
