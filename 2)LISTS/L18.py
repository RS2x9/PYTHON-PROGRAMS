# WRITE A PROGRAM THAT DISPLAYS OPTIONS FOR DELETING ELEMENTS IN A LIST WITH OPTION FOR:
#if element is to be deleted with value or by using its position or a slice of list to be deleted
L=[10,20,30,40,50,60,70,80,90]
print('list is:',L)
print('Enter 1 to delete element of list by value:')
print('Enter 2 to delete element of list by index:')
print('Enter 3 to delete slice of list')
ch=int(input('enter your choice:'))
if ch==1:
      d_value=int(input('enter value:'))            
      L.remove(d_value)
      print('modified list',L)
if ch==2:
                  d_index=int(input('enter index'))
                  del L[d_index]
                  print('modified list',L)
                  
if ch==3:
                  di_start=int(input("enter first index"))
                  di_end=int(input('enter last index'))
                  del L[di_start:di_end+1]
                  print('modified list',L)
    

# this program is running well on programmiz 
