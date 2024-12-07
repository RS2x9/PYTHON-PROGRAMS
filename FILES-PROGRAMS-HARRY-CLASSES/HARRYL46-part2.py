# os.rename(<old name>,<new name>) to change the name of folder
import os
for i in range(2):
    os.rename(f"data/trial{i+1}",f"data/renamed {i+1}")
