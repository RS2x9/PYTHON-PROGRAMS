# reading one line at a time 
f= open(r"D:\PYTHON PROGRAMS\7) file handling-shraddha\demo.txt" , "r")
line1 = f.readline()
print( line1)
'''
    --> there is empty line getting printed at output
    --> at every ending line in the text document there is 
        \n character at the end which is being read 
'''
# now the pointer has gone to second line 
line2 = f.readline()
print(line2)
# the last was not ended with \n so no empty line is printed

f.close()