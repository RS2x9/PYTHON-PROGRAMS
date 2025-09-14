'''
    'w+' : 
    --> open for reading and writting . 
    --> If the file already exists, it truncates (deletes) all previous content.
    --> If the file does not exist, it creates a new file.
'''

# txt  file already created 
f=open(r"D:\PYTHON PROGRAMS\7) file handling-shraddha\demo5.txt" , "w+")    # all the previous content is deleted 
'''
    text pre-written:
    Circuits hum where silence dwells, a mind in code begins to dream,
    Through wires and waves, it learns to see the world in data’s gleam.

'''
f.write("hello world")      # this is over-written in file 
f.close()