#creating list
x=[12,34,'hi',34.5]      #list can store mixed datatype values
print(x)
a=[1,2,3]
print(bool(a))           #this will return True
#the truth value of empty list is False
b=[]
print(bool(b))           #empty list is eqiuvalent to 0,so it returns False
#we can create long lists,we can split across several lines
c=[1,2,3,4,4,5,6,7,
   12,15,13,14]
print(c)
#Nested Lists:list inside list
d=[1,2,3,[4,5,6,7]]
print(d)
#to extract elements of list
#forward indexing starts from 0
print(d[3])              #python treats [4,5,6,7] as a single element
#extracting elements of lists elements inside the list d
print(d[3][0])
print(d[3][1])
print(d[3][2])
print(d[3][3])

print()

