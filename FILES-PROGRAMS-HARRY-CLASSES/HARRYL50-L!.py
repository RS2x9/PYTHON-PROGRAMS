f1=open("HARRYL49-F1.txt")
# open("<filename>","mode").readline()    :to read lines in file line by line
while True:
    line=f1.readline()                 
    print(line,type(line))      #see the outputs careful 
    # always write the below statements otherwise lope will run infinitely
    if not line:
        break
    ''' after reading both the lines it will execute this statement
                              and after break class string  is shown due to  type(line) only '''
       
    
print()
print()
print()
# now see the difference in the output
f2=open("HARRYL49-F1.txt")
while True:
    line1=f2.readline()
    print(line1)
    if not line1:
        print(line1,type(line1))  #now line is not there then also python prints type(line1) as string
        break
f2.close()
