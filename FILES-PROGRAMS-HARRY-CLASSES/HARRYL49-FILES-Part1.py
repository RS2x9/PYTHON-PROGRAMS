'''  open("<file name>,"<mode>") :to open file
 r=reading  ; a=append ; w=write    '''

f=open("HARRYL49-F1.txt","r")   #"r' is the defaut mode

print(f)      #this dont gives the result we want

# open("<filename>","mode").read()   :to read text stored in file

print(f.read())   # if write mode is used with read() then Error

#we should always close the file by:  open("<file name>,"<mode>").close()
f.close()

#intresting: if we use file which do not exists with write mode then new file will get created
f2=open("HARRYL49F2.txt","w")
print(f2)

print()
# open("<file name>,"rb")  :to read file in binary
print(open("HARRYL49-F1.txt","rb").read())    # see b is there in output:represents binary

print()

