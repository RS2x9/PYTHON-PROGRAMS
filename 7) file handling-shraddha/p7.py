# with
# the file will get automatically closed after with block is exited 

with open(r"D:\PYTHON PROGRAMS\7) file handling-shraddha\demo6.txt" , "a+") as f:
    f.seek(0)   # file pointer was pointing at the end of file 
    data = f.read()
    print(data)