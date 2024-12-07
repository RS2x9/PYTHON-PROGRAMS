# TUPLES ARE IMMUTABLE .TO MANUPULATE IT, CONVERT THEM TO LIST AND THEN BACK TO TUPLES
countries=('Spain','Italy','India','England','Germany')
temp=list(countries)
temp.append('Russia')
temp.pop(3)
temp[2]='Finland'
countries=tuple(temp)
print(countries)

# CONCATINATING TUPLES
states=('Jharkhand','Karataka','Bihar')
cs=countries+states
print(cs)

print()
 
# count() :returns number of repeated items
tuple1=(0,1,2,3,31,1,3,2)
print('count of 3 is:',tuple1.count(3))

# index()
print('index of 1:',tuple1.index(1))
# we can find index of any thing in slice using index(<value>,<start index>,<end index>)
print(tuple1.index(3,3,7))
print(tuple1.index(1,3,7))

