import os
print(os.getcwd())
print()
# os.path.abspath('<relative path>') : gives absolute path f relative path
print(os.path.abspath('.'))

# os.path.isabs('<path>') : checks whether path is absolute or not
print(os.path.isabs(os.getcwd()))
print(os.path.isabs('.'))
print()
# os.relpath(total path,start)  : retuns relative path after start path
# if start path is not given then 
print(os.path.relpath(os.getcwd(),'C:\PYTHON PROGRAMS'))
print()
# filename is same as base name
# os.path.dirname(path) : givves everything without base name
# os.path.basename(path) : gives basename of path
print(os.path.dirname(os.getcwd()))
print(os.path.basename(os.getcwd()))

print()
# os.path.split(path)  : seperates the dirname and basename of path in tuple form 
print(os.path.split(os.getcwd()))
print(os.path.dirname(os.getcwd()),',',os.path.basename(os.getcwd()))   # both gives same result

print()
# to split each part of path in the form of list
print(os.getcwd().split(os.sep))
