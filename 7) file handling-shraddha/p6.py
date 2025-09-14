'''
    'a+' mode :
    --> for reading and writting 
    --> the file pointer points to the end of the file opening it 
    
'''

f= open(r"D:\PYTHON PROGRAMS\7) file handling-shraddha\demo5.txt" , "a+")
print(f.read())     # file pointer is pointing at the end of file 
f.write("\n nice to meet you")

f.seek(0)       # file pointer is pointing at the start of file
print(f.read())
f.close()