# problem-1
'''
    --> Add the following data :
        hi everyone 
        we are learning File I/O
        using Java
        I like programming in Java.
    
    --> replace all the occurences of "java" with "pyhton" 
    --> search if the word "learning" is there in file or not
'''

with open(r"D:\PYTHON PROGRAMS\7) file handling-shraddha\problem1.txt" , "w") as f:
    f.write("hi everyone\nwe are learning File I/O\nusing Java\nI like programming in Java.")

with open(r"D:\PYTHON PROGRAMS\7) file handling-shraddha\problem1.txt" , "r") as f2:
    data = f2.read()

new_data = data.replace("Java", "python")

with open(r"D:\PYTHON PROGRAMS\7) file handling-shraddha\problem1.txt" , "w") as f3:
    f3.write(new_data)

print(new_data)

with open(r"D:\PYTHON PROGRAMS\7) file handling-shraddha\problem1.txt" , "r") as f4 :
    data2 = f4.read()
    if data2.find("learning") : print("\nFound")
    else : print("\nNot found")