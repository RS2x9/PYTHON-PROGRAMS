# IF WE WANT TO COME OUT OF THE LOOP BEFORE COMPLETING THE LOOP ,THEN WE USE break STATEMENT
# WE WANT TO SKIP SOME PART OF THE LOOP ,,THEN WE USE continue STATEMENT
#break :TERMINATES THE CURRENT LOOP AND IT CONTINUES THE EXECUTION OF NEXT STATEMENT
count=0
while count<=5:
    if count==3:
        break
    else :
        print(count)
    count=count+1
print('thank you')
'''WHEN count==3 THEN break WILL COME IN PICTURE AND IT WILL TERMINATE
                       THE while LOOP AND IT WILL EXECUTE THE NEXT STATEMENT that is print('thank you') '''

