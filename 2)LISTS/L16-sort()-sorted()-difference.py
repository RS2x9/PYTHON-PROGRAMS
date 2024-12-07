                          # sort()  AND sorted()   DIFFERENCE
#sorted() works on iterable sequence like list,tuple,etc AND RETURNS A NEW LIST
#sort() works only on list
a='cab'
b=sorted(a)   #PRINTS ELEMENTS IN ASCENDING ORDER
print(b)
c=sorted(a,reverse=True)
print(c)
print()

T=(1,3,2,4,5,4)
TA=sorted(T)
print(TA)
TRA=sorted(T,reverse=True)
print(TRA)
