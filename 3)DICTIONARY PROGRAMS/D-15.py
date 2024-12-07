'''  write a ready-made dictionary which stores roll and marks.program to input a roll number
and delete it from dicionary.display error message if the roll number does not exist in dictionary   '''
M={1:67.3,2:54.5,3:77.9,4:89.9,5:83.5}
print('Created dictionary:',M)
rollin=int(input('Enter roll to delete'))
if rollin in M:
    del M[rollin]
    print('dictionary is:',M)
else :
    print('there is no',rollin,'existing in dictionary')
