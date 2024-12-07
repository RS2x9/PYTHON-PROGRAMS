# DEVELOPE A PYTHON PROGRAM TO print() 10 MOST FREQUENTLY APPEARING WORDS IN TEXT FILE
words=[]
file=open('Rishabh2.txt','r')    # r means reading mode
for line in file:    #reads one Line from file and stores in Line
     # splitting the line in words using split
    words.extend(line.split())
print(words)
print()
from collections import Counter     #Counter is a function
count=Counter(words)      #Counter() counts words
top10=count.most_common(10)     #most_common() is a function
print(top10)
file.close()      #closing the opened file is necesary
