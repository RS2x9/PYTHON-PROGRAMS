# method-2
# split() : splits the data inside in the form of list

count=0
with open(r"D:\PYTHON PROGRAMS\7) file handling-shraddha\problem3-2.txt" , "r") as f:
    data = f.read()
    nums= data.split(",")
    print(nums , "\n")
    for i in range(len(nums)):
        if (int(nums[i]) %2 ==0) : count+=1

print("count: " , count)