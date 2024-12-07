''' WRITE A PROGRAM THAT INPUTS A LIST,REPLICATES IT TWICE AND PRINTS THE SORTED LIST
IN ASCENDING AND DESCENDING ORDER   '''
#CODE-1
List=[]
while True:
    a=input('Enter list elements or enter exit to stop')
    List.append(a)
    if a=='exit':
        List.pop() #pop() is used to remove '' from the created list which gets appened at the last
        break
print('Created list is:',List)
print('REplicated list:',List*2)
List.sort()
print('ascending order:',List)
List.sort(reverse=True)
print('descending order:',List)
print()

#CODE-2
list=eval(input('Enter List'))
print('Created List is',list)
print('replicaed list is',list*2)
list.sort()
print('list in ascending oder',list)
list.sort(reverse=True)
print('list in descending order',list)
