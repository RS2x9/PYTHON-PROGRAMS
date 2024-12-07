# with : automatically closes the file 

with open("HARRYL49-F1.txt","a") as f:
    f.write("\n Hey i am here using with statement")   #\n :to print in next line
    
a=open("HARRYL49-F1.txt")
print(a.read())
a.close()
