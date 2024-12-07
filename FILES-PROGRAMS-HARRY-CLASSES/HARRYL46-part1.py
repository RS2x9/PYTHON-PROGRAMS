import os     # built in module of python
# os.mkdir("<foldername>")  : creates folder

# creating 2 folders in data folder
'''  for i in range(2):
       os.mkdir(f"data\day{i+1}")  '''  # when i=0,gives error as data already exists

if (not os.path.exists("data")):     #checks whether folder name data exists or not
    os.mkdir("data")
for i in range(2):
    os.mkdir(f"data/trial{i+1}")
