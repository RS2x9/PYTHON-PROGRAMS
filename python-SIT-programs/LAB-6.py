# DEVELOPE A PROGRAM TO SORT THE CONTENTS OF A TEXT FILE AND WRITE THE SORTED CONTENTS INTO A SEPERATE TEXT FILE.
words=[]
file1=open('Rishabh2.txt','r')    #only reading this file
for line in file1:
    words.extend(line.split())
file1.close()
words.sort()
print(words)
file2=open('Rishabh1.txt','w')   #w: we can add words to this file
for i in words:
    file2.write(i +'\n')  #go & see 'Rishabh1.txt',words has been added
file2.close()
