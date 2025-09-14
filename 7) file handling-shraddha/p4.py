'''
    --> 'r+' : open for reading and writing. 
        --> over-writes from the starting of txt file. 
    --> if the file name do not  exists then it do not create a new file 
'''
f=open(r"D:\PYTHON PROGRAMS\7) file handling-shraddha\demo3.txt" , "r+")
f.write("this is Rishi Narayan")
f.write("hello")        # this get appended at the end of line 
# now the file pointer is at the end of the file 
f.seek(0)       # used to point to the start of the file 
print(f.read())
f.close()

# there is difference between in writting the above and below  code 

print("\n")
f2=open(r"D:\PYTHON PROGRAMS\7) file handling-shraddha\demo4.txt" , "r+")
# pre-written text in file : This is embedded engineer
f2.write("hello")       # this over-writes from the start of the line 
# the file pointer is after the word : hello
f2.seek(0)      # used to point to the start of the file 
print(f2.read())
f2.close()