# video : https://youtu.be/ERCMXc8x7mc?si=iGzpJF-AqzNJq0XL
'''
    File I/O :- 
    --> python can be used to perform operations on a file(read and write data)
    --> types of files: 
        --> text files: 
            --> .txt
            --> .docx
            --> .log  , etc
        --> Binary files 
            --> .mp4
            --> .mov
            --> .png
            --> .jpeg    , etc
    --> at the end everything get stored in bits 
'''

'''
    reading a file :-
    --> we have to open a file before reading and writting.
    --> f = open( "file name","mode")
        --> mode : 
            r: read  , this is default mode 
            w: write 
        --> when file is opened stream of characters is returned 
'''

f= open(r"D:\PYTHON PROGRAMS\7) file handling-shraddha\demo.txt","r")  #here directly demo.txt is written .if the file is stored somewhere else then specify the complete path.
'''
    while getting during speciying path:
    --> use raw string : f = open(r"D:\PYTHON PROGRAMS\7) file handling-shraddha\demo.txt", "r")
    --> double backslashes: f = open("D:\\PYTHON PROGRAMS\\7) file handling-shraddha\\demo.txt", "r")
    --> forward slashes : f = open("D:\\PYTHON PROGRAMS\\7) file handling-shraddha\\demo.txt", "r")
'''

data = f.read()     #  to read the content of the file 
print(data , "\n")

# printing first few characters 
data2 = f.read(10)
print(data2 , "\n")
'''
    here nothing is printd : After call f.read(), 
    the file pointer moves to the end of the file.
    So, when f.read(10) is callled , it tries to read 10 more characters, 
    but there are no characters left, so it returns an empty string.
    solution : reset the file pointer using f.seek(0):
'''
f.seek(0)   # reset the file pointer to the begining of the file
data3 = f.read(10)
print(data3 , "\n")

print("type of data : ", type(data))
f.close()       # always close file so that no body could access it 

'''
    modes in open()
    --> 'r' : open a file (by default)
    --> 'w' : open for writting 
        --> deletes the previous data and writes the new one 
    --> 'x' : create a new file and open it for writting 
    --> 'a' : appends the data at the end 
    --> 'b' : open a binary file
    --> 't' : opens a text file(by default)
    --> '+' : open a disk file for updating( reading and writting )
    --> 'r+' : open for reading and writing. 
        --> over-writes from the starting of txt file. 
    --> 'w+' : open for reading and writting . over-writes
    --> 'a+' 
'''