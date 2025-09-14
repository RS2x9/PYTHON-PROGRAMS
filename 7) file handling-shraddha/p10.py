# problem-2
'''
    write a function in which line of the file does the word "learning" occur first.
    print -1 if the word not found
'''

def check_for_line() :
    line_num =1
    word = "learning"
    data = True    # represents data fetched is True 
    with open(r"D:\PYTHON PROGRAMS\7) file handling-shraddha\problem1.txt" , "r") as f:
        while True:     #runs till the end of the file 
            data = f.readline()
            if (word in data) : 
                print(line_num)
                return
            line_num+=1
    return -1

check_for_line()