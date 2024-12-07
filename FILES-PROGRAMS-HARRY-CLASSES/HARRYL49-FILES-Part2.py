# open("<filename>","w").write("write anything")  : to write in File. This will repalce the content of file
# open("<filename>","a").write("write anything"): to add at last in File in the existing content

f=open("HARRYL49-F1.txt","w")
f.write("Hahaha .how are you")
#print(f.write("Hahaha"))    #this will print the number of characters
                            #and adds one more Hahaha at the end
f.close()    # we should close after doing any operation otherwise no output is seen

# to see what we have written. read the file
f1=open("HARRYL49-F1.txt","r")
print(f1.read())
f1.close()
