'''
    writting to file:-
    --> open("file path" , "w") : over-writes the entiire data 
    --> open("file path" , "a") : appends the data at the end 
    --> if the specified do not exist then using "a" , "w" : new file 
        will be created.
    --> we can't read the file during writting modes 
        again open the file after closing it to read the contents.
''' 

# "w" mode :-
f1 = open(r"D:\PYTHON PROGRAMS\7) file handling-shraddha\demo2.txt" , "w")  # demo2.txt will also be created 
f1.write("This is Rishi Narayan \nlearning file handling ")
f1.close()

# "r" mode :-
f2 = open(r"D:\PYTHON PROGRAMS\7) file handling-shraddha\demo2.txt" , "r")
data = f2.read()
print(data)
f2.close()

# "a" mode :-
f3 = open(r"D:\PYTHON PROGRAMS\7) file handling-shraddha\demo2.txt", "a")
f3.write("\n Aim is to become Data Scientist")
f3.write("\nThis is the best role will fit me in")
f3.close()

# "r" mode:-
print("\n")
f4 = open(r"D:\PYTHON PROGRAMS\7) file handling-shraddha\demo2.txt" , "r")
data2 = f4.read()
print(data2)
f4.close()