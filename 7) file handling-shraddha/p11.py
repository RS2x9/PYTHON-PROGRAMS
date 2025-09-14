# problem-3 : count of even numbers 
# method-1 

# in the text file there should be a comma at the end so that the program could to that point 
count=0
with open(r"D:\PYTHON PROGRAMS\7) file handling-shraddha\problem3.txt" , "r") as f:
    data = f.read()
    print(data, "\n")
    num=""      #empty string to store sting numbers
    for i in range(len(data)):
        if( data[i]==','):
            x = int(num)
            if(x%2==0) : 
                count+=1
            
            num=""
        else :
            num+=data[i]
print("count", count)
